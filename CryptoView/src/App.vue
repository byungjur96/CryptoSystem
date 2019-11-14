<template>
  <div>
    <SideMenu v-if="openSide"></SideMenu>
    <NavHeader v-on:is-side-opened="menuClickEvent"></NavHeader>
    <Contents></Contents>
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
      isSideOpened: false
    }
  },
  components: {
    NavHeader, SideMenu, Contents
  },
  methods: {
    menuClickEvent: function() {
      this.$data.isSideOpened = !this.$data.isSideOpened;
    }
  },
  computed: {
    openSide: function() {
      return this.$data.isSideOpened;
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