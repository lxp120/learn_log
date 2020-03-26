from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # if len(str(text)) < 50:
    #     text = text
    # else:
    #     text = text[:50] + "..."

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + ".."
