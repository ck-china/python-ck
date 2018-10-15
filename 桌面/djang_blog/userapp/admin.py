from django.contrib import admin
from .models import BlogUser,EmailVerifyRecord,userlogin
class EmailAdmin(admin.ModelAdmin):
    list_display = ["id",'code',"send_type","send_time"]
# Register your models here.
admin.site.register(BlogUser)
admin.site.register(EmailVerifyRecord,EmailAdmin)
admin.site.register(userlogin)