from tortoise import fields
from src.models.base import BaseModelPK
from src.enums import UserRole

class AbstractUser(BaseModelPK):
    username = fields.CharField(max_length=255, unique=True)
    email = fields.CharField(max_length=255, unique=True, null=True)
    password = fields.CharField(max_length=128)
    role = fields.CharEnumField(enum_type=UserRole, default=UserRole.USER)
    org_id = fields.IntField(null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.username} - {self.email}'


class User(AbstractUser):
    class Meta:
        table = 'users'
