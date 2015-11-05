from django import forms

from answer.models import Question, Answer


class CreateUserQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question']


class CreateAnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['answer']
