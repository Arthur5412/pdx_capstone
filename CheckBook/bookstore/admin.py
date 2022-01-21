from django.contrib import admin
#this imports everythng from the models
from .models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(Member)

