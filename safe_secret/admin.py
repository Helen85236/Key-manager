from django.contrib import admin
from safe_secret.models import Secret

admin.site.register(Secret)
