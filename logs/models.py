from django.db import models
from uuid import uuid4

class Log(models.Model):
    uid = models.UUIDField(default=uuid4, editable=False)
    level = models.CharField(max_length=10)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.BigIntegerField(default=None)
    time = models.TextField(default='')

    def str(self):
        return f'{self.created} {self.level} {self.message}'
