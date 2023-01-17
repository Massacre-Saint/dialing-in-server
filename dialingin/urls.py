"""dialingin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from dialinginapi.views import (
    check_user,
    register_user,
    UserView,
    MethodView,
    GrindView,
    MethodEquipmentView,
    RecipeView,
    RecipeEquipmentView
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'users')
router.register(r'methods', MethodView, 'users')
router.register(r'grinds', GrindView, 'grinds')
router.register(r'method_equip', MethodEquipmentView, 'method_equip')
router.register(r'recipes', RecipeView, 'recipes')
router.register(r'recipe_equip', RecipeEquipmentView, 'recipe_equip')
urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
