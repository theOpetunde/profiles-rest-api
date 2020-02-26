from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow usere to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

#Create a custom permission to allow status update for Users
class UpdateOwnStatus(permissions.BasePermission):
    """Allows users to update their own status"""
    def has_object_permission(self, request, view, obj):
        """check the user is trying their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
