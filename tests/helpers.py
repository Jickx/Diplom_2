from faker import Faker

faker = Faker()

def generate_user_data():
    """Генерирует случайные данные для пользователя."""
    return {
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.first_name()
    }
