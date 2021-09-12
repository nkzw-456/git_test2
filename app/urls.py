from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Index, detail, ContactView

urlpatterns = [
    path('', views.Index.as_view()),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('list/', views.BlogListView.as_view(), name='list'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
