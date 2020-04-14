<template>
  <div id="side-menu" class="side-open">
    <div 
        v-for="algorithm in algorithms" 
        v-bind:key="algorithm" 
        v-on:click="changeAlg(algorithm)"
        class="side-option">
        {{ algorithm }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'side-bar',
  data: function() {
      return {
          algorithms: [],
          isSideOpened: true
      }
  },
  methods: {
        changeAlg: function(string) {
            this.$store.commit('change', string);
            this.$emit('menuSelect');
        },
        getAlgorithm: function() {
            axios.get("http://0.0.0.0:5000/alg/list")
                .then(res => { this.$data.algorithms = res.data; });
        }
  },
	created: function() {
			this.getAlgorithm();
	},
}
</script>

<style>
@media (max-width: 480px) {
    .side-closed {
        display: none;
    }

    .side-open {
        position: fixed;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .side-option {
        color: white;
        font-size: 2em;
        margin: 20px;
        opacity: 1;
    }

    .side-option-effect {
        opacity: 1;
        transition: 0.25s;
        transition-duration: 1s;
        transition-delay: 1s;
        transition-timing-function: ease-out;
    }
}
</style>