<template>
  <div class="result-form flex-center-container">
    <div>
      <transition-group name="fade" @after-leave="switchShowSuccessProb">

        <h1
        key='prob'
        class="display-2 mb-3 text-center"
        v-if="showSuccessProb"
        >
          The success probability of <font class="font-weight-bold">your project</font> would be<br><br>
          <font class="display-4 font-weight-bold red-text">
            {{(this.successProb * 100).toFixed(2)}}</font>%
        </h1>

        <v-progress-circular
          key="circular"
          :size="70"
          :width="7"
          color="#c52b2d"
          v-if="indeterminate"
          indeterminate
        ></v-progress-circular>
      </transition-group>
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
  showSuccessProb = false
  successProb = ''
  targetEst = ''
  scrollY = 0

  switchShowSuccessProb () {
    this.showSuccessProb = !this.showSuccessProb
  }

  calculateScrollY () {
    this.scrollY = window.scrollY
    console.log(this.calculateScrollY)
  }

  mounted () {
    window.addEventListener('scroll', this.calculateScrollY)
    axios.put(
      '/crowlizer/api/inference/',
      this.$store.getters.projectObject
    ).then((response) => {
      console.log('scceeded')
      console.log(response)
      this.successProb = response.data.predicted_success_prob
      this.targetEst = response.data.predicted_target_amount
    }).catch((error: Error) => {
      console.log('failed')
      console.log(error)
    }).finally(() => {
      this.indeterminate = false
    })
  }

  beforeDestroy () {
    window.removeEventListener('scroll', this.calculateScrollY)
  }
}
</script>

<style>
@import "../../main-styles.css";

.result-form {
  width: 100%;
  height: 100%;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.7s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
