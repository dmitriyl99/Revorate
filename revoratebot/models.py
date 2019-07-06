from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    telegram_user_id = models.IntegerField(blank=True, null=True)
    token = models.CharField(max_length=100)
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_dispatcher = models.BooleanField(blank=True, null=True)
    is_driver = models.BooleanField(blank=True, null=True)
    language = models.CharField(max_length=10)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Rating(models.Model):
    from_id = models.IntegerField()
    to_id = models.IntegerField()
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=500)
