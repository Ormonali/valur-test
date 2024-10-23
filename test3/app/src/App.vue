<template>
  <div id="app">
    <Calculate />
  </div>
</template>
<script>
import Calculate from './components/Calculate.vue'

export default {
  name: 'App',
  components: {
    Calculate
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
