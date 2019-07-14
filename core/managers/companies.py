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
