<template>
  <div class="tab-item flex-center-container">
    <div>
      <h1 class="display-2 mb-3 text-center">募集方式</h1>
      <p class="subheading font-weight-regular text-center">
        募集する方式を教えてください<br><br>
        All-In方式：集まった分の支援金を受け取られる方式<br>
        All-or-Nothing方式：目標金額を達成した場合のみ支援金を受け取れる方式
      </p>
      <div class="flex-center-container">
        <v-btn
          class="ma-2"
          color="teal"
          min-width="170"
          :outlined="!isSelectedallOrNothing"
          @click="pressedAllOrNothing"
          dark
          >
          All-or-Nothing
          </v-btn>
        <v-btn
          class="ma-2"
          color="teal"
          min-width="170"
          :outlined="isSelectedallOrNothing"
          @click="pressedAllIn"
          dark
          >
          All-In
          </v-btn>
        </div>
      </div>
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator'
import ProjectConst from '@/domain/const/projectConst'

@Component
export default class Methods extends Vue {
  isSelectedallOrNothing = true

  private pressedAllOrNothing () {
    if (!this.isSelectedallOrNothing) {
      this.$store.commit('setMethod', ProjectConst.allOrNothing)
      this.isSelectedallOrNothing = true
    }
  }

  private pressedAllIn () {
    if (this.isSelectedallOrNothing) {
      this.$store.commit('setMethod', ProjectConst.allIn)
      this.isSelectedallOrNothing = false
    }
  }

  mounted () {
    if (this.$store.getters.method === ProjectConst.allOrNothing) {
      this.$store.commit('setMethod', ProjectConst.allOrNothing)
      this.isSelectedallOrNothing = true
    } else if (this.$store.getters.method === ProjectConst.allIn) {
      this.$store.commit('setMethod', ProjectConst.allIn)
      this.isSelectedallOrNothing = false
    } else {
      // TODO: 登録されている以外のメソッドが参照された場合のエラー処理
      throw Error(this.$store.getters.method)
    }
  }
}
</script>

<style>
@import "../../css/main-styles.css";
</style>
