from django.db import models
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    '''Gives the option to the user to add questions that are up to 200 characters long
    and has another field that adds the date published of that question'''
    def __str__(self):
        return self.question_text
    '''Returns the question text'''

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    '''Gives the option to the user to add multiple choices to a specific question that they selected,
    where those question count as votes when selected and the numbers are being recorded starting from 0'''
    def __str__(self):
        return self.choice_text
    '''Returns the choice text'''