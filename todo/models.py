from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    todo_text = models.CharField(max_length=200)
    complete = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

    def __str__(self):
    	return self.todo_text 
    def state(self):
    	return self.complete