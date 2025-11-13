from django.db.models.signals import post_migrate
from django.contrib.auth import get_user_model
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_superuser(sender, **kwargs):
    if sender.name != "apps.accounts":
        return

    User = get_user_model()

    if not User.objects.filter(username="pam").exists():
        User.objects.create_superuser(
            username="pam",
            email="pam@corposcienza.com.br",
            password="123qwe"
        )
        print(">>> Superuser padrão criado: pam / 123qwe")

    if not User.objects.filter(username="henrique").exists():
        User.objects.create_superuser(
            username="henrique",
            email="henrique@corposcienza.com.br",
            password="1a2b3c4f"
        )
        print(">>> Superuser criado: henrique / 1a2b3c4f")
