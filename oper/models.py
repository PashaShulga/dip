from django.db import models


class Operators(models.Model):
    class meta():
        db_table = "operator"

    operator_name = models.CharField(max_length=20, blank=True)
    operator_tariff_desc = models.TextField()
    operator_tariff_sum = models.FloatField(default=0.0)
    operator_tariff_date = models.DateField()


class Client(models.Model):
    class meta():
        db_table = "client"

    client_name = models.CharField(max_length=100)
    client_telephone = models.CharField(max_length=25)
    client_tariff = models.CharField(max_length=100)
    split = models.ForeignKey(Operators)


class Actions(models.Model):
    class meta():
        db_table = "actions"

    name_action = models.CharField(max_length=50)
    action_desc = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    action_operator = models.OneToOneField(Operators)
