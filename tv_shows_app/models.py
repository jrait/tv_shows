from django.db import models
from datetime import date,datetime

class ShowsManager(models.Manager):
    def validator(self,postData):
        today = datetime.now()
        rel_date = datetime.strptime(postData['release_date'], '%Y-%m-%d')
        errors = {}
        if len(postData['title'])<2:
            errors['title'] = "Title must be at least 2 characters!"
        if len(postData['network']) <3:
            errors['network'] = "Network must be at least 3 characters!"
        if len(postData['desc'])<10 and len(postData['desc']) != 0:
            errors['desc'] = "Description must be at least 10 characters!"
        if rel_date > today:
            errors['date'] = "Release Date must be in the past!"
        
        return errors
# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length = 255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowsManager()


