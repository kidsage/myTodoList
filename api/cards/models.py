from django.db import models
from api.lists.models import List
from django.contrib.auth.models import User


class Card(models.Model):
    list = models.ForeignKey(List, related_name='cards', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    position = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assignee = models.ForeignKey(User, related_name='cards', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
