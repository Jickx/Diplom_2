import allure
import requests
from data.urls import Urls


class OrderHelper:

    @staticmethod
    @allure.step("Получение списка доступных ингредиентов")
    def get_ingredients():
        """Получает список доступных ингредиентов."""
        response = requests.get(Urls.INGREDIENTS_URL)
        return response.json()["data"]

    @staticmethod
    @allure.step("Отправка запроса на создание заказа")
    def create_order(ingredients, headers=None):
        """Создает заказ с указанными ингредиентами и заголовками."""
        payload = {"ingredients": ingredients}
        return requests.post(Urls.ORDERS_URL, json=payload, headers=headers)
