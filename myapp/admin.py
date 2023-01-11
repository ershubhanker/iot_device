from django.contrib import admin
from .models import *

admin.site.register(WifiDetails)
# @admin.register(WifiDetails)
# class WifiDetailsAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return False

    # to disable editing for specific or all fields
    # you can use readonly_fields attribute
    # (to see data you need to remove editable=False from fields in model):
    # readonly_fields = ('ssid', 'password')


# @admin.register(DateTimeDetails)
# class DateTimeDetailsAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return False

    # to disable editing for specific or all fields
    # you can use readonly_fields attribute
    # (to see data you need to remove editable=False from fields in model):
    # readonly_fields = ('_date', '_time')
    
admin.site.register(DateTimeDetails)
admin.site.register(lockoutDetails)
# class lockoutDetailsAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return False

    # to disable editing for specific or all fields
    # you can use readonly_fields attribute
    # (to see data you need to remove editable=False from fields in model):
    # readonly_fields = ('weekday1', 'weekday2')


admin.site.register(ECDetails)
# admin.site.register(AllDetail)


