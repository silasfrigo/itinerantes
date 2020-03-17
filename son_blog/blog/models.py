from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=255)
    
    summary = RichTextField()
    content = RichTextUploadingField()
    
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


    def save(self,*args, **kwargs):
        #Check if admin is logged
        #if self.admin==true;
        super().save(*args,**kwargs) # call the save method in an function
