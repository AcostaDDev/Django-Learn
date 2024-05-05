from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsMeOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return bool(request.user.is_authenticated and request.user.username is 'david')

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            return bool(request.user.is_authenticated and request.user.username is 'david')