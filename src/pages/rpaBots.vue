<template>
  <div>
    <q-banner v-if="successMessage" class="success-banner">
      {{ successMessage }}
    </q-banner>
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
    <div class="row items-center full-width">
      <q-btn
        color="primary"
        label="Run"
        @click="runBot(bot)"
      />
      <div class="q-ml-md progress-bar-container">
        <q-linear-progress
          :indeterminate="bot.isLoading"
          class="progress-bar"
          style="flex-grow: 1;"
        />
      </div>
    </div>
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
        {
          name: 'CMS data provider bot',
          description: 'This bot downloads a data base with de CMS data',
          command: 'rcc run',
          cwd: 'bots/CMS_Provider_data',
          isLoading: false,
        },
        {
          name: 'Twitter tendences bot',
          description: 'This bot downloads the tendences of twitter in real time using json object format',
          command: 'rcc run',
          cwd: 'bots/twitterTendences',
          isLoading: false,
        },
        // ...
      ],
      successMessage: '',
    };
  },
  methods: {
    runBot(bot) {
      console.log(`Running ${bot.name}`);
      bot.isLoading = true;

      console.log(`Running in directory: ${bot.cwd}`); // Imprime el directorio del bot

      const eventSource = new EventSource(`http://localhost:3000/run-command?command=${encodeURIComponent(bot.command)}&cwd=${encodeURIComponent(bot.cwd)}`);

      eventSource.onmessage = (event) => {
        console.log(event.data);
        // Aquí puedes actualizar la barra de progreso basándote en los datos recibidos
      };

      eventSource.onerror = (error) => {
        console.error(`Error running bot: ${error}`);
        bot.isLoading = false;
      };

      eventSource.onclose = () => {
        bot.isLoading = false;
      };
      eventSource.addEventListener('bot-finished', () => {
        bot.isLoading = false;
        this.successMessage = `Bot ${bot.name} finished successfully!`;
        setTimeout(() => {
          this.successMessage = '';
        }, 5000); // the message will disappear after 5 seconds
        eventSource.close();
      });
    },
  },
});
</script>

<style scoped>
.my-card {
  width: 100%;
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
.progress-bar {
  height: 20px; /* Ajusta este valor a la altura que desees */
}
.full-width {
  width: 100%;
  display: flex;
  align-items: center;
}
.progress-bar-container {
  flex-grow: 1;
}
.success-banner {
  background-color: rgba(212, 237, 218, 0.8);
  color: #155724; /* Color de texto verde oscuro */
}
</style>
