import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from .models import Blog
from .serializers import BlogSerializer

class GetBlog(APIView):
    def get(self, request, slug):
        try:
            blog = Blog.objects.get(slug=slug)
            serializer = BlogSerializer(blog).data
            return Response(
                {
                    "status": "success",
                    "message": "Blog retrieved successfully",
                    "data": serializer
                },
                status=status.HTTP_200_OK
            )
        except Blog.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "Blog not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
class GetAllBlogs(APIView):
    def get(self, request):
        blogs = Blog.objects.all().order_by('-created_at')
        serializer = BlogSerializer(blogs, many=True).data
        return Response(
            {
                "status": "success",
                "message": "Blogs retrieved successfully",
                "data": serializer
            },
            status=status.HTTP_200_OK
        )

