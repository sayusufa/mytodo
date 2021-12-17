from django.db import models

class Task(models.Model):

    task = models.CharField(max_length=255)
    is_executed = models.BooleanField(default=False)
    day_added = models.DateTimeField(auto_now_add=True)
    Date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    time_todo = models.TimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.task