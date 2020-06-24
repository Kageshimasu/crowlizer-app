import axios from 'axios'
import ProjectDto from '@/domain/dto/projectDto'

export default class ProbabilityPredictionService {
  private static INSTANCE: ProbabilityPredictionService

  public static get instance (): ProbabilityPredictionService {
    if (!this.INSTANCE) {
      this.INSTANCE = new ProbabilityPredictionService()
    }
    return this.INSTANCE
  }

  public async predictProbability (projectDto: ProjectDto) {
    // const response = await axios.put(
    //   '/crowlizer/api/inference/',
    //   projectDto
    // )
    const sleep = (msec: number) => new Promise(resolve => setTimeout(resolve, msec))
    await sleep(5000)
    console.log('test')
    // console.log(response.data.predicted_success_prob)
    return null
  }
}
