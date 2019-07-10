"""
Module for sos signals management
"""
from revoratebot.models import SosSignal, User


def create_sos(user: User, latitude, longitude):
    """
    Create new sos signal object
    :param user: Sender
    :param latitude: Latitude
    :param longitude: Longitude
    :return: created sos signal object
    """
    new_sos_signal = SosSignal(user=user, location_lat=latitude, location_lon=longitude)
    new_sos_signal.save()
    return new_sos_signal
