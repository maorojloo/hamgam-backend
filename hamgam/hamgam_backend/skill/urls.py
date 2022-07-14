from django.urls import path, include
from . import views

urlpatterns = [
    #path('', Skill_list),
    #path('<int:pk>/', Skill_detail),
    #path('published/', Skill_list_published),
    path('',views.ListSkill.as_view()),
    #path('create',views.ListSkill.as_view()),
    path('<int:pk>/', views.DetailSkill.as_view()),
    path('<int:pk>/update', views.UpdateSkill.as_view()),
    path('<int:pk>/delete', views.DeleteSkill.as_view()),   
]