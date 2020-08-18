<template>
  <div>
    <div class="absolute-alert">
      <v-alert type="error" :value="alert">終了日には開始日以降の日付を指定して下さい。</v-alert>
    </div>
    <div class="tab-item flex-center-container">
      <div class="target-amount-form">
        <h1 class="display-2 mb-3 text-center">期間</h1>
        <p class="subheading font-weight-regular text-center">
          プロジェクトの期間を教えてください
        </p>
          <div class="flex-center-container">

            <div class="ma-2">
              <v-menu
                v-model="menuStartDate"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="290px"
              >
                <template v-slot:activator="{ on }">
                  <v-text-field
                    v-model="startDate"
                    color="teal"
                    label="Start at"
                    readonly
                    v-on="on"
                    :error="alert"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="startDate" color="teal" @input="setStartDate"></v-date-picker>
              </v-menu>
            </div>

            <div class="ma-2">
              <v-menu
                v-model="menuEndDate"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="290px"
              >
                <template v-slot:activator="{ on }">
                  <v-text-field
                    v-model="endDate"
                    color="teal"
                    label="End at"
                    readonly
                    v-on="on"
                    :error="alert"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="endDate" color="teal" @input="setEndDate"></v-date-picker>
              </v-menu>
            </div>

          </div>
        </div>
    </div>
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class Date extends Vue {
  startDate = this.$store.getters.startDate
  endDate = this.$store.getters.endDate
  menuStartDate = false
  menuEndDate = false
  alert = false

  private isStartDateGreaterThanEndDate () {
    return this.$store.getters.startDate >= this.$store.getters.endDate
  }

  private lockIfInputInvalid () {
    this.$store.commit('setLockedStep', this.isStartDateGreaterThanEndDate())
  }

  private alertIfInputInvalid () {
    this.alert = this.isStartDateGreaterThanEndDate()
  }

  private setStartDate () {
    this.menuStartDate = false
    this.$store.commit('setStartDate', this.startDate)
    this.alertIfInputInvalid()
    this.lockIfInputInvalid()
  }

  private setEndDate () {
    this.menuEndDate = false
    this.$store.commit('setEndDate', this.endDate)
    this.alertIfInputInvalid()
    this.lockIfInputInvalid()
  }

  mounted () {
    this.lockIfInputInvalid()
  }
}
</script>

<style>
@import "../../css/main-styles.css";

.target-amount-form {
  width: 600px
}
</style>
