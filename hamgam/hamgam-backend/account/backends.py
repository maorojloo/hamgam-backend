from typing import Any, Optional
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest 



class EmailBackend(ModelBackend):
    def authenticate(self, request: Optional[HttpRequest], email: Optional[str] = ..., password: Optional[str] = ..., **kwargs: Any):
        username = email
        User = get_user_model()

