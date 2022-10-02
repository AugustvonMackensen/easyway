
# Create your models here.
from django.db import models
from users.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


view = models.PositiveBigIntegerField(default= 0)

def update_view(self):
    self.view = self.view + 1
    self.save()