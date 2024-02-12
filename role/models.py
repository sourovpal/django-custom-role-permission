from typing import Any
from django.db import models

class Permission(models.Model):
     name = models.CharField(max_length=250, blank=False, null=False, unique=True)
     slug = models.CharField(max_length=250, blank=False, null=False)
     group_name = models.CharField(max_length=250, blank=False, null=False)
     guard_name = models.CharField(max_length=250, blank=False, null=False)
     class Meta:
        db_table="permissions"
        constraints = [
            models.UniqueConstraint(fields=['name', 'guard_name'], name='permission_name_and_guard_name_unique')
        ]

class Role(models.Model):
     name = models.CharField(max_length=250, blank=False, null=False, unique=True)
     guard_name = models.CharField(max_length=250, blank=False, null=False)
     permissions = models.ManyToManyField(Permission, verbose_name='permissions', related_query_name="role_has_permissions")
     class Meta:
        db_table="roles"
        constraints = [
            models.UniqueConstraint(fields=['name', 'guard_name'], name='role_name_and_guard_name_unique')
        ]


class Admin(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    role = models.OneToOneField(Role, on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table="admins"

    def has_permissions(self, permission, group_name="admin"):
        try:
            check = self.role.permissions.filter(name=permission, guard_name=group_name).first()
        except Exception as e:
            check = None
        if check:
            return True
        return False

    def has_role(self):
        try:
            check = self.role
        except Exception as e:
            check = None
        if check:
            return check
        return None

