<template>
  <div class="tab-item flex-center-container">
    <div class="sns-form">
      <h1 class="display-2 mb-3 text-center">SNS</h1>
      <p class="subheading font-weight-regular text-center">
        あなたの活動を教えてください
      </p>
        <div>
          <v-row justify="space-between">
            <v-checkbox v-model="twitterBox" :label="`Twitter`" @change="updateTwitterExistence"></v-checkbox>
            <v-checkbox v-model="facebookBox" :label="`Facebook`" @change="updateFacebookExistence"></v-checkbox>
            <v-checkbox v-model="instagramBox" :label="`Instagram`" @change="updateInstagramExistence"></v-checkbox>
            <v-checkbox v-model="webpageBox" :label="`WebPage`" @change="updateWebpageExistence"></v-checkbox>
          </v-row>
        </div>
        <transition-group name="fade">
              <v-text-field
                key="friends"
                v-if="twitterBox"
                v-model="twitterFriends"
                label="Twitterのフォロー数"
                type="number"
                min="1"
                color="teal"
                height="3vh"
                :error="alertFriends"
                @keypress="preventTypingExceptNumber"
                @input="setTwitterFriends"
                single-line
              />
              <v-text-field
                key="followers"
                v-if="twitterBox"
                v-model="twitterFollowers"
                label="Twitterのフォロワー数"
                type="number"
                min="1"
                color="teal"
                height="3vh"
                :error="alertFollowers"
                @keypress="preventTypingExceptNumber"
                @input="setTwitterFollowers"
                single-line
              />
          </transition-group>
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
export default class Sns extends Vue {
  twitterBox = this.$store.getters.twitterExistence
  facebookBox = this.$store.getters.facebookExistence
  instagramBox = this.$store.getters.instagramExistence
  webpageBox = this.$store.getters.webpageExistence
  twitterFriends = this.$store.getters.twitterFriends === 0 ? '' : this.$store.getters.twitterFriends
  twitterFollowers = this.$store.getters.twitterFollowers === 0 ? '' : this.$store.getters.twitterFollowers
  alertFriends = false
  alertFollowers = false

  private updateTwitterExistence () {
    if (!this.twitterBox) {
      this.twitterFriends = ''
      this.twitterFollowers = ''
      this.$store.commit('setTwitterFriends', 0)
      this.$store.commit('setTwitterFollowers', 0)
    }
    this.$store.commit('setTwitterExistence', this.twitterBox)
    this.lockIfTwitterDetailsInvalid()
  }

  private updateFacebookExistence () {
    this.$store.commit('setFacebookExistence', this.facebookBox)
  }

  private updateInstagramExistence () {
    this.$store.commit('setInstagramExistence', this.instagramBox)
  }

  private updateWebpageExistence () {
    this.$store.commit('setWebpageExistence', this.webpageBox)
  }

  private setTwitterFriends () {
    this.alertFriends = (this.twitterFriends === '')
    this.$store.commit('setTwitterFriends', this.twitterFriends)
    this.lockIfTwitterDetailsInvalid()
  }

  private setTwitterFollowers () {
    this.alertFollowers = (this.twitterFollowers === '')
    this.$store.commit('setTwitterFollowers', this.twitterFollowers)
    this.lockIfTwitterDetailsInvalid()
  }

  private lockIfTwitterDetailsInvalid () {
    this.$store.commit(
      'setLockedStep',
      ((this.twitterFriends === '') || (this.twitterFollowers === '')) && this.twitterBox
    )
  }

  mounted () {
    this.lockIfTwitterDetailsInvalid()
  }
}
</script>

<style>
@import "../../main-styles.css";

.sns-form {
  height: 200px;
  width: 450px;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
