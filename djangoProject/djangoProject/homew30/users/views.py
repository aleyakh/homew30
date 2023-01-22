from django.db.models import Count, Q
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.serializers import UserDetailSerializer, UserListSerializer, UserCreateSerializer, UserUpdateSerializer, \
    LocationModelSerializer


class UserPagination(PageNumberPagination):
    page_size = 5


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserListView(ListAPIView):
    queryset = User.objects.annotate(total_ads=Count("ads", filter=Q(ads__is_published=True))).order_by("username")
    serializer_class = UserListSerializer
    pagination_class = UserPagination


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationModelSerializer
