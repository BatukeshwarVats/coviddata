from django.contrib import admin

# Register your models here.
from .models import Info
admin.site.register(Info)

from .models import ContactForm
admin.site.register(ContactForm)