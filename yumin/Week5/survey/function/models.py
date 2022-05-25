from django.db import models

# Create your models here.
class Survey(models.Model):
    surveyIdx = models.AutoField(primary_key=True)
    question = models.TextField()

    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    ans4 = models.TextField(null=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answerIdx = models.AutoField(primary_key=True)
    choice = models.TextField()
