<template>
    <div id="header">
        <div v-on:click="changeMenuBtn" id="menu">
            <div v-bind:class="sideBtnStyle"></div>
            <div v-bind:class="sideBtnStyle"></div>
        </div>
        <h2> {{ returnName }} </h2>
        <div id="info">I</div>
    </div>
</template>

<script>
export default {
    name: 'nav-header',
    data: function() {
        return {
            openSide: false
        }
    },
    props: ['isSideOpened'],
    methods: {
        changeMenuBtn: function() {
            this.$emit('changeMenuBtn');
        },
    },
    computed: {
        returnName: function() {
            return this.$store.state.algorithm;
        },
        tuneSide: function() {
            this.$data.openSide = this.$props.isSideOpened;
        },
        sideBtnStyle: function() {
            if (!this.$props.isSideOpened) { return {'side-menu-open':true }; }
            else { return {'side-menu-close':true }; }
        }
    }
}
</script>

<style>
@media (max-width: 480px) {
    #header {
        width: 100%;
        height: 50px;
        background-color: rgba(0,0,0,0.8);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
  
    #header > div {
        margin: 20px;
    }

    #header > h2 {
        color: white;
        font-size: 20px;
    }

    #menu {
        width: 20px;
        z-index: 1000;
        cursor: pointer;
    }

    .side-menu-open {
        width: 100%;
        height: 1px;
        background-color: white;
        margin-top: 6px;
        margin-bottom: 6px;
        border: 0;
        transition: 
            transform .3s cubic-bezier(0.04, 0.04, 0.12, 0.96),
            -webkit-transform .3s cubic-bezier(0.04, 0.04, 0.12, 0.96);
    }

    .side-menu-close {
        position: relative;
        width: 100%;
        height: 1px;
        border: 0;
        background-color: white;
        transition: 
            transform .35s cubic-bezier(0.04, 0.04, 0.12, 0.96),
            -webkit-transform .35s cubic-bezier(0.04, 0.04, 0.12, 0.96);
    }

    .side-menu-close:first-child {
        top: 0.5px;
        transform: rotate( 45deg );
    }

    .side-menu-close:last-child {
        bottom: 0.5px;
        transform: rotate( -45deg );
    }

    #info {
        cursor: pointer;
        color: white;
    }
}
</style>