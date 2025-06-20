import pytest
import requests
from faker import Faker
from constant import login_url, items_url, headers_a, auth_data, api_headers, base_url

fake = Faker('ru_RU')

@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    response= session.post(f"{base_url}/api/v1/login/access-token", data= auth_data, headers=headers_a)
    assert response.status_code == 200, f"Auth failed: {response.status_code}, {response.text}"

    token = response.json().get("access_token")
    assert token is not None, "Токен не получен: access_token отсутствует в ответе"

    session.headers.update(api_headers)
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session


@pytest.fixture()
def item_data():
    return{
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=10)
    }

@pytest.fixture()
def created_item(item_data,auth_session):
    response = auth_session.post(items_url, json=item_data)
    assert response.status_code in (200, 201), "Ошибка создания items фикст."

    return response.json()
#item_id = created_item["id"]


@pytest.fixture()
def many_items_0(auth_session):
    items = [auth_session.post(items_url,json={"title": f"Item {i}", "description": f"Desc {i}"}).json()for i in range(3)]
    return items

@pytest.fixture()
def many_items(auth_session):
    def create(i):
        resp = auth_session.post(items_url, json={"title": f"Item {i}", "description": f"Desc {i}"})
        assert resp.status_code==200, "Ошибка создания итемсов фикст."
        return resp.json()
    return [create(i) for i in range(3)]

@pytest.fixture()
def updated_data():
    return {
        "title": fake.word(),
        "description": fake.sentence(nb_words=10)
    }
