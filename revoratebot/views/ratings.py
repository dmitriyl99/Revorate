from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from core.managers import companies
from revoratebot.viewmodels import RatingViewModel
from revoratebot.models import Rating


class RatingsListView(LoginRequiredMixin, ListView):
    template_name = 'admin/ratings/list.html'
    model = Rating
    ordering = 'created_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        view_models_set = [RatingViewModel(r) for r in queryset]
        context["ratings"] = view_models_set
        context['companies'] = companies.get_all_companies()
        context['departments'] = companies.get_all_departments()
        return context
    
