from django.urls import path, include
from .views import idea_list, idea_detail, idea_list_published 


urlpatterns = [
    path('', idea_list),
    path('<int:pk>/', idea_detail),
    path('published/', idea_list_published)
]