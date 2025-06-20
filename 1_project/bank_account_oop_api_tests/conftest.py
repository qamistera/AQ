#conftest.py
from datetime import datetime, timedelta

from faker import Faker
import pytest
import requests


from hw2.constant import headers, base_url, json

fake=Faker()

@pytest.fixture(scope="session")
def auth_session():

    session=requests.Session()
    session.headers.update(headers)

    auth_response = session.post(f"{base_url}/auth", json=json)
    assert auth_response.status_code ==200, f"Ошибка {auth_response.status_code} != 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе."

    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture()
def booking_data():
    # Случайное количество дней от сегодня до checkin
    checkin_offset = fake.random_int(min=2, max=10)
    checkin_date = datetime.today() + timedelta(days=checkin_offset)

    # Случайное количество дней проживания (1–14 дней)
    stay_length = fake.random_int(min=1, max=14)
    checkout_date = checkin_date + timedelta(days=stay_length)

    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": checkin_date.strftime("%Y-%m-%d"),
            "checkout": checkout_date.strftime("%Y-%m-%d")
        },
        "additionalneeds": fake.text(max_nb_chars=10)
    }

@pytest.fixture()
def session_and_booking_id(auth_session, booking_data):

    create_response = auth_session.post(f'{base_url}/booking', json=booking_data)
    assert create_response.status_code==200, f"Создание брони ошибка{create_response.status_code}!= 200"

    booking_id = create_response.json().get("bookingid")
    assert booking_id is not None , f"Ошибка bookingid не получен"

    return auth_session, booking_id


@pytest.fixture()
def updated_data():
    # Случайное количество дней от сегодня до checkin
    checkin_offset_put = fake.random_int(min=2, max=10)
    checkin_date = datetime.today() + timedelta(days=checkin_offset_put)

    # Случайное количество дней проживания (1–14 дней)
    stay_length_put = fake.random_int(min=1, max=14)
    checkout_date = checkin_date + timedelta(days=stay_length_put)

    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": checkin_date.strftime("%Y-%m-%d"),
            "checkout": checkout_date.strftime("%Y-%m-%d")
        },
        "additionalneeds": fake.text(max_nb_chars=10)
    }

@pytest.fixture()
def patch_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name()
    }

