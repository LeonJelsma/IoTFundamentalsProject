<template>
  <div id="app">
    <DashboardView></DashboardView>
  </div>
</template>

<script>
import DashboardView from "@/views/DashboardView";

export default {
  name: 'App',
  components: {
    DashboardView,
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
  height: 100%;
}
</style>
