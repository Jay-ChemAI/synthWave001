<template>
  <div>
    <h2 class="text-center"> Δ-Tsuru RPA  </h2>
    <div class="q-pa-md row items-start q-gutter-md">
      <q-card
        v-for="bot in bots"
        :key="bot.name"
        class="my-card"
        flat
        bordered
      >
        <q-card-section>
          <div class="text-h6">{{ bot.name }}</div>
          <div>{{ bot.description }}</div>
        </q-card-section>

        <q-card-section>
          <q-btn
            color="primary"
            label="Run"
            @click="runBot(bot)"
          />
        </q-card-section>
      </q-card>
    </div>
    <div class="progress-container">
      <q-linear-progress dark rounded indeterminate color="secondary" />
      <q-linear-progress dark query color="primary" />
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'IndexPage',
  data() {
    return {
      bots: [
        { name: 'Bot 1', description: 'This is bot 1' },
        { name: 'Bot 2', description: 'This is bot 2' },
        { name: 'Bot 2', description: 'This is bot 2' },
        { name: 'Bot 3', description: 'This is bot 3' },
        { name: 'Bot 4', description: 'This is bot 4' },
        { name: 'Bot 5', description: 'This is bot 5' },
        { name: 'Bot 6', description: 'This is bot 6' },
        { name: 'Bot 7', description: 'This is bot 7' },
        { name: 'Bot 8', description: 'This is bot 8' },
        { name: 'Bot 9', description: 'This is bot 9' },
        { name: 'Bot 10', description: 'This is bot 10' },
        { name: 'Bot 11', description: 'This is bot 11' },
        // Add more bots here
      ],
    };
  },
  methods: {
    runBot(bot) {
      console.log(`Running ${bot.name}`);

      // Add code to run the bot here
    },
  },
});
</script>

<style scoped>
.my-card {
  width: 300px;
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
