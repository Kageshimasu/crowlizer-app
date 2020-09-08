<template>
  <div class="home-form flex-center-container">
    <div>
      <h1 class="display-2 font-weight-bold mb-3 text-center">
        Welcome to {{title}}
      </h1>
      <p class="subheading font-weight-regular text-center">
        Crowlizer is a web application which predicts your project's future<br>
        Click the button below to try this.
      </p>
      <p class="flex-center-container">
        <router-link to="/form/date" class="btn btn-default btn-xl">ANALYZE</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import { Component, Vue } from 'vue-property-decorator'
import config from '@/../vue.config'

@Component
export default class Home extends Vue {
  title = config.pages.index.title;
}

</script>

<style>
@import "../../css/main-styles.css";
@import "../../css/animation-styles.css";

.home-form {
  width: 100%;
  height: 100%;
}

button {
  color: #353a43;
  background-color: #eee;
  padding: 0.3em 0.8em;
  border: 0;
  border-radius: 3px;
  font-size: 0.95em;
  cursor: pointer;
  box-shadow: 0px 2px 2px 0px rgba(0, 0, 0, 0.16), 0px 1px 5px 0px rgba(0, 0, 0, 0.2);
  border-bottom: solid 1px #353a43;
  transition: all ease .3s;
}

button:hover,
button:active {
  color: #486b93;
  background-color: #fff;
}
</style>
