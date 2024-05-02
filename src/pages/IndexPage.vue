<template>
  <q-page class="flex flex-center">
    <div class="flex flex-center flex-direction-column">
      <div class="title-container">
        <h1>synthWave- </h1>
        <h1 class="secondary-color"> 001</h1>
      </div>
      <q-btn outline color="secondary" label="START" @click="handleClick" size="lg" />
    </div>
    <div class="progress-container">
      <q-linear-progress dark rounded indeterminate color="secondary" />
      <q-linear-progress dark query color="primary" />
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'IndexPage',
  setup() {
    const router = useRouter();

    const handleClick = () => {
      router.push('/start');
    };

    return {
      handleClick,
    };
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
</style>
