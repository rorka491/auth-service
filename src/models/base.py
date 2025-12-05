from tortoise import fields, models


class BaseModelPK(models.Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True
    

    def __str__(self) -> str:
        return f'Object {self.__class__.__name__} ({self.id})'

