from django.db import models

#Question model

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    publishing_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text
    
#Choice model

class Choice(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
