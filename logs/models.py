from django.db import models
import logging

class Log(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False)
    LOG_LEVEL_CHOICES = [
        (logging.getLevelName(logging.DEBUG), 'DEBUG'),
        (logging.getLevelName(logging.INFO), 'INFO'),
        (logging.getLevelName(logging.WARNING), 'WARNING'),
        (logging.getLevelName(logging.ERROR), 'ERROR'),
        (logging.getLevelName(logging.CRITICAL), 'CRITICAL'),
    ]

    level = models.CharField(max_length=10, choices=LOG_LEVEL_CHOICES)
    message = models.TextField()
    user = models.BigIntegerField(default=None)
    time = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.level} - {self.message} - {self.user} - {self.time}'
