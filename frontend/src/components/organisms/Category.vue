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
          item-value="id"
          item-text="name"
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
    { id: 1, name: 'アート' },
    { id: 2, name: '音楽' },
    { id: 3, name: '開発' },
    { id: 4, name: 'フード' },
    { id: 5, name: 'ファッション' },
    { id: 6, name: '書籍' },
    { id: 7, name: 'アニメ・漫画' },
    { id: 8, name: 'スポーツ' },
    { id: 9, name: '映像' },
    { id: 10, name: 'テクノロジー' },
    { id: 11, name: 'ビジネス' },
    { id: 12, name: '地域活性化' }
  ]

  private isCategoryInvalid () {
    return (this.$store.getters.category === 0)
  }

  private lockIfCategoryInvalid () {
    this.$store.commit('setLockedStep', this.isCategoryInvalid())
  }

  private selectedItem (input: number) {
    this.$store.commit('setCategory', input)
    this.lockIfCategoryInvalid()
  }

  mounted () {
    this.lockIfCategoryInvalid()
  }
}
</script>

<style>
@import "../../css/main-styles.css";

.title-margin {
  margin-bottom: 50px
}
</style>
