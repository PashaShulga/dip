from django.contrib import admin
from oper.models import Client, Operators


class ClientTariff(admin.StackedInline):
    model = Client


class OperatorTariffs(admin.StackedInline):
    model = Operators

admin.site.register(Client)
admin.site.register(Operators)