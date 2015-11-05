from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    user_from = models.ForeignKey(User, related_name='questions_from')
    user_to = models.ForeignKey(User, related_name='questions_to')

    question = models.TextField(max_length=300)

    date_question = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')

    answer = models.TextField(max_length=600, null=True, blank=True)

    date_answer = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer

