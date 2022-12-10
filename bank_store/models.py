from django.db import models

class Bank(models.Model):

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'bank'

    def __int__(self):
        return self.id


class Branch(models.Model):

    ifsc = models.CharField(primary_key=True, max_length=11)

    bank_id = models.ForeignKey(Bank,on_delete=models.CASCADE)

    branch = models.CharField(max_length=127)

    address = models.CharField(max_length=195)

    city = models.CharField(max_length=50)

    district = models.CharField(max_length=50)

    state = models.CharField(max_length=26)

    class Meta:
        db_table = 'branch'

    def __int__(self):
        return self.ifsc
    @property
    def bank_name(self):
        return self.bank_id.name
