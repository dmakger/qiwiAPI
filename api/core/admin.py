from django.contrib import admin

from .models import Nationality, Gender, Profile, TypeTransaction, PaymentMethodTransaction, CategoryTransaction, \
    Transactions, Card


class NationalityAdmin(admin.ModelAdmin):
    pass


class GenderAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


class TypeTransactionAdmin(admin.ModelAdmin):
    pass


class PaymentMethodTransactionAdmin(admin.ModelAdmin):
    pass


class CategoryTransactionAdmin(admin.ModelAdmin):
    pass


class TransactionsAdmin(admin.ModelAdmin):
    pass


class CardAdmin(admin.ModelAdmin):
    pass


admin.site.register(Nationality, NationalityAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Profile, ProfileAdmin)

admin.site.register(TypeTransaction, TypeTransactionAdmin)
admin.site.register(PaymentMethodTransaction, PaymentMethodTransactionAdmin)
admin.site.register(CategoryTransaction, CategoryTransactionAdmin)
admin.site.register(Transactions, TransactionsAdmin)

admin.site.register(Card, CardAdmin)
