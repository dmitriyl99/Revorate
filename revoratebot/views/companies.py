from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from revoratebot.models import Company, Department, User



class CompaniesListView(ListView, LoginRequiredMixin):
    template_name = 'admin/companies/companies_list.html'
    context_object_name = 'companies'
    model = Company


class CompanyView(ListView, SingleObjectMixin, LoginRequiredMixin):
    template_name = 'admin/companies/company.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Company.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.object
        return context

    def get_queryset(self):
        return self.object.department_set.all()
