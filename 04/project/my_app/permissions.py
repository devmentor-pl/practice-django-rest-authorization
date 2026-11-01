from rest_framework.permissions import BasePermission
from .acl import check_permission


class NoteACLPermission(BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method == "GET":
            action = "read"
        elif request.method in ["PUT", "PATCH"]:
            action = "update"
        elif request.method == "DELETE":
            action = "delete"
        else:
            action = "other"

        return check_permission(request.user, obj, action)

    def has_permission(self, request, view):

        if request.method == "POST":
            return check_permission(request.user, None, "create")

        return bool(request.user and request.user.is_authenticated)