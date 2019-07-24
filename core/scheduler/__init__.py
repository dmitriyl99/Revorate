"""
Package for scheduling tasks
"""
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


_scheduler = BackgroundScheduler()


def init():
    """
    Init the scheduler
    """
    _scheduler.start()


def add_timer_for_comment(chat_id, rating_id: int, func):
    trigger = IntervalTrigger(minutes=1)
    _scheduler.add_job(func, trigger, [chat_id, rating_id], 
                       id='rating_{}'.format(rating_id), replace_existing=True)


def remove_timer_for_comment(rating_id: int):
    _scheduler.remove_job('rating_{}'.format(rating_id))
