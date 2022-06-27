from django.contrib import admin
from django.urls import path, include
from .api import router 


urlpatterns = [
    path('admin/', admin.site.urls),
        # ...
    path('__debug__/', include('debug_toolbar.urls')),
    path('ideas/', include('idea.urls')),
    path('api/v1/', include(router.urls)),
    path('api/accounts', include('account.urls')),

]
