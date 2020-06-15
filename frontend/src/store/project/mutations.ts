import { MutationTree } from 'vuex'
import { ProjectState } from '@/store/types'

const mutations: MutationTree<ProjectState> = {
  setLockedStep: (state, isLocked: boolean) => {
    state.tabDto.isLockedStep = isLocked
  },
  setStartDate: (state, startDate: string) => {
    state.projectDto.startDate = startDate
  },
  setEndDate: (state, endDate: string) => {
    state.projectDto.endDate = endDate
  },
  setTargetAmount: (state, targetAmount: number) => {
    state.projectDto.targetAmount = targetAmount
  },
  setMethod: (state, method: string) => {
    state.projectDto.method = method
  },
  setCategory: (state, category: string) => {
    state.projectDto.category = category
  },
  setTitle: (state, title: string) => {
    state.projectDto.title = title
  },
  setDescription: (state, description: string) => {
    state.projectDto.description = description
  },
  setNumImages: (state, numImages: number) => {
    state.projectDto.numImages = numImages
  },
  setNumVideos: (state, numVideos: number) => {
    state.projectDto.numVideos = numVideos
  },
  setTwitterExistence: (state, twitterExistence: boolean) => {
    state.projectDto.twitterExistence = twitterExistence
  },
  setTwitterFriends: (state, twitterFriends: number) => {
    state.projectDto.twitterFriends = twitterFriends
  },
  setTwitterFollowers: (state, twitterFollowers: number) => {
    state.projectDto.twitterFollowers = twitterFollowers
  },
  setFacebookExistence: (state, facebookExistence: boolean) => {
    state.projectDto.facebookExistence = facebookExistence
  },
  setInstagramExistence: (state, instagramExistence: boolean) => {
    state.projectDto.instagramExistence = instagramExistence
  },
  setWebpageExistence: (state, setWebpageExistence: boolean) => {
    state.projectDto.webpageExistence = setWebpageExistence
  }
}

export default mutations
