from django.db import models
from django.conf import settings

User=settings.AUTH_USER_MODEL

class work(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    info = models.TextField()
    date_time = models.DateTimeField()