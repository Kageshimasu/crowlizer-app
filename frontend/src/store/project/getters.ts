import { GetterTree } from 'vuex'
import { ProjectState, RootState } from '@/store/types'

const getters: GetterTree<ProjectState, RootState> = {
  projectObject: (state: ProjectState) => {
    return state.projectDto
  },
  isLockedStep: (state: ProjectState) => {
    return state.tabDto.isLockedStep
  },
  startDate: (state: ProjectState) => {
    return state.projectDto.startDate
  },
  endDate: (state: ProjectState) => {
    return state.projectDto.endDate
  },
  targetAmount: (state: ProjectState) => {
    return state.projectDto.targetAmount
  },
  method: (state: ProjectState) => {
    return state.projectDto.method
  },
  category: (state: ProjectState) => {
    return state.projectDto.category
  },
  title: (state: ProjectState) => {
    return state.projectDto.title
  },
  description: (state: ProjectState) => {
    return state.projectDto.description
  },
  numImages: (state: ProjectState) => {
    return state.projectDto.numImages
  },
  numVideos: (state: ProjectState) => {
    return state.projectDto.numVideos
  },
  twitterExistence: (state: ProjectState) => {
    return state.projectDto.twitterExistence
  },
  twitterFriends: (state: ProjectState) => {
    return state.projectDto.twitterFriends
  },
  twitterFollowers: (state: ProjectState) => {
    return state.projectDto.twitterFollowers
  },
  facebookExistence: (state: ProjectState) => {
    return state.projectDto.facebookExistence
  },
  instagramExistence: (state: ProjectState) => {
    return state.projectDto.instagramExistence
  },
  webpageExistence: (state: ProjectState) => {
    return state.projectDto.webpageExistence
  }
}

export default getters
