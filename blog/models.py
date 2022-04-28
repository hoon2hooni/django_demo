from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    head_image = models.ImageField(upload_to="blog/images/%Y/%m/%d/%H",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now =True)
    
    def __str__(self):
        return f"제목:{self.title} 내용:{self.content}" 