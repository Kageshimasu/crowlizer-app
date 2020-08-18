<template>
  <div>
    <v-card color="light-grey-background" elevation="0">
      <v-tabs
        v-model="currentRoute"
        background-color="transparent"
        color="#c52b2d"
        grow
      >
        <v-tab
          v-for="tab of tabs"
          class="red-text"
          :key="tab.id"
          :to="tab.route"
          @click="onTabPressed"
          :disabled="disabled"
        >
          {{tab.name}}
        </v-tab>
        <v-tab-item
          class="light-grey-background"
          v-for="tab of tabs"
          :key="tab.id"
          :value="tab.route"
        >
          <router-view></router-view>
        </v-tab-item>
      </v-tabs>
    </v-card>
  </div>
</template>

<script lang='ts'>
import { Component, Prop, Vue } from 'vue-property-decorator'

@Component
export default class ProjectEditor extends Vue {
  @Prop()
  tabs!: [{id: string; name: string; route: string}];

  @Prop({ default: '' })
  currentId!: string;

  @Prop({ default: false })
  disabled?: boolean;

  private getRouteFromId (id: string): string {
    for (let i = 0; i < this.tabs.length; i++) {
      if (this.tabs[i].id === id) {
        return this.tabs[i].route
      }
    }
    return this.tabs[0].route
  }

  private getIdFromRoute (route: string): string {
    return this.tabs.filter(v => v.route === route)[0].id
  }

  private onTabPressed () {
    this.$emit('onTabPressed', this.getIdFromRoute(this.$route.path))
  }

  currentRoute = this.getRouteFromId(this.currentId)
}
</script>

<style>
@import "../../css/main-styles.css";

.f-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.v-application{
    font-family: "M Plus 1p" !important;
}
</style>
