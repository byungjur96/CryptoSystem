<template>
    <div class="container">
        <div>복호화 알고리즘을 골라주세요.</div>
        <select class="category" v-model="category">
            <option value="rsa">RSA</option>
            <option value="des">DES</option>
            <option value="des">AES</option>
        </select>
        <div>Ciphertext를 입력해주세요.</div>
        <input v-model="ciphertext" id="ciphertext" placeholder="Ciphertext">
        <button v-on:click="requestSubmit" id="submit">Decrypt</button>
    </div>
</template>

<script>
export default {
    name: 'Decrypt',
    data: function() {
        return {
        ciphertext: undefined,
        category: ""
        }
    },
    methods: {
        requestSubmit: function() {
            if (this.$data.category !== "" && this.$data.ciphertext !== undefined) {
                alert("등록되었습니다");
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

    .price {
        display: flex;
        border-width: 2px;
        border-style: inset;
        border-color: initial;
        border-image: initial;
        justify-content: center;
        align-items: center;
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