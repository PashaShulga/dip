from django.db import models
from django.db.models import Model


class Operators(models.Model):
    class Meta:
        db_table = "operator"

    operator_name = models.CharField(max_length=20, blank=True)


class Client(models.Model):
    class Meta:
        db_table = "client"

    client_name = models.CharField(max_length=100)
    client_telephone = models.CharField(max_length=25)
    operator = models.ForeignKey('Operators')
    tariff_mts = models.ManyToManyField('TariffMTS')


class Actions(models.Model):
    class Meta:
        db_table = "actions"

    name_action = models.CharField(max_length=50)
    action_desc = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    action_operator = models.OneToOneField(Operators)


class TariffMTS(models.Model):
    id = models.AutoField(db_column='tariff_id', primary_key=True)
    name = models.CharField(max_length=50, db_column='name_of_tariff', blank=True, null=True)
    mobile_internet_scope = models.CharField(max_length=10, blank=True, null=True)
    mobile_internet_pay = models.FloatField(blank=True, null=True)
    sms_mms = models.IntegerField(blank=True, null=True)
    sms_mms_pay = models.FloatField(blank=True, null=True)
    theeG = models.BooleanField(default=False, blank=True)
    treeG_scope = models.CharField(max_length=50, blank=True, null=True)
    treeG_pay = models.IntegerField(blank=True, null=True)
    call_out = models.FloatField(blank=True, null=True)
    call_out_pay = models.FloatField(blank=True, null=True)
    call_out_minutes = models.IntegerField(blank=True, null=True)
    call_rouming_pay = models.FloatField(blank=True, null=True)
    call_in_pay = models.FloatField(blank=True, null=True)
    call_in_minutes = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'mts'


class TariffKievstar(models.Model):
    id = models.AutoField(db_column='tariff_id', primary_key=True)
    name = models.CharField(max_length=50, db_column='name_of_tariff')
    mobile_internet_scope = models.CharField(max_length=10)
    sms_mms = models.CharField(max_length=50)
    sms_mms_counter = models.CharField(max_length=50)
    theeG = models.BooleanField(default=False)
    treeG_scope = models.CharField(max_length=50)
    treeG_pay = models.IntegerField()
    call_out = models.DecimalField(max_digits=3, decimal_places=2)
    call_out_pay = models.DecimalField(max_digits=3, decimal_places=2)
    call_out_minutes = models.IntegerField()
    call_in_pay = models.DecimalField(max_digits=3, decimal_places=2)
    call_in_minutes = models.IntegerField()

    class Meta:
        db_table = 'kievstar'


class TariffLifeOverload(models.Model):
    id = models.AutoField(db_column='tariff_id', primary_key=True)
    mobile_internet_scope = models.CharField(max_length=10)
    mobile_internet_pay = models.IntegerField()
    mobile_internet_out_country = models.DecimalField(max_digits=3, decimal_places=2)
    mobile_internet_access = models.DecimalField(max_digits=5, decimal_places=2)
    sms_in_country = models.DecimalField(max_digits=3, decimal_places=2)
    mms_in_country = models.DecimalField(max_digits=3, decimal_places=2)
    call_in_any_country = models.DecimalField(max_digits=3, decimal_places=2)
    theeG = models.BooleanField(default=False)
    treeG_scope = models.CharField(max_length=50)
    treeG_pay = models.IntegerField()
    call_out_out_country = models.DecimalField(max_digits=3, decimal_places=2)
    call_in_pay = models.DecimalField(max_digits=3, decimal_places=2)
    call_in_minutes = models.IntegerField()

    class Meta:
        db_table = 'life_overload'


class TariffLifeStock(models.Model):
    id = models.AutoField(db_column='tariff_id', primary_key=True)
    name = models.CharField(max_length=50, db_column='name_of_tariff')
    sum = models.DecimalField(max_digits=5, decimal_places=2)
    call_in_minutes = models.IntegerField()
    call_in_other_oper = models.IntegerField()
    mobile_internet = models.IntegerField()
    call_out_oper = models.IntegerField()
    mms_in_country = models.IntegerField()
    sms_in_country = models.IntegerField()

    class Meta:
        db_table = 'life_stock'


class TariffLifeMiddle(models.Model):
    id = models.AutoField(db_column='tariff_id', primary_key=True)
    name = models.CharField(max_length=30, db_column='name_of_tariff')
    sum = models.DecimalField(max_digits=5, decimal_places=2)
    call_in_minutes = models.IntegerField()
    call_in_other_oper = models.IntegerField()
    mobile_internet = models.IntegerField()
    call_out_oper = models.IntegerField()
    mms_in_country = models.IntegerField()
    sms_in_country = models.IntegerField()

    class Meta:
        db_table = 'life_middle'


class TariffLifeBest(models.Model):
    id = models.AutoField(db_column='tariff_id', primary_key=True)
    name = models.CharField(max_length=30, db_column='name_of_tariff')
    sum = models.DecimalField(max_digits=5, decimal_places=2)
    call_in_minutes = models.IntegerField()
    call_in_other_oper = models.IntegerField()
    mobile_internet = models.IntegerField()
    call_out_oper = models.IntegerField()
    mms_in_country = models.IntegerField()
    sms_in_country = models.IntegerField()

    class Meta:
        db_table = 'life_best'