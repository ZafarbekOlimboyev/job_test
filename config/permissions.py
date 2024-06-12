from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user.is_staff or request.user.is_superuser


class Cheak(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_staff
        elif request.method == 'DELETE':
            return request.user.is_superuser
        return request.user.is_superuser or request.user == view.get_object()
