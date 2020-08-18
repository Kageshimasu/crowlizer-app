import ProjectConst from '@/domain/const/projectConst'

export default class ProjectDto extends Object {
  targetAmount = 0
  startDate = new Date().toISOString().substr(0, 10)
  endDate = new Date().toISOString().substr(0, 10)
  method = ProjectConst.allOrNothing
  category = 0
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

  equals (projectDto: ProjectDto) {
    const memberList = Object.getOwnPropertyNames(projectDto)
    for (const val of memberList) {
      if ((this as any)[val] !== (projectDto as any)[val]) {
        return false
      }
    }
    return true
  }
}
