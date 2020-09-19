from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount


# Register your models here.

class AccountAdmin(UserAdmin):
    # for column header display in admin section
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    # Fields that can be queried from the search bar
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(UserAccount, AccountAdmin)
