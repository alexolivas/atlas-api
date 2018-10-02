from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=150)
    account_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    account_owner = models.ForeignKey('AccountOwner', on_delete=models.CASCADE)
    industry = models.CharField(max_length=50)
    phone = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    billing_street = models.CharField(max_length=90, blank=True, null=True)
    billing_street_2 = models.CharField(max_length=30, blank=True, null=True)
    billing_city = models.CharField(max_length=90, blank=True, null=True)
    billing_state = models.CharField(max_length=2, blank=True, null=True)
    billing_zip = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class AccountOwner(models.Model):
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
