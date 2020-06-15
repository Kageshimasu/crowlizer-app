import { Module } from 'vuex'
import { ProjectState, RootState } from '@/store/types'
import getters from './getters'
import actions from './actions'
import mutations from './mutations'
import ProjectDto from '@/domain/dto/projectDto'
import TabDto from '@/domain/dto/tabDto'

const state: ProjectState = {
  projectDto: new ProjectDto(),
  tabDto: new TabDto()
}

export const project: Module<ProjectState, RootState> = {
  state,
  getters,
  actions,
  mutations
}
