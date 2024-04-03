from django.db import models

class Log(models.Model):
    level = models.CharField(max_length=10)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.created} {self.level} {self.message}'
