import pytest
import requests
from urls import Urls


class TestUserCreation:

    def test_create_unique_user_success(self, user_data):
        """Тест успешного создания уникального пользователя."""
        response = requests.post(Urls.CREATE_USER_URL, json=user_data)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    def test_create_existing_user_error(self, user_data):
        """Тест ошибки при создании пользователя, который уже существует."""
        requests.post(Urls.CREATE_USER_URL, json=user_data)

        response = requests.post(Urls.CREATE_USER_URL, json=user_data)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_required_field_error(self, user_data, missing_field):
        """Тест ошибки при отсутствии одного из обязательных полей."""
        user_data.pop(missing_field)
        response = requests.post(Urls.CREATE_USER_URL, json=user_data)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"
