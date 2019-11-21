<template>
    <div class="container">
        <div>암호화 알고리즘을 골라주세요.</div>
        <select class="category" v-model="category">
            <option value="rsa">RSA</option>
            <option value="des">DES</option>
            <option value="des">AES</option>
        </select>
        <div>Plaintext를 입력해주세요.</div>
        <input v-model="plaintext" id="plaintext" placeholder="Plaintext">
        <button v-on:click="requestSubmit" id="submit">Encrypt</button>
    </div>
</template>

<script>
export default {
    name: 'Encrypt',
    data: function() {
        return {
        plaintext: undefined,
        category: ""
        }
    },
    methods: {
        requestSubmit: function() {
            if (this.$data.category !== "" && this.$data.plaintext !== undefined) {
                console.log(this.$data.category);
                console.log(this.$data.plaintext);
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