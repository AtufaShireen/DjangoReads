from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# declare a new model with a name "Post"
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
#renames the instances of the model with their title name
    def __str__(self):
        return self.title