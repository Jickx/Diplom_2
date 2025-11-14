import pytest
import requests
from helpers import generate_user_data
from urls import Urls


@pytest.fixture(scope="function")
def user_data():
    """Фикстура для генерации данных пользователя и очистки после теста."""
    payload = generate_user_data()
    access_token = None

    yield payload

    login_payload = {"email": payload.get("email"), "password": payload.get("password")}
    try:
        login_response = requests.post(Urls.LOGIN_USER_URL, json=login_payload)
        if login_response.status_code == 200:
            access_token = login_response.json().get("accessToken")
    except requests.exceptions.RequestException:
        pass

    if access_token:
        try:
            headers = {"Authorization": access_token}
            requests.delete(Urls.USER_DATA_URL, headers=headers)
        except requests.exceptions.RequestException:
            pass
