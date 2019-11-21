<template>
    <div id="contents">
        <!-- <Encrypt></Encrypt> -->
        <Decrypt></Decrypt>
    </div>
</template>

<script>
import Encrypt from './contents/Encrypt';
import Decrypt from './contents/Decrypt';

export default {
  name: 'contents',
  components: {
      Encrypt, Decrypt
  }
}
</script>

<style>
@media (max-width: 480px) {
    #contents {
        width: 100%;
        height: 100%;
    }
}
</style>