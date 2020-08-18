<template>
  <div class="tab-item flex-center-container">
    <div class="description-form">
      <h1 class="display-2 mb-3 text-center">プロジェクト詳細</h1>
        <div>
          <v-text-field
            color="teal"
            label="表題:"
            v-model="title"
            @input="setTitle"
          ></v-text-field>
          <v-textarea
            color="teal"
            label="概要:"
            height="300"
            v-model="description"
            @input="setDescription"
            :no-resize="true"
            outlined
          >
          </v-textarea>
        </div>
      </div>
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class Description extends Vue {
  title = this.$store.getters.title
  description = this.$store.getters.description

  private setTitle () {
    this.$store.commit('setTitle', this.title)
  }

  private setDescription () {
    this.$store.commit('setDescription', this.description)
  }
}
</script>

<style>
@import "../../css/main-styles.css";

.description-form {
  width: 500px
}
</style>
