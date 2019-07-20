"""
Module for manage ratings
"""
from revoratebot.models import Rating, User


def create_rating(from_user: User, to_user: User, value: int, comment: str) -> Rating:
    """
    Create a new rating from user to user
    :param from_user: from User
    :param to_user: to User
    :param value: estimate value
    :param comment: comment
    :return: created rating object
    """
    from_id = from_user.id
    to_id = to_user.id
    company_id = to_user.department.company_id
    department_id = to_user.department_id
    new_rating = Rating(to_id=to_id, from_id=from_id, value=value, comment=comment, company_id=company_id, department_id=department_id)
    new_rating.save()
    return new_rating
