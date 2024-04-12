from django.db import models
from clientes.models import Cliente

class Log(models.Model):
    id = models.CharField(max_length=120)
    level = models.CharField(max_length=10)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Cliente, on_delete = models.CASCADE, default = None)
    time = models.TextField()

    def str(self):
        return f'{self.created} {self.level} {self.message}'
