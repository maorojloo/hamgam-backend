from . import views
from django.urls import URLPattern, path

urlpatterns = [

    path('',views.appealAPIView.as_view()),
    path('<int:pk>',views.appealAPIView.as_view()),





]
