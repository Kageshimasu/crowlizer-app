<template>
  <div class=".flex-center-container">
    <div>
      <v-progress-circular
        :size="70"
        :width="7"
        color="#c52b2d"
        :indeterminate="indeterminate"
      ></v-progress-circular>
    </div>
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator'
import axios from 'axios'
import ProjectDto from '@/domain/dto/projectDto'

@Component
export default class Result extends Vue {
  indeterminate = true

  mounted () {
    axios.put(
      '/crowlizer/api/inference/',
      this.$store.getters.projectObject
    ).then((response) => {
      console.log('scceeded')
      console.log(response)
    }).catch((error: Error) => {
      console.log('failed')
      console.log(error)
    }).finally(() => {
      this.indeterminate = false
    })
  }
}
</script>

<style>
@import "../../main-styles.css";
</style>
