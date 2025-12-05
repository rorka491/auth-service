from tortoise import fields
from src.models.base import BaseModelPK



class Admin(BaseModelPK):
    username = fields.CharField(max_length=32, unique=True)
    password = fields.CharField(max_length=128)
    is_active = fields.BooleanField(default=True)

    class Meta:
        table = "admin"





