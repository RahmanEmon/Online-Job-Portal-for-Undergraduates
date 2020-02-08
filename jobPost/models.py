from django.db import models

class Post(models.Model):
    job_title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    job_description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.job_title


    def snippet(self):
        return self.job_description[:70]+'....'