from django.contrib import admin
from .models import register
# Register your models here.
admin.site.register(register)
from django.contrib import admin
from .models import AboutPage

admin.site.register(AboutPage)

from django.contrib import admin
from .models import ContactSubmission

admin.site.register(ContactSubmission)
