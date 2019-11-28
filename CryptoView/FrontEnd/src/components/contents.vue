<template>
    <div class="container">
        <div>암호화 알고리즘을 골라주세요.</div>
        <select class="category" v-model="category">
            <option value="rsa">RSA</option>
            <option value="des">DES</option>
            <option value="des">AES</option>
        </select>
        <div>{{ message[mode] }}를 입력해주세요.</div>
        <input v-model="text" id="plaintext" :placeholder="message[mode]">
        <button v-on:click="requestSubmit" id="submit">{{ mode }}</button>
    </div>
</template>

<script>
export default {
    name: 'contents',
    data: function() {
        return {
            text: undefined,
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
            if (this.$data.category !== "" && this.$data.text !== undefined) {
                console.log(this.$data.category);
                console.log(this.$data.text);
                console.log(this.$props.mode);
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
}
</style>