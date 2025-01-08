from .serializers import CareerSerializer
from .models import Career
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse

class CareerView(APIView):
    def get(self, request, *args, **kwargs):
        careers = Career.objects.all()
        serializer = CareerSerializer(careers, many=True)
        content = {"careers": serializer.data}

        return JsonResponse(content, status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        try:
            career_to_be_deleted = Career.objects.get(id=id)
            career_to_be_deleted.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Career.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
