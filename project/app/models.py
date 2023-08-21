from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Asset(models.Model):
    NAME_CHOICES = (
        ("1", "Macbook"),
        ("2", "Asus-Laptop"),
        ("3", "Monitor"),
        ("4", "Laptop-Stand"),
        ("5", "HDMI"),
        ("6", "Keyboard"),
        ("7", "Mouse"),
    )

    name = models.CharField(choices=NAME_CHOICES, max_length=50)
    asset_id = models.CharField(max_length=50, unique=True)
    serial_number = models.CharField(max_length=50, unique=True)
    manufact_user = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    purchase_date = models.DateField()
    condition = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.asset_id


class AssignManager(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    is_returned = models.BooleanField(default=False)
    request_to_accept = models.BooleanField(default=False)
    request_to_return = models.BooleanField(default=False)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_by")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_to")
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.asset.asset_id
