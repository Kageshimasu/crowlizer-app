import Vue from 'vue'
import Vuex from 'vuex'
import { project } from './project'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    version: '1.0.0'
  },
  modules: {
    project
  }
})
