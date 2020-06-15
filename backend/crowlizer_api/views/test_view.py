from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from crowlizer_api.models.infra.abstract_json_dto import AbstractJsonDto


class Tekito(AbstractJsonDto):

    def __init__(self):
        self.name = 'tarou'
        self.age = 17


class View1(APIView):

    @staticmethod
    def hello(request):
        print(request)
        tekito = Tekito()
        return HttpResponse(tekito)

    def put(self, request) -> Response:
        print('================')
        j = request.data
        print(j['targetAmount'])
        tekito = Tekito()
        return Response(str(tekito), status.HTTP_200_OK)
