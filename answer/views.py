from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views.generic import ListView, FormView, CreateView

from answer.models import Question, Answer
from answer.forms import CreateUserQuestionForm, CreateAnswerForm


class UserListView(ListView):
    model = User
    template_name = "home.html"
    context_object_name = 'users'


class UserQuestionListView(ListView):
    model = Question

    def get(self, request, *args, **kwargs):
        self.user = User.objects.get(pk=self.kwargs.get('user_pk'))

        return super(UserQuestionListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(UserQuestionListView, self).get_context_data(**kwargs)

        current_user = User.objects.get(pk=self.kwargs.get('user_pk'))
        ctx['current_user'] = current_user
        ctx['add_question_form'] = CreateUserQuestionForm()

        return ctx

    def get_queryset(self):
        qs = super(UserQuestionListView, self).get_queryset()

        return qs.filter(user_to=self.user)


class CreateUserQuestion(CreateView):
    model = Question
    form_class = CreateUserQuestionForm

    def form_valid(self, form):

        form.instance.user_from = self.request.user
        form.instance.user_to = User.objects.get(pk=self.kwargs.get('user_pk'))
        return super(CreateUserQuestion, self).form_valid(form)

    def get_success_url(self):
        return reverse('user_questions', kwargs={'user_pk': self.kwargs.get('user_pk')})


class CreateAnswer(CreateView):
    model = Answer
    form_class = CreateAnswerForm
    template_name = 'answer/answer.html'

    def form_valid(self, form):
        form.instance.question = Question.objects.get(pk=self.kwargs.get('pk'))
        return super(CreateAnswer, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CreateAnswer, self).get_context_data(**kwargs)

        current_user = User.objects.get(pk=self.kwargs.get('user_pk'))
        question = Question.objects.get(pk=self.kwargs.get('pk'))
        ctx['current_user'] = current_user
        ctx['question'] = question

        return ctx

    def get_success_url(self):
        return reverse('user_questions', kwargs={'user_pk': self.kwargs.get('user_pk')})
