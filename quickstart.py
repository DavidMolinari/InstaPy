""" Quickstart script for InstaPy usage """
import sys

# imports
from instapy import InstaPy
from instapy import smart_run
import string
from instapy import set_workspace

# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)
userNames = sys.argv[1].split(',')
f = open("cred.ini", "r")

user_name = f.readline().strip()
user_password = f.readline().strip()


# get an InstaPy session!
session = InstaPy(username=user_name, password=user_password)


with smart_run(session, userNames):
    # general settings
    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                 sleepyhead=True, stochastic_flow=True, notify_me=True,
                                 peak_likes_hourly=47,
                                 peak_likes_daily=471,
                                 peak_comments_hourly=12,
                                 peak_comments_daily=167,
                                 peak_follows_hourly=36,
                                 peak_follows_daily=264,
                                 peak_unfollows_hourly=29,
                                 peak_unfollows_daily=332,
                                 peak_server_calls_hourly=621,
                                 peak_server_calls_daily=3762)
    session.set_skip_users(skip_private=True,
                           skip_no_profile_pic=False,
                           skip_business=True,
                           business_percentage=100)

    # SETTINGS
    session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
    session.set_do_follow(enabled=True, percentage=70)
    session.set_do_like(enabled=True, percentage=70)
    session.set_do_comment(enabled=False, percentage=80)
    session.set_do_story(enabled=True, percentage=70, simulate=False)

    # ACTIONS


    session.follow_likers(userNames, photos_grab_amount=2, follow_likers_per_photo=3, randomize=True,
                          sleep_delay=600, interact=True)

