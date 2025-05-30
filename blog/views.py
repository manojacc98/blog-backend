from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate
from django.db import IntegrityError

from .models import Blog, AppUser
from .serializers import BlogSerializer, RegisterSerializer
from rest_framework.pagination import PageNumberPagination
User = get_user_model()


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-published_at')
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        blog = self.get_object()
        if blog.author != request.user:
            return Response({'detail': 'Not allowed.'}, status=403)
        print("Incoming PUT data:", request.data)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        blog = self.get_object()
        if blog.author != request.user:
            return Response({'detail': 'Not allowed.'}, status=403)
        return super().destroy(request, *args, **kwargs)


@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"error": "User with this email already exists."}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(email=email, password=password)

    if user is None:
        return Response({"detail": "Invalid credentials"}, status=401)

    refresh = RefreshToken.for_user(user)
    return Response({
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    })



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    return Response({
        "username": request.user.username,
        "email": request.user.email
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_blogs(request):
    user = request.user
    blogs = Blog.objects.filter(author=user).order_by('-published_at')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)



class BlogPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 12

@api_view(['GET'])
def public_blogs(request):
    blogs = Blog.objects.all().order_by('-published_at')
    paginator = BlogPagination()
    result_page = paginator.paginate_queryset(blogs, request)
    serializer = BlogSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
