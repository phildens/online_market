from django.contrib import admin
from resetpassword.models import ResetPassword


@admin.register(ResetPassword)
class ModelNameAdmin(admin.ModelAdmin):
    pass
