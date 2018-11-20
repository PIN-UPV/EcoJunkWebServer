from rest_framework import permissions


class IsUserOwnerForDeletes(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ("DELETE"):
            return request.user == obj.customer
        return True
