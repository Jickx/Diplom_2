import requests

from data.urls import Urls


class UserHelper:

    @staticmethod
    def create_user(user_data):
        return requests.post(Urls.CREATE_USER_URL, json=user_data)
