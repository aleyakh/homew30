from django.urls import path
from rest_framework import routers

from ads.views import *

urlpatterns = [
    path('ad/upload_image/<int:pk>/', AdsUploadImage.as_view()),
]

router = routers.SimpleRouter()
router.register('ad', AdsViewSet)

urlpatterns += router.urls
