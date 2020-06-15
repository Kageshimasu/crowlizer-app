<template>
  <div class="tab-item flex-center-container">
    <div class="target-amount-form">
      <div class="title-margin">
        <h1 class="display-2 mb-3 text-center">カテゴリー</h1>
        <p class="subheading font-weight-regular text-center">
          プロジェクトのカテゴリーを教えてください
        </p>
      </div>
      <div>
        <v-select
          v-model="item"
          color="teal"
          height="3vh"
          label="選択してください"
          :items="items"
          @input="selectedItem"
          dense
        ></v-select>
      </div>
      </div>
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class Category extends Vue {
  item = this.$store.getters.category
  alert = false
  items = [
    'アート', '音楽', '開発', 'フード', 'ファッション', '書籍', 'アニメ・漫画',
    'スポーツ', '映像', 'テクノロジー', 'ビジネス', '地域活性化']

  private isCategoryInvalid () {
    return (this.$store.getters.category === '')
  }

  private lockIfCategoryInvalid () {
    this.$store.commit('setLockedStep', this.isCategoryInvalid())
  }

  private selectedItem (input: string) {
    this.$store.commit('setCategory', input)
    this.lockIfCategoryInvalid()
  }

  mounted () {
    this.lockIfCategoryInvalid()
  }
}
</script>

<style>
@import "../../main-styles.css";

.title-margin {
  margin-bottom: 50px
}
</style>
