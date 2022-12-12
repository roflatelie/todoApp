from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=50, default='Title')
    description = models.CharField(max_length=200, default='None', blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
