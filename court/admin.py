from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Advocate)
admin.site.register(Case)
admin.site.register(Judge)
# Register your models here.
