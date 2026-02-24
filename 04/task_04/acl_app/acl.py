from rest_framework.permissions import BasePermission


def acl(user, obj, action):
    if not user or not user.is_authenticated:  # sprawdzenie czy uzytkonwik jest zalogowany
        return False

    # sprawdzenie czy zostala podana odpowiednia metoda
    if action in {"read", "update", "delete"}:
        # jezeli wlasciciel zgadza sie z uzytkownikiem zwraca True
        return obj.owner_id == user.id

    return False


class IsOwner(BasePermission):
    method_to_action = {
        "GET": "read",
        "PUT": "update",
        "PATCH": "update",
        "DELETE": "delete",
    }

    def has_object_permission(self, request, view, obj):
        action = self.method_to_action.get(request.method)
        if action is None:
            return False
        return acl(request.user, obj, action)
