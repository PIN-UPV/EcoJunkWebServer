from rest_framework import permissions


class NoDeletes(permissions.BasePermission):
    """Doesn't allow deletes for the resource."""

    def has_permission(self, request, view):
        if request.method == "DELETE":
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return False
        return True


class NoUpdates(permissions.BasePermission):
    """Doesn't allow updates for the resource."""

    def has_permission(self, request, view):
        if request.method == "PATCH":
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "PATCH":
            return False
        return True
