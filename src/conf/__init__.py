"""
Auto create super user
"""
from django.contrib.auth import get_user_model
from django.conf import settings
import django


django.setup()
User = get_user_model()

username = getattr(settings, 'DJANGO_SU_USERNAME', None)
email = getattr(settings, 'DJANGO_SU_EMAIL', None)
password = getattr(settings, 'DJANGO_SU_PASSWORD', None)


if not User.objects.filter(username=username, email=email).exists():
    User.objects.create_superuser(username, email, password)
