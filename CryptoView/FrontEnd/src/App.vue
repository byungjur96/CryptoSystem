<template>
  <div>
    <SideMenu 
      v-if="openSide"
      v-on:makeEncrypt="changeEncrypt"
      v-on:makeDecrypt="changeDecrypt">
    </SideMenu>
    <NavHeader 
      v-bind:is-side-opened="openSide"
      v-on:changeMenuBtn="menuClickEvent">
    </NavHeader>
    <Contents v-bind:mode="changeMode"></Contents>
  </div>
</template>

<script>
import NavHeader from './components/header.vue';
import SideMenu from './components/side-menu.vue';
import Contents from './components/contents.vue';

export default {
  name: 'app',
  data: function() {
    return {
      isSideOpened: false,
      mode: "Encrypt"
    }
  },
  components: {
    NavHeader, SideMenu, Contents
  },
  methods: {
    menuClickEvent: function() {
      this.$data.isSideOpened = !this.$data.isSideOpened;
    },
    changeEncrypt: function() {
      this.$data.isSideOpened = !this.$data.isSideOpened;
      this.$data.mode = "Encrypt";
    },
    changeDecrypt: function() {
      this.$data.isSideOpened = !this.$data.isSideOpened;
      this.$data.mode = "Decrypt";
    }
  },
  computed: {
    openSide: function() {
      return this.$data.isSideOpened;
    },
    changeMode: function() {
      return this.$data.mode;
    }
  }
}
</script>

<style>
@media (max-width: 480px) {
 #side-menu {
    width: 100vw;
    height: 100vh;
    opacity: 0.8;
    background-color: black;
    z-index: 999;
  } 
}
</style>