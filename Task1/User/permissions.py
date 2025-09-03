from rest_framework import permissions

class RoleBasedPermission(permissions.BasePermission):
    """
    CRUD uchun rollarga qarab ruxsat beradi
    - Admin: hamma narsaga ruxsat
    - Teacher: Create, Read, Update mumkin, Delete yo‘q
    - Student: faqat Read
    - Manager: Read + Update
    - Parent: faqat Read
    """

    def has_permission(self, request, view):
        # Faqat login bo'lgan user ishlata oladi
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        role = request.user.role
        method = request.method

        if role == "admin":
            return True  # hammasi mumkin

        elif role == "teacher":
            return method in ["GET", "POST", "PUT", "PATCH"]

        elif role == "student":
            return method == "GET"

        elif role == "manager":
            return method in ["GET", "PUT", "PATCH"]

        elif role == "parent":
            return method == "GET"

        return False
