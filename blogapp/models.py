from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# declare a new model with a name "Post"
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    bg_pic = models.ImageField(default='def.png', upload_to='post_pics')

    # renames the instances of the model with their title name
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        pat=self.bg_pic.path
        img = Image.open(pat)
        if img.mode in ("RGBA", "P"): img = img.convert("RGB")
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(pat)
