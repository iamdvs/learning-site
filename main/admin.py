from django.contrib import admin
# Register your models here.


from .models import *

admin.site.register(Series)
admin.site.register(Articles)