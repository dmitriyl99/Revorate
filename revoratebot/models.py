from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)


class Department(models.Model):
    name = models.CharField(max_length=150)
    code_name = models.CharField(max_length=50, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    telegram_user_id = models.IntegerField(blank=True, null=True)
    token = models.CharField(max_length=100)
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    is_manager = models.BooleanField(default=False)


class Rating(models.Model):
    from_id = models.IntegerField()
    to_id = models.IntegerField()
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=500)
