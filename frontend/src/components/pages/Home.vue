<template>
  <v-container>
    <v-row class="text-center">

      <v-col cols="12">
        <!-- <v-img
          :src="require('../../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        /> -->
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to {{title}}
        </h1>

        <p class="subheading font-weight-regular">
          Krowlizer is a web application to know how analyzers dissect<br>
          Your project.
          please click
          <router-link to="/form/goal">here</router-link>
          to try this
        </p>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
import { Component, Vue } from 'vue-property-decorator'
import config from '@/../vue.config'

@Component
export default class Home extends Vue {
  title = config.pages.index.title;
}
</script>
