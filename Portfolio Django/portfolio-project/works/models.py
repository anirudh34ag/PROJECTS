from django.db import models


class Job(models.Model):
    #Image
    image = models.ImageField(upload_to =  "images/")

    #Summary
    summary = models.CharField(max_length = 200)


