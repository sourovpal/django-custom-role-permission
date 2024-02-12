from role.models import Admin
from django.http import HttpResponse
def can(permission=""):
    def decorator_wrapper(view_func):
        def func_wrapper(request, *args, **kwargs):
            try:
                # admin = request.user.filter(id=1).first()
                admin = Admin.objects.filter(id=1).first()
            except Exception as e:
                admin = None
            if admin:
                try:
                    hasPermisssion = admin.role.permissions.filter(name=permission, guard_name="admin").first()
                except Exception as e:
                    hasPermisssion = None
                if hasPermisssion:
                    request.user = admin
                    request.role = admin.role
                    request.permission = hasPermisssion
                    return view_func(request, *args, **kwargs)
                return HttpResponse("Not Permission")
        return func_wrapper
    return decorator_wrapper