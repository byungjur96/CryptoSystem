<template>
  <div>
  <Modal v-if="openModal"></Modal>
    <SideMenu 
      v-if="openSide"
      v-on:menuSelect="menuClickEvent">
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
import Modal from './components/keygen';

export default {
  name: 'app',
  data: function() {
    return {
      isSideOpened: false,
      mode: "dec"
    }
  },
  components: {
    NavHeader, SideMenu, Contents, Modal
  },
  methods: {
    menuClickEvent: function() {
      this.$data.isSideOpened = !this.$data.isSideOpened;
    }
  },
  computed: {
    openSide: function() {
      return this.$data.isSideOpened;
    },
    changeMode: function() {
      return this.$data.mode;
    },
    openModal: function() {
      return this.$store.state.open_keygen_modal;
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
#modal {
  position:fixed;
  width: 100vw;
  height: 100vh;
}
}
</style>