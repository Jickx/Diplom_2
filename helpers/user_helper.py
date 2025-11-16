import allure
import requests

from data.urls import Urls


class UserHelper:

    @staticmethod
    @allure.step("Отправка запроса на создание пользователя")
    def create_user(user_data):
        return requests.post(Urls.CREATE_USER_URL, json=user_data)
