from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# registra o modelo User no admin se não quiser usar o padrão 'auth.User'
# admin.site.unregister(CustomUser)  # opcional, pra customizar exibição

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ("username", "email", "is_staff", "is_active", "last_login")
#     search_fields = ("username", "email")
#     list_filter = ("is_staff", "is_active")

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ("username", "email", "full_name", "is_staff", "is_active")

    search_fields = ("username", "email")
    list_filter = ("is_active", "is_staff")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Informações pessoais", {"fields": ("first_name", "last_name", "email", "phone")}),
        (
            "Permissões",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Datas importantes", {"fields": ("last_login", "date_joined")}),
    )

    # Campos que aparecem NA TELA DE "ADICIONAR" usuário
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )