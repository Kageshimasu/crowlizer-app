<template>
    <v-stepper :value="activeStepOrder" class="elevation-0">
      <v-stepper-header class="light-grey-background">
        <template
          v-for="step in steps"
        >
          <v-stepper-step
            color="red-background"
            :key="step.id"
            :step="step.stepOrder"
            :complete="step.complete"
            >
            {{step.name}}
          </v-stepper-step>
          <v-divider :key="step.id + 'divider'" v-if="step.id < getLastId()"></v-divider>
        </template>
      </v-stepper-header>
  </v-stepper>
</template>

<script lang='ts'>
import { Component, Prop, Vue } from 'vue-property-decorator'

@Component
export default class Stepper extends Vue {
  @Prop()
  steps!: {id: string; stepOrder: number; name: string; complete: boolean}[];

  @Prop()
  activeStepOrder!: number;

  private getLastId () {
    return this.steps.slice(-1)[0].id
  }
}
</script>

<style>
@import "../../css/main-styles.css";
</style>
