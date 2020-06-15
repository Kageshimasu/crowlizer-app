import ProjectDto from '@/domain/dto/projectDto'
import TabDto from '@/domain/dto/tabDto'


export interface RootState {
  version: string;
}

export interface ProjectState {
  projectDto: ProjectDto;
  tabDto: TabDto;
}
