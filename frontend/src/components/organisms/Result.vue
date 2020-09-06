<template>
  <div class="result-form result-flex-container">
    <slot v-if="!failedConnection">
      <slot v-if="!isVisibleTargetAmount">
        <div :class="{fadeOut: !isVisibleTargetAmount}">
          <transition-group class="result-form result-flex-container" name="fade" @after-leave="switchShowSuccessProb">
            <h1
            key='prob'
            class="result-text display-1 mb-3 text-center"
            v-if="showSuccessProb"
            style="flex-grow: 3;"
            >
              The success probability of your project would be<br><br>
              <font class="display-2 font-weight-bold red-text">
                {{(this.successProb * 100).toFixed(2)}}
              </font>%
            </h1>
            <v-progress-circular
              key="circular"
              :size="70"
              :width="7"
              color="#c52b2d"
              v-if="indeterminate"
              indeterminate
            ></v-progress-circular>
            <h2
            key="scroll-text"
            class="scroll-down-style mb-3 text-center"
            style="flex-grow: 3;"
            v-if="showSuccessProb"
            >
              <!-- Scroll Down to see your project's value -->
            </h2>
          </transition-group>
        </div>
      </slot>
      <slot v-if="isVisibleTargetAmount">
        <div :class="{fadeIn: isVisibleTargetAmount}">

            <h1
            key='prob'
            class="result-text display-1 mb-3 text-center"
            v-if="showSuccessProb"
            >
              I think your project would be worth <br><br>
              <font class="display-2 font-weight-bold red-text">
                {{targetEst}}</font> yen
            </h1>

            <v-progress-circular
              key="circular"
              :size="70"
              :width="7"
              color="#c52b2d"
              v-if="indeterminate"
              indeterminate
            ></v-progress-circular>
        </div>
      </slot>
    </slot>
    <slot v-if="failedConnection">
      <div class="flex-center-container">
        <h1
        class="result-text display-1 mb-3 text-center"
        >
        Sorry :( <br>
        <font class="display-1 font-weight-bold red-text">Failed</font> to Connect the server
        </h1>
      </div>
    </slot>
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator'
import axios from 'axios'
import ProjectDto from '@/domain/dto/projectDto'

@Component({})
export default class Result extends Vue {
  indeterminate = true
  showSuccessProb = false
  successProb = ''
  targetEst = ''
  scrollY = 0
  isVisibleTargetAmount = false
  enabledWhenUnloadConfirm = false
  failedConnection = false

  private switchShowSuccessProb () {
    this.showSuccessProb = true
  }

  private handleScroll () {
    if (window.scrollY > this.scrollY) {
      this.isVisibleTargetAmount = true
    } else {
      this.isVisibleTargetAmount = false
    }
    this.scrollY = window.scrollY
  }

  onBeforeunloadHandler (evt: BeforeUnloadEvent): void {
    evt.returnValue = '編集中の内容は失われます。'
  }

  mounted () {
    this.startOver()
    window.addEventListener('beforeunload', this.onBeforeunloadHandler, false)
    window.addEventListener('scroll', this.handleScroll)
    axios.put(
      '/crowlizer/api/inference/',
      this.$store.getters.projectObject
    ).then((response) => {
      console.log('scceeded')
      this.successProb = response.data.predicted_success_prob
      this.targetEst = response.data.predicted_target_amount
      this.targetEst = (Number(this.targetEst) > 0) ? Number(this.targetEst).toFixed(0) : '0'
      this.showSuccessProb = true
    }).catch((error: Error) => {
      console.log('failed')
      console.log(error)
      this.failedConnection = true
    }).finally(() => {
      this.indeterminate = false
    })
  }

  startOver () {
    const newProjectDto = new ProjectDto()
    if (this.$store.getters.projectObject.equals(newProjectDto)) {
      this.$router.push({ path: '/' })
    }
  }

  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
    window.removeEventListener('beforeunload', this.onBeforeunloadHandler, false)
  }
}
</script>

<style>
@import "../../css/main-styles.css";
@import "../../css/animation-styles.css";

.result-form {
  width: 100%;
  height: 101%;
}

.result-flex-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.result-text {
}

.scroll-down-style {
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.7s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

.fadeIn {
  animation: fadeIn 1s;
}
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0px);
  }
}

.fadeOut {
  animation: fadeOut 1s;
}
@keyframes fadeOut {
  0% {
    opacity: 0;
    transform: translateY(0px);
  }
  100% {
    opacity: 1;
    transform: translateY(10px);
  }
}
</style>
