from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """
    Allows access only to Account owners.
    """

    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False
