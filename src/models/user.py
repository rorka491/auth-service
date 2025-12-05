from tortoise import fields
from src.models.base import BaseModelPK

class AbstrctUser(BaseModelPK):
    username = fields.CharField(max_length=255, unique=True)
    email = fields.CharField(max_length=255, unique=True, null=True)
    password = fields.CharField(max_length=128)

    class Meta:
        abstract = True


    def __str__(self):
        return f'{self.username} - {self.email}'
    

class User(AbstrctUser):
    class Meta:
        table = 'users'

