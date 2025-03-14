from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from limitless.admin import admin
from users.models import Profile, User


class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        ("Credentials", {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active",)}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "date_joined",
        "last_login",
    )
    list_filter = ("is_active",)
    search_fields = ("email", "first_name", "last_name")
    date_hierarchy = "date_joined"
    readonly_fields = ("date_joined", "last_login")
    ordering = ("-date_joined",)


admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "avatar")
    search_fields = ("user__email",)
    list_filter = ("user__is_active",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "last_modified_at")
