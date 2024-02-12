from django.urls import path
from .views import createRole, createPermission, roleHasPermission, createUser
urlpatterns = [
    path("/create-role", createRole),
    path("/create-user", createUser),
    # path("/create-permission/", createPermission),
    # path("/role-has-permisssion/", roleHasPermission),
]
