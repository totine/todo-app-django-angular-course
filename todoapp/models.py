from django.db import models


class ToDoElement(models.Model):
    todo_text = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
