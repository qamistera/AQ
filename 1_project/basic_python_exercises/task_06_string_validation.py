# Валидация имени, email и телефона
def validate_login(name: str, email: str, phone: str) -> str:
    if not name or "@" not in email or len(phone) != 10:
        return "Ошибка ввода. Проверьте данные."
    return f"Пользователь {name} успешно зарегистрирован."

# Проверка надёжности пароля
def password_strength(password: str) -> str:
    if len(password) < 6:
        return "Слабый пароль"
    if not any(c.isdigit() for c in password):
        return "Добавьте цифры для надёжности"
    if not any(c.isupper() for c in password):
        return "Добавьте заглавные буквы"
    return "Надёжный пароль"