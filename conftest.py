from http import HTTPStatus

import pytest
import requests
from helpers.user_generator import UserGenerator
from data.urls import Urls


@pytest.fixture(scope="function")
def user():
    """
    Фикстура для генерации данных пользователя и очистки после теста.

    Генерирует данные пользователя, возвращает их в тест.
    После выполнения теста выполняет очистку: авторизуется и удаляет пользователя.
    """
    payload = UserGenerator.generate_user()
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


@pytest.fixture(scope="function")
def registered_user():
    """
    Фикстура для создания и регистрации пользователя в системе.

    Создает пользователя через API, возвращает данные пользователя и токен доступа.
    После выполнения теста удаляет пользователя из системы.
    """
    payload = UserGenerator.generate_user()
    response = requests.post(Urls.CREATE_USER_URL, json=payload)
    assert response.status_code == HTTPStatus.OK
    access_token = response.json().get("accessToken")

    yield {"payload": payload, "access_token": access_token}

    if access_token:
        try:
            requests.delete(Urls.USER_DATA_URL, headers={"Authorization": access_token})
        except requests.exceptions.RequestException:
            pass
