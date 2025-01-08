from .serializers import PostSerializer, PostSchemaPostSerializer, PostSchemaPatchSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse

class PostView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        content = {"resource": serializer.data}

        return JsonResponse(content, status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        try:
            post_to_be_deleted = Post.objects.get(id=id)
            post_to_be_deleted.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        serializer = PostSchemaPostSerializer(data=request.data)
        data_is_valid = serializer.is_valid()

        if not data_is_valid:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        body = serializer.validated_data

        created_post = Post(
            username=body['username'],
            title=body['title'],
            content=body['content']
        )
        created_post.save()

        serialized_created_post = PostSerializer(created_post, many=False)
        content = {"resource": serialized_created_post.data}

        return JsonResponse(content, status=status.HTTP_201_CREATED)

    def patch(self, request, id, *args, **kwargs):
        serializer = PostSchemaPatchSerializer(data=request.data)
        data_is_valid = serializer.is_valid()

        if not data_is_valid:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        body = serializer.validated_data

        try:
            post_to_update = Post.objects.get(id=id)

            post_to_update.title = body['title']
            post_to_update.content = body['content']
            post_to_update.save()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)