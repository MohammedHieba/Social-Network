from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import When, Q, Case, Value, Field, CharField, F

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView

from chats.forms import MessageForm
from chats.models import Chat


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
        return '/chats/1'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chat'] = Chat.objects.get(id=self.kwargs.get('id'))
        # print(context.get('form').fields)
        return context

    def form_valid(self, form, *args, **kwargs):
        # form.cleaned_data['chat'] = Chat.objects.get(id=self.kwargs.get('id'))
        # form.cleaned_data['by'] = self.request.user
        # form.save()
        return super().form_valid(form)
