from django.db import models

class Survey(models.Model):
    question = models.TextField()
    opt1 = models.CharField(max_length=100)
    opt2 = models.CharField(max_length=100)
    opt3 = models.CharField(max_length=100)
    opt4 = models.CharField(max_length=100)




class Answer(models.Model):
    question = models.ForeignKey(Survey, on_delete=models.CASCADE)
    ans = models.CharField(max_length=100)

