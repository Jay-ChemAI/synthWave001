<template>
  <q-page class="flex flex-center flex-direction-column full-height">
    <div>
      <h2> ABOUT </h2> <br>
    </div>
    <div>
      This page is about the Δ-Tsuru experience <br>
      All the content here is made by Javier De Santiago
    </div><br>
    <div class="flex-grow flex flex-center">
    <q-btn outline color="secondary" label="Contact me" @click="handleClick" size="md" />
    </div>
    <div class="flex-grow">
      <!-- This div will grow to take up all available space, pushing the following content down -->
    </div>
    <div class="bottom-content">
      All rights reserved
      2024 <br>
    </div>
    <div class="progress-container">
      <q-linear-progress dark rounded indeterminate color="secondary" />
      <q-linear-progress dark query color="primary" />
    </div>
  </q-page>
</template>
<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'IndexPage',
  methods: {
    handleClick() {
      console.log('Button clicked');
      window.location.href = 'mailto:javierlx12@hotmail.com';
    },
  },
});
</script>

<style scoped>
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
.flex-direction-column {
  flex-direction: column;
  justify-content: flex-start;
}
.full-height {
  height: 100vh; /* Make the container take up the full viewport height */
}

.flex-grow {
  flex-grow: 1; /* Make this div take up all available space */
}

.bottom-content {
  margin-bottom: 20px; /* Add a margin at the bottom */
}
</style>
