from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import serializers

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerailizer
from .models import Post


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        post = qs.first()
        #serializer = PostSerailizer(qs, many=True)
        serializer = PostSerailizer(post)

        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
