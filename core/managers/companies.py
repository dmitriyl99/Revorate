from revoratebot.models import Company, Department


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
