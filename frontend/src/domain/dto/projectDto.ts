import ProjectConst from '@/domain/const/projectConst'

export default class ProjectDto {
  targetAmount = 0
  startDate = new Date().toISOString().substr(0, 10)
  endDate = new Date().toISOString().substr(0, 10)
  method = ProjectConst.allOrNothing
  category = ''
  title = ''
  description = ''
  numImages = 0
  numVideos = 0
  twitterExistence = false
  twitterFriends = 0
  twitterFollowers = 0
  facebookExistence = false
  instagramExistence = false
  webpageExistence = false
}
