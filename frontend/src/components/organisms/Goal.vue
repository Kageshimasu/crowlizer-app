<template>
  <div>
    <div class="absolute-alert">
      <v-alert type="error" :value="alert">金額を入力してください。</v-alert>
    </div>
    <div class="tab-item flex-center-container">
      <div class="target-amount-form">
        <h1 class="display-2 mb-3 text-center">目標金額</h1>
        <p class="subheading font-weight-regular text-center">
          目標とする金額を教えてください
        </p>
          <div>
            <v-text-field
              type="number"
              min="1"
              color="teal"
              height="3vh"
              v-model="targetAmount"
              :error="alert"
              @keypress="preventTypingExceptNumber"
              @input="setTargetAmount"
              label="例: 198000(円)"
              single-line
              />
          </div>
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
export default class Goal extends Vue {
  targetAmount = this.$store.getters.targetAmount === 0 ? '' : this.$store.getters.targetAmount
  alert = false

  private isTargetAmountInvalid () {
    return (this.targetAmount === '') || (this.targetAmount === '0')
  }

  private lockIfTargetAmountInvalid () {
    this.$store.commit('setLockedStep', this.isTargetAmountInvalid())
  }

  private alertIfTargetAmountInvalid () {
    this.alert = this.isTargetAmountInvalid()
  }

  private setTargetAmount () {
    this.lockIfTargetAmountInvalid()
    this.alertIfTargetAmountInvalid()
    this.$store.commit('setTargetAmount', this.targetAmount)
  }

  mounted () {
    this.lockIfTargetAmountInvalid()
  }
}
</script>

<style>
@import "../../main-styles.css";

.target-amount-form {
  width: 400px
}
</style>
