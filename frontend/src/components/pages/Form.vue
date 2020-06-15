<template>
  <div>
    <div>
      <div class="flex-center-container">
        <v-card-title class="text-center py-6">
          <h1 class="font-weight-bold headline red-text">Crowlier ver 1.0.0</h1>
        </v-card-title>
      </div>
        <Stepper
          :steps="steps"
          :activeStepOrder="activeStepOrder"
        />
      <DynamicTab
        :tabs="currentTabs"
        :currentId="currentId"
        :disabled="this.$store.getters.isLockedStep"
        @onTabPressed="changeCurrentId"
      />
    </div>
    <div class="flex-center-container">
      <v-btn
        class="ma-2"
        tile
        outlined
        @click="reset"
        :to="defaultTab.route"
      >
        リセットする
      </v-btn>
      <v-btn
        class="ma-2 white--text"
        tile
        color="red-background"
        @click="appendTab"
        :to="getNextRoute()"
        :disabled="this.$store.getters.isLockedStep"
      >
        {{getNextButtonName()}}に進む
      </v-btn>
    </div>
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator'
import DynamicTab from '@/components/templates/DynamicTab.vue'
import Stepper from '@/components/molecules/Stepper.vue'
import ProbabilityPredictionService from '@/domain/probabilityPredictionService'

@Component({
  components: {
    DynamicTab,
    Stepper
  }
})
export default class Form extends Vue {
  tabsJpn = [
    { id: '0', name: '日付' },
    { id: '1', name: '目標' },
    { id: '2', name: '募集方式' },
    { id: '3', name: 'カテゴリ' },
    { id: '4', name: '概要' },
    { id: '5', name: 'ビジュアル' },
    { id: '6', name: 'SNS' }
  ]

  tabs = [
    { id: '0', name: 'DATE', route: '/form/date' },
    { id: '1', name: 'GOAL', route: '/form/goal' },
    { id: '2', name: 'METHODS', route: '/form/methods' },
    { id: '3', name: 'CATEGORY', route: '/form/category' },
    { id: '4', name: 'DESCRIPTION', route: '/form/description' },
    { id: '5', name: 'VISUALIZATION', route: '/form/visualization' },
    { id: '6', name: 'SNS', route: '/form/sns' }
  ]

  lastPage = { name: '分析', route: '/' }

  defaultTab = this.tabs[0]
  currentId = this.defaultTab.id
  currentTabs = [this.defaultTab]
  isDisabledMovement = false
  steps = this.initStepsFromTabs(this.tabs)
  activeStepOrder = this.steps[0].stepOrder
  probPredService = ProbabilityPredictionService.instance

  private initStepsFromTabs (
    tabs: {id: string; name: string; route: string}[]) {
    const steps = []
    for (let i = 0; i < tabs.length; i++) {
      steps.push({ id: tabs[i].id, stepOrder: i + 1, name: tabs[i].name, complete: false })
    }
    return steps
  }

  private reset () {
    this.currentTabs = [this.defaultTab]
    this.currentId = this.defaultTab.id
    this.updateSteps()
  }

  private changeCurrentId (idToChange: string) {
    this.currentId = idToChange
  }

  private appendTab () {
    if (this.nextPageExists()) {
      const maxIndex = this.currentTabs.length - 1
      if (this.currentId === this.tabs[maxIndex].id) {
        this.currentTabs.push(this.tabs[maxIndex + 1])
      }
      this.currentId = this.getNextId()
      this.updateSteps()
    } else {
      this.reset()
    }
  }

  private nextPageExists () {
    for (let i = 0; i < this.tabs.length - 1; i++) {
      if (this.tabs[i].id === this.currentId) {
        return true
      }
    }
    return false
  }

  private getNextRoute (): string {
    if (this.nextPageExists()) {
      const nextId = this.getNextId()
      return this.tabs.filter(v => v.id === nextId)[0].route
    }
    this.probPredService.predictProbability(this.$store.getters.projectObject)
    return this.lastPage.route
  }

  private getNextButtonName (): string {
    if (this.nextPageExists()) {
      const nextId = this.getNextId()
      return this.tabsJpn.filter(v => v.id === nextId)[0].name
    }
    return this.lastPage.name
  }

  private getNextId (): string {
    for (let i = 0; i < this.tabs.length - 1; i++) {
      if (this.tabs[i].id === this.currentId) {
        return this.tabs[i + 1].id
      }
    }
    return this.tabs[0].id
  }

  private updateSteps () {
    this.steps = this.steps.map((v) => {
      for (let i = 0; i < this.currentTabs.length - 1; i++) {
        if (this.currentTabs[i].id === v.id) {
          v.complete = true
          this.activeStepOrder = v.stepOrder + 1
          return v
        }
      }
      v.complete = false
      return v
    })
    if (!this.steps[0].complete) {
      this.activeStepOrder = this.steps[0].stepOrder
    }
  }

  private updateMovement () {
    this.isDisabledMovement = this.$store.getters.targetAmount === 0
  }

  mounted () {
    // Defaultタブに直す
    if (this.$route.path !== this.defaultTab.route) {
      this.$router.push({ path: this.defaultTab.route })
    }
    this.reset()
  }
}
</script>

<style>
@import "../../main-styles.css";
</style>
