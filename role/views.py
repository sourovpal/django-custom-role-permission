from django.shortcuts import render
from .models import Role, Permission, Admin
from django.forms import model_to_dict
from django.http import HttpResponse
# Create your views here.
from core.decorators.can import can

def createRole(request):
    try:
        data = [
            {
                "name":"Owner",
                "guard_name":"admin",
            },
            {
                "name":"Admin",
                "guard_name":"admin",
            },
            {
                "name":"Manager",
                "guard_name":"admin",
            },
        ]
        for role in data:
            Role.objects.create(**role)
        createPermission()
    except Exception as e:
        pass
    return HttpResponse("New Role Created Successful")

def createPermission():
    try:
        data = [
            {
                "name":"Dashboard View",
                "slug":"dashboard-view",
                "group_name":"Dashboard",
                "guard_name":"admin",
            },
            {
                "name":"Dashboard Create",
                "slug":"dashboard-Create",
                "group_name":"Dashboard",
                "guard_name":"admin",
            },
            {
                "name":"Dashboard Edit",
                "slug":"dashboard-edit",
                "group_name":"Dashboard",
                "guard_name":"admin",
            },
            {
                "name":"Dashboard Delete",
                "slug":"dashboard-delete",
                "group_name":"Dashboard",
                "guard_name":"admin",
            },
        ]
        for permission in data:
            Permission.objects.create(**permission)
        roleHasPermission()
    except Exception as e:
        pass
    return HttpResponse("New Permission Created Successful")

def roleHasPermission():
    try:
        permissions = Permission.objects.all()
        role = Role.objects.filter(id=1).first()
        role.permissions.add(*permissions)
    except Exception as e:
        pass
    return HttpResponse("New Permission Created Successful")
@can("Dashboard Create")
def createUser(request):
    try:
        # role = Role.objects.filter(name="Owner").first()
        # Admin.objects.create(first_name="Sourov", last_name="Pal", email="sourovpal35@gmail.com", password="12345678", role=role)
        print(model_to_dict(request.user))
        print(model_to_dict(request.user.role))
        print([model_to_dict(per) for per in request.user.role.permissions.all()])
    except Exception as e:
        pass
    return HttpResponse("New Permission Created Successful")
