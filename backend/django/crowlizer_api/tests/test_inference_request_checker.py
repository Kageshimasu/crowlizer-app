import datetime
import unittest

from crowlizer_api.views.inference_request_checker import InferenceRequestChecker
from crowlizer_api.models.domain.inference_input_dto import InferenceInputDto


def create_dummy_correct_input_dto():
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


class InferenceRequestCheckerTest(unittest.TestCase):

    def test_checker(self):
        input_dto = create_dummy_correct_input_dto()
        checker = InferenceRequestChecker()
        checker.check(input_dto)


if __name__ == '__main__':
    unittest.main()
