from rest_framework import permissions


class RiderPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "accept_deal" or view.action == "decline_deal":
            return request.user.is_authenticated and request.user.is_rider
        return True
