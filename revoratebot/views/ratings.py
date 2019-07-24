from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from core.managers import companies, ratings
from revoratebot.viewmodels import RatingViewModel, CompanyRatingViewModel
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


class BotCompanyRatingView(TemplateView):
    template_name = 'admin/ratings/bot_list.html'

    def get(self, *args, **kwargs):
        self.company_id = kwargs.get('company_id')
        return super().get(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_ratings = ratings.get_ratings_by_compnay(self.company_id)
        view_model_set = [CompanyRatingViewModel(r) for r in company_ratings]
        context['ratings'] = view_model_set
        context['company'] = companies.get_company_by_id(self.company_id)
        return context
    
    
