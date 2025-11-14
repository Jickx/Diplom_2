import pytest
import requests

from data.messages import USER_ALREADY_EXISTS, REQUIRED_FIELDS_ERROR
from data.urls import Urls
from http import HTTPStatus

from helpers.user_helper import UserHelper


class TestUserCreation:

    def test_create_unique_user_success(self, user):
        """Тест успешного создания уникального пользователя."""
        response = UserHelper.create_user(user)

        assert response.status_code == HTTPStatus.OK
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    def test_create_existing_user_error(self, user):
        """Тест ошибки при создании пользователя, который уже существует."""
        requests.post(Urls.CREATE_USER_URL, json=user)

        response = requests.post(Urls.CREATE_USER_URL, json=user)

        assert response.status_code == HTTPStatus.FORBIDDEN
        assert response.json()["success"] is False
        assert response.json()["message"] == USER_ALREADY_EXISTS

    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_required_field_error(self, user, missing_field):
        """Тест ошибки при отсутствии одного из обязательных полей."""
        user.pop(missing_field)
        response = requests.post(Urls.CREATE_USER_URL, json=user)

        assert response.status_code == HTTPStatus.FORBIDDEN
        assert response.json()["success"] is False
        assert response.json()["message"] == REQUIRED_FIELDS_ERROR
