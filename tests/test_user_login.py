from http import HTTPStatus

import requests

from data.messages import EMAIL_OR_PASSWORD_ARE_INCORRECT
from data.urls import Urls
from helpers.user_generator import UserGenerator


class TestUserLogin:
    """Тесты для проверки функциональности авторизации пользователя через API."""

    def test_login_registered_user_success(self, registered_user):
        """Проверка успешной авторизации зарегистрированного пользователя."""
        creds = {
            "email": registered_user["payload"]["email"],
            "password": registered_user["payload"]["password"],
        }

        response = requests.post(Urls.LOGIN_USER_URL, json=creds)
        assert response.status_code == HTTPStatus.OK
        assert response.json()["success"] is True

    def test_login_incorrect_login_and_password(self):
        """Проверка авторизации с некорректными учетными данными."""
        incorrect_user = UserGenerator.generate_user()

        response = requests.post(Urls.LOGIN_USER_URL, json=incorrect_user)
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json()["success"] is False
        assert response.json()["message"] == EMAIL_OR_PASSWORD_ARE_INCORRECT
