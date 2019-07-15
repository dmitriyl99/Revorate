from django.urls import path
from .views import index, companies, departments, users

urlpatterns = [
    path('', index.IndexView.as_view(), name='admin_home'),
    path('companies/', companies.CompaniesListView.as_view(), name='admin_companies_list'),
    path('companies/<int:pk>', companies.CompanyView.as_view(), name='admin_company'),
    path('companies/create', companies.CreateCompanyView.as_view(), name='admin_new_company'),
    path('companies/<int:pk>/delete', companies.DeleteCompanyView.as_view(), name='admin_delete_company'),
    path('companies/<int:pk>/edit', companies.UpdateCompanyView.as_view(), name='admin_edit_company'),
    path('companies/<int:company_id>/departments/create', departments.CreateDepartmentView.as_view(), name='admin_new_department'),
    path('companies/<int:company_id>/departments/<int:pk>', departments.EditDepartmentView.as_view(), name='admin_edit_department'),
    path('companies/<int:company_id>/departments/<int:pk>/delete', departments.DeleteDepartmentView.as_view(), name='admin_delete_department'),
    path('users/', users.UsersListView.as_view(), name='admin_users')
]