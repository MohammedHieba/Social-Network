from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import When, Q, Case, Value, Field, CharField, F

# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView

from chats.forms import MessageForm
from chats.models import Chat, Message


@method_decorator(login_required, name='dispatch')
class ChatsView(TemplateView):
    template_name = "chats/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chats'] = Chat.objects.filter(Q(first_user=self.request.user) | Q(second_user=self.request.user))
        return context


@method_decorator(login_required, name='dispatch')
class ChatView(FormView):
    template_name = "chats/show.html"
    form_class = MessageForm

    def get_success_url(self):
        return reverse('Chats:show', kwargs={"id": self.kwargs.get('id')})

    def dispatch(self, request, *args, **kwargs):
        chat = Chat.objects.filter(
            Q(first_user=self.request.user) | Q(second_user=self.request.user),
            id=self.kwargs.get('id')).first()
        if not chat:
            return HttpResponseForbidden()
        return super(ChatView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chat'] = Chat.objects.get(id=self.kwargs.get('id'))
        return context

    def form_valid(self, form, *args, **kwargs):
        Message.objects.create(message=form.cleaned_data.get('message'), chat_id=self.kwargs.get('id'),
                               by=self.request.user)
        return super().form_valid(form)


@method_decorator(login_required)
def chat(request, user):
    chat = Chat.objects.search_by_user(request.user, user)
    if not chat.exists():
        Chat.objects.create(first_user=request.user, second_user=user)
    return reverse('Chats:show', kwargs={"id": chat.id})
