from django.contrib import admin
from django.contrib.auth.models import User

# registra o modelo User no admin se não quiser usar o padrão 'auth.User'
admin.site.unregister(User)  # opcional, pra customizar exibição

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_active", "last_login")
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_active")
