from lib2to3.pytree import Base
from rest_framework.permissions import BasePermission

class NotAuthenticated(BasePermission):
    message = "You already have an account."
    def has_permission(self, request, view):
        return  not request.user.is_authenticated
    
    # message = "You must be the ownear of this object"

    # def has_object_permission(self, request, view, obj):
    #     return obj.user == request.user