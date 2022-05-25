from django.db import models

class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    
    question  = models.CharField(max_length=200)
    ans       = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.question + ' - ' + self.ans



class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    response = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.response


