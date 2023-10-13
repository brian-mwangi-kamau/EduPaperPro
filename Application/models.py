from django.db import models



class Resource(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    form = models.FileField(upload_to='forms/')

    def __str__(self):
        return self.title
