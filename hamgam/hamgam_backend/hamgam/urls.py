from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('mamad', views.mamad),

    path('admin/', admin.site.urls),
        # ...
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/ideas/', include('idea.urls')),
    path('api/skills/', include('skill.urls')),
    path('api/accounts/', include('account.urls')),

]
