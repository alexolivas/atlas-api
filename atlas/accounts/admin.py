from django.contrib import admin
from atlas.accounts.models import Account
from atlas.accounts.models import AccountOwner


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_number', 'industry', 'website',)
admin.site.register(Account, AccountAdmin)


class AccountOwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email',)
admin.site.register(AccountOwner, AccountOwnerAdmin)
