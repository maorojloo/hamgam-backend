from django.urls import path, include
from .views import idea_list, idea_detail, idea_list_published 
from . import views

urlpatterns = [
    path('', idea_list),
    path('<int:pk>/', idea_detail),
    path('published/', idea_list_published),
    path('mamad/',views.ListIdea.as_view()),
    path('rez/<int:pk>/', views.DetailIdea.as_view()),
    
]