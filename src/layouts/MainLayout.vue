<template>
  <q-layout view="lHh Lpr lFf" class="background-image">
    <q-header elevated>
      <q-toolbar class="toolbar-background">
        <q-btn
          flat
          dense
          round
          aria-label="Menu"
          icon="menu"
          @click="toggleLeftDrawer"
        >
          <img class="menu-icon"/>
        </q-btn>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >

      <q-list>
        <q-item-label
          header
        >
          Essential Links
        </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />

      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>

</template>

<script>
import { defineComponent, ref } from 'vue';
import EssentialLink from 'components/EssentialLink.vue';

const linksList = [
  {
    title: 'Start',
    caption: 'Start your journey',
    icon: 'school',
    link: '/#/',
  },
  {
    title: 'Bots',
    caption: 'Bots for your server',
    icon: 'code',
    link: '/#/bots',
  },

  {
    title: 'About',
    caption: 'Contact me',
    icon: 'favorite',
    link: '/#/about',
  },
];

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
  },

  setup() {
    const leftDrawerOpen = ref(false);

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
      progress1: 0.4,
      progress2: 0.62,
    };
  },
});
</script>

<style scoped>
.background-image {
  position: relative;
}

.background-image::before {
  content: "";
  background-image: url('space.jpg');
  background-size: 10%; /* Ajusta este valor para cambiar el tamaño de la imagen */
  background-repeat: repeat; /* Cambia a 'repeat' para repetir la imagen como un mosaico */
  opacity: 0.8; /* 1 es completamente opaco, 0 es completamente transparente */
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: -1;
}
.toolbar-background {
  background-image: url('wabes.gif');
  background-size: cover;
  background-repeat: no-repeat;
  opacity: 0.9;
  box-shadow: none !important;
  height: 60px; /* Ajusta este valor para cambiar la altura de la toolbar */

}

</style>
