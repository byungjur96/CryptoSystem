<template>
    <div class="container">
        <!-- Encryption / Decryption -->
        <div>수행할 작업을 골라주세요.</div>
        <p>
            <input type="radio" id="work1" value="enc" v-model="work" v-on:click="getParam">
            <label for="work1">Encryption</label>
        </p>
        <p>
            <input type="radio" id="work2" value="dec" v-model="work" v-on:click="getParam">
            <label for="work2">Decryption</label>
        </p>

        <!-- Text 입력 -->
        <div>{{ message[work] }}를 입력해주세요.</div>
        <input v-model="input" id="input" :placeholder="message[work]">

        <!-- Parameter 입력 -->
        <div>Parameter를 입력해주세요.</div>
        <div v-for="param in params[work][algorithm]" v-bind:key="param[work]">
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
            work: "enc",
            params: {},
            value: {},
            message: {
                "enc": "Plaintext",
                "dec": "Ciphertext"
            }
        }
    },
    props: ['mode'],
    methods: {
        requestSubmit: function() {
            if (this.$store.state.algorithm !== "" && this.$data.input !== undefined) {
                let param = {};
                this.$data.showResult = true;
                param[ this.$data.message[this.$data.work] ] = this.$data.input;
                for (let p of this.$data.params[this.$data.work][this.$store.state.algorithm]) {
                    param[p] = this.$data.value[p];
                }
                axios.post("http://0.0.0.0:5000/"+this.$store.state.algorithm+"/"+this.$data.work, param)
                    .then(res => {
                        this.$data.output = res.data["result"]
                    });
            } else {
                alert("양식에 맞춰서 다시 제출해 주세요.");
            }
        },
        getParam: function() {
            axios.get("http://0.0.0.0:5000/params")
                .then(res => {
                    this.$data.params = res.data;
                });
        }
    },
    computed: {
        option: function() {
            this.getParam();
            if (this.$data.work === "enc") return "Encrypt";
            else if (this.$data.work === "dec") return "Decrypt";
            else return undefined;
        },
        asciiVal: function() {
            this.$data.input.charCodeAt()
        },
        algorithm: function() {
            return this.$store.state.algorithm;
        }

    },
    created: function() {
        this.getParam();
    }
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
        width: 20px;
        margin-top: 5px;
        margin-bottom: 5px;
        margin-left: 4px;
    }
    .param {
        width: calc(100% - 30px);
        margin-top: 5px;
        margin-bottom: 5px;
    }
}
</style>