from faker import Faker

faker = Faker()


class UserGenerator:

    @staticmethod
    def generate_user():
        """Генерирует случайные данные для пользователя."""
        return {
            "email": f"{faker.user_name()}.{faker.random_int(min=10, max=999)}+{faker.lexify(text='???')}@{faker.free_email_domain()}",
            "password": faker.password(),
            "name": faker.first_name()
        }
