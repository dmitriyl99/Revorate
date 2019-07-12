from django.urls import path
from .views import index, companies

urlpatterns = [
    path('', index.IndexView.as_view(), name='admin_home'),
    path('companies/', companies.CompaniesListView.as_view(), name='admin_companies_list'),
    path('companies/<int:pk>', companies.CompanyView.as_view(), name='admin_company')
]