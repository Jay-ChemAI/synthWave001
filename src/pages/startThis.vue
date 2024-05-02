<template>
  <div class="title-container">
    <h2> Welcome to the Δ-Tsuru experience  </h2>
  </div>
  <div class="progress-container">
    <q-linear-progress dark rounded indeterminate color="secondary" />
    <q-linear-progress dark query color="primary" />
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'IndexPage',
  methods: {
    handleClick() {
      console.log('Button clicked');
    },
  },
});
</script>

<style scoped>
.title-container {
  display: flex;
  justify-content: center;
  height: 100vh;
}

.flex-direction-column {
  flex-direction: column;
}

.secondary-color {
  color: #168c80;
}

.title-container {
  display: flex;
}
.progress-container {
  position: fixed;
  bottom: 0;
  width: 100%;
}
</style>
