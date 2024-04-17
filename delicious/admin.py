from django.contrib import admin
from .models import Order,Cart,UserDetails,FoodVlogs,ExecutiveDetails,Advertisements
# Register your models here.

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(UserDetails)
admin.site.register(FoodVlogs)
admin.site.register(ExecutiveDetails)
admin.site.register(Advertisements)