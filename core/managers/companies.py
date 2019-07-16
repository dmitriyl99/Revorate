from revoratebot.models import Company, Department
from typing import Optional


def create_default_company_departments(company: Company):
    dispatchers = Department(name='Dispatchers', company=company)
    dispatchers.save()
    updaters = Department(name='Update', company=company)
    updaters.save()
    safety = Department(name='Safety', company=company)
    safety.save()
    fleet = Department(name='Fleet', company=company)
    fleet.save()
    trailer = Department(name='Trailer', company=company)
    trailer.save()


def get_company_by_id(company_id) -> Optional[Company]:
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        return None
    return company


def create_company(name: str) -> Company:
    company = Company(name=name)
    company.save()
    create_default_company_departments(company)
    return company


def create_department_for_company(department_name: str, company: Company) -> Department:
    department = Department(name=department_name, company=company)
    department.save()
    return department


def get_department_by_id(department_id: int) -> Optional[Department]:
    try:
        department = Department.objects.get(pk=department_id)
    except Department.DoesNotExist:
        return None
    return department