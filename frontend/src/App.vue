<template>
  <v-app class="light-grey-background">
    <!-- <v-app-bar
      app
      color="grey-header"
      elevation="1"
      dark
    >
      <v-spacer />
      <div class="center display-2 light-rey-text text-center">
        Krowlizer
      </div>
      <div class="bottom">
        <v-btn
          href="https://github.com/vuetifyjs/vuetify/releases/latest"
          target="_blank"
          text
        >
          <div class="light-rey-text">ver 1.0.0</div>
          <v-icon class="light-rey-text">mdi-open-in-new</v-icon>
        </v-btn>
      </div>
    </v-app-bar> -->
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class App extends Vue {
  name = 'App';
}
</script>

<style>
@import "/css/main-styles.css";

.center{
  margin-left: auto;
  margin-right: auto;
}
</style>
