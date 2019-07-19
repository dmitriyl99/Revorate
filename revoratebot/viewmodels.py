from revoratebot.models import Rating
from core.managers import users


class RatingViewModel:
    def __init__(self, rating: Rating):
        self.from_user = users.get_by_id(rating.from_id)
        self.to_user = users.get_by_id(rating.to_id)
        self.value = rating.value
        self.created_at = rating.created_at
        self.comment = rating.comment
