from django.urls import path

from ads.views import *

urlpatterns = [

    path('ad/', AdsListViews.as_view()),
    path('ad/<int:pk>/', AdsDetailView.as_view()),
    path('ad/create/', AdsCreateView.as_view()),
    path('ad/update/<int:pk>/', AdsUpdateView.as_view()),
    path('ad/delete/<int:pk>/', AdsDeleteView.as_view()),
    path('ad/upload_image/<int:pk>/', AdsUploadImage.as_view()),

    path('cat/', CategoriesListViews.as_view()),
    path('cat/<int:pk>/', CategoriesDetailView.as_view()),
    path('cat/create/', CategoriesCreateView.as_view()),
    path('cat/update/<int:pk>/', CategoriesUpdateView.as_view()),
    path('cat/delete/<int:pk>/', CategoriesDeleteView.as_view()),

]
