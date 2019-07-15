from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from revoratebot.models import User


class UsersListView(LoginRequiredMixin, ListView):
    ordering = 'created_at'
    model = User
    template_name = 'admin/users/users_list.html'
    context_object_name = 'users'
