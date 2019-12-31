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
        <div v-if="showResult" class="result">{{ output }}</div>
        <button v-on:click="requestSubmit" id="submit">{{ mode }}</button>
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
            category: "rsa",
            message: {
                "Encrypt": "Plaintext",
                "Decrypt": "Ciphertext"
            }
        }
    },
    props: ['mode'],
    methods: {
        requestSubmit: function() {
            if (this.$data.category !== "" && this.$data.input !== undefined) {
                this.$data.showResult = true;
                this.$data.output = this.$data.input
                let param = {
                    "ciphertext": "1220703125",
                    "d": "9178373396735665477",
                    "n": "9943237852845877651"
                }
                axios.post("http://0.0.0.0:5000/dec/rsa", param)
                    .then(res => {
                        console.log(res.data);
                    })
            } else {
                alert("양식에 맞춰서 다시 제출해 주세요.");
            }
        }
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
}
</style>