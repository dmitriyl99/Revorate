from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import  FormView
from revoratebot.models import User
from revoratebot.forms import CreateUserForm
from django.urls import reverse
from django.contrib import messages
from core.managers import companies, users


class UsersListView(LoginRequiredMixin, ListView):
    ordering = 'created_at'
    model = User
    template_name = 'admin/users/users_list.html'
    context_object_name = 'users'


class CreateUserView(LoginRequiredMixin, FormView):
    form_class = CreateUserForm
    template_name = 'admin/users/new_user.html'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone_number = form.cleaned_data['phone_number']
        is_manager = form.cleaned_data['is_manager']
        department = form.cleaned_data['department']
        company = form.cleaned_data['company']
        if not is_manager:
            if not company.isdigit():
                # If user didn't select an exiting company, he wants to create a new one with given name
                user_company = companies.create_company(company)
                user_department = companies.create_department_for_company(department, user_company)
            else:
                user_company = companies.get_company_by_id(company)
                if not user_company:
                    messages.error(self.request, "Указанная компания не существует, проверьте свой выбор")
                    return super().form_invalid(form)
                if not department.isdigit():
                    # If user didn't select an exiting department in exiting company, he wants to create a new one
                    user_department = companies.create_department_for_company(department, user_company)
                else:
                    user_department = companies.get_department_by_id(department)
                    if not user_department:
                        messages.error(self.request, "Указанный отдел компании %s не существует, проверьте свой выбор"
                                       % user_company.name)
                        return super().form_invalid(form)
        else:
            user_department = None
        user = users.create_user(name, phone_number, user_department, is_manager)
        self.object = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('admin_user_created', kwargs={'pk': self.object.id})
