import datetime
import unittest

from crowlizer_api.models.app.inference_service import InferenceService
from crowlizer_api.models.domain.inference_input_dto import InferenceInputDto


def create_dummy_input_dto():
    inference_input_dto = InferenceInputDto()
    inference_input_dto.targetAmount = 240000
    inference_input_dto.startDate = datetime.datetime(2020, 6, 1)
    inference_input_dto.endDate = datetime.datetime(2020, 6, 8)
    inference_input_dto.method = 'all-in'
    inference_input_dto.category = '音楽'
    inference_input_dto.title = 'test'
    inference_input_dto.description = 'testtesttest'
    inference_input_dto.numImages = 0
    inference_input_dto.numVideos = 0
    inference_input_dto.twitterExistence = True
    inference_input_dto.twitterFriends = 8
    inference_input_dto.twitterFollowers = 10
    inference_input_dto.facebookExistence = False
    inference_input_dto.instagramExistence = False
    inference_input_dto.webPageExistence = False
    return inference_input_dto


class InferenceServiceTest(unittest.TestCase):

    def test_inference(self):
        input_dto = create_dummy_input_dto()
        InferenceService.infer(input_dto)


if __name__ == '__main__':
    unittest.main()
