<template>
  <div id="modal">
    <div class="layout" @click="closeModal()"></div>
    <div class="pop-up">
      <h3>Key Generator</h3>
      <div id="key" v-if="keyExist()">{{ key }}</div>
      <button @click="generateKey()">Generate</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data: function() {
    return {
      key: undefined
    }
  },
  methods: {
    generateKey: function() {
      axios.get("http://0.0.0.0:5000/keygen/"+this.$store.state.algorithm)
              .then(res => {
                  console.log(res.data);
                  this.$data.key = res.data;
              });
      },
    closeModal: function() {
      this.$store.commit('open_modal');
    },
    keyExist: function() {
      return key !== undefined;
    }
  },
  
}
</script>

<style>
  #modal {
    position: relative;
    z-index: 100;
    width: 100%;
    height: 100%;
  }
  .layout {
    position: absolute;
    width: 100vw;
    height: 100vh;
    background-color: black;
    opacity: 0.5;
  }
  .pop-up {
    position: absolute;
    left: calc(50vw - 100px);
    top: calc(50vh - 150px);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    border: 1px solid black;
    width: 200px;
    height: 300px;
    background-color: white;
  }

  .pop-up > h3 {
    margin-top: 20px;
  }

  .pop-up > button {
    margin-bottom: 30px;
  }
</style>