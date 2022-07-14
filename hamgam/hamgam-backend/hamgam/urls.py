from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('mamad', views.mamad),

    path('admin/', admin.site.urls),
        # ...
    path('__debug__/', include('debug_toolbar.urls')),
    path('ideas/', include('idea.urls')),
    path('skills/', include('skill.urls')),
    path('accounts/', include('account.urls')),

]
