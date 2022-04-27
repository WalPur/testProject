from rest_framework.permissions import IsAdminUser, SAFE_METHODS


class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly,
            self).has_permission(request, view)
        # to prevent mods to create tournaments
        return request.method in SAFE_METHODS or (is_admin and not request.user.is_mod)


class IsAdminUserAndNotMod(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserAndNotMod,
            self).has_permission(request, view)
        # to prevent mods to see users list
        return request.method in SAFE_METHODS or is_admin and not request.user.is_mod


class IsModOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_mod = super(
            IsModOrReadOnly,
            self).has_permission(request, view)
        return request.method in SAFE_METHODS or is_mod
