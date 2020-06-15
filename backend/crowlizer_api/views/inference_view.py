from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .inference_request_converter import InferenceRequestConverter
from .inference_request_checker import InferenceRequestChecker
from ..models.app.inference_service import InferenceService


class InferenceView(APIView):

    def __init__(self):
        super(InferenceView).__init__()
        self._converter = InferenceRequestConverter()
        self._checker = InferenceRequestChecker()
        self._service = InferenceService()

    def put(self, request):
        request_dto = self._converter.json2request(request.data)
        self._checker.check(request_dto)
        input_dto = self._converter.request2input(request_dto)
        output_dto = self._service.infer(input_dto)
        return Response(output_dto.to_json(), status.HTTP_200_OK)
