from django.db import models


class ToDoElement(models.Model):
    text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
