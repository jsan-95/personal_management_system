# -*- coding: utf-8 -*-
from rest_framework import routers
from user.viewsets import UserViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
