from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=20, blank=False)
    description = models.TextField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title