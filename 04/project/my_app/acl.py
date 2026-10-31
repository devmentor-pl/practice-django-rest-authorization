def check_permission(user, obj, action):

    if not user or not user.is_authenticated:
        return False

    if action == "create":
        return True

    if obj is None:
        return False

    if obj.owner == user:
        return action in ["read", "update", "delete"]

    return False
