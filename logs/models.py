from django.db import models
from uuid import uuid4

class Log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    level = models.CharField(max_length=10)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.BigIntegerField()
    time = models.TextField(default='')

    def str(self):
        return f'{self.created} {self.level} {self.message}'
