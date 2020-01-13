<template>
    <div class="container">
        <div>암호화 알고리즘을 골라주세요.</div>
        <select class="category" v-model="category">
            <option value="rsa">RSA</option>
            <option value="des">DES</option>
            <option value="des">AES</option>
            <option value="des">ElGamal</option>
        </select>
        <div>{{ message[mode] }}를 입력해주세요.</div>
        <input v-model="input" id="input" :placeholder="message[mode]">
        <!-- Parameter -->
        <div>Parameter를 입력해주세요.</div>
        <div v-for="param in params[category]" v-bind:key="param[0]">
            <span class="param-info">{{ param }}</span>
            <input class="param" v-model="value[param]" :placeholder="param">
        </div>
        <div v-if="showResult" class="result">{{ output }}</div>
        <button v-on:click="requestSubmit" id="submit">{{ option }}</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'contents',
    data: function() {
        return {
            input: undefined,
            output: undefined,
            showResult: false,
            params: {},
            value: {},
            category: "rsa",
            message: {
                "enc": "Plaintext",
                "dec": "Ciphertext"
            }
        }
    },
    props: ['mode'],
    methods: {
        requestSubmit: function() {
            if (this.$data.category !== "" && this.$data.input !== undefined) {
                let param = {};
                this.$data.showResult = true;
                param["ciphertext"] = this.$data.input;
                for (let p of this.$data.params[this.$data.category]) {
                    param[p] = this.$data.value[p];
                }
                axios.post("http://0.0.0.0:5000/"+this.$props.mode+"/"+this.$data.category, param)
                    .then(res => {
                        console.log(res.data);
                        this.$data.output = res.data["plaintext"]
                    });
            } else {
                alert("양식에 맞춰서 다시 제출해 주세요.");
            }
        },
        getParam: function() {
            axios.get("http://0.0.0.0:5000/"+this.$props.mode+"/list")
                .then(res => {
                    this.$data.params = res.data;
                    console.log(this.$data.params);
                });
        }
    },
    computed: {
        option: function() {
            if (this.$props.mode === "enc") return "Encrypt";
            else if (this.$props.mode === "dec") return "Decrypt";
            else return undefined;
        }
    },
    created: function() {
        this.getParam();
    },
}
</script>

<style>
@media (max-width: 480px) {
    .container {
        width: 100%;
        padding-top: 50px;
        height: calc(100vh - 100px);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .container > * {
        margin: 10px;
        width: 80%;
    }

    .category {
        border: solid black 1px;
    }

    #submit {
        width: 100%;
        height: 32px;;
        margin-top: auto;
        margin-bottom: 0;
        margin-left: 0;
        margin-right: 0;
        background-color: white;
    }
    .result {
        width: 80%;
        height: 50px;
        border: 1px solid black;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .param-info {
        width: 15px;
        margin-top: 5px;
        margin-bottom: 5px;
        margin-left: 4px;
    }
    .param {
        width: calc(100% - 25px);
        margin-top: 5px;
        margin-bottom: 5px;
    }
}
</style>