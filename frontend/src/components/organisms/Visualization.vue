<template>
  <div class="tab-item flex-center-container">
    <div class="visualization-form">
      <h1 class="display-2 mb-3 text-center">ビジュアル</h1>
      <p class="subheading font-weight-regular text-center">
        アップロードする画像枚数と動画数を教えてください
      </p>
        <div>
          <v-text-field
            type="number"
            color="teal"
            label="画像枚数:"
            v-model="numImages"
            @input="setNumImages"
            @keypress="preventTypingExceptNumber"
          ></v-text-field>
          <v-text-field
            type="number"
            color="teal"
            label="動画数:"
            v-model="numVideos"
            @input="setNumVideos"
            @keypress="preventTypingExceptNumber"
          ></v-text-field>
        </div>
      </div>
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator'
import { preventTypingExceptNumber } from '@/infra/text_field_utils'

@Component({
  methods: {
    preventTypingExceptNumber
  }
})
export default class Visualization extends Vue {
  numImages = this.$store.getters.numImages === 0 ? '' : this.$store.getters.numImages
  numVideos = this.$store.getters.numVideos === 0 ? '' : this.$store.getters.numVideos

  private setNumImages () {
    this.$store.commit('setNumImages', this.numImages)
  }

  private setNumVideos () {
    this.$store.commit('setNumVideos', this.numVideos)
  }
}
</script>

<style>
@import "../../main-styles.css";

.visualization-form {
  width: 400px
}
</style>
