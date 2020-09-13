import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost/'
axios.defaults.headers.post['Content-Type'] = 'application/json;charset=utf-8'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
