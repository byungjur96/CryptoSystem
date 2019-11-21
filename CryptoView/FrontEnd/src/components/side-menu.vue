<template>
    <div id="side-menu" class="side-open">
        <div href="" class="side-option">Encrypt</div>
        <div href="" class="side-option">Decrypt</div>
        <div href="" class="side-option">History</div>
    </div>
</template>

<script>
export default {
  name: 'side-bar'
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