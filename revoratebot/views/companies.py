from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from revoratebot.models import Company

from core.managers import companies


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


class CreateCompanyView(CreateView, LoginRequiredMixin):
    model = Company
    fields = ['name']
    template_name = 'admin/companies/new_company.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        companies.create_default_company_departments(self.object)
        messages.success(self.request, "Создана компания %s вместе со стандартными отделами Dispatchers, Update, "
                                       "Safety, Fleet, Trailer" % form.cleaned_data['name'])
        return result
