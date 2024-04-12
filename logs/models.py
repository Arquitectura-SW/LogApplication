from django.db import models

class Log(models.Model):
    id = models.CharField(max_length=120)
    level = models.CharField(max_length=10)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.BigIntegerField()
    time = models.TextField()

    def str(self):
        return f'{self.created} {self.level} {self.message}'
