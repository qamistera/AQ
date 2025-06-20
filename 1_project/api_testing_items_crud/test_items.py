

from constant import login_url, items_url, headers_a, auth_data, base_url

class TestItems:
    endpoint = f"{base_url}/api/v1/items/"

    def test_create_item(self, auth_session, item_data):
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (200, 201) , f"Ошибка по размещению {response.status_code}: {response.text}"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None, "Нет ID item"
        assert data.get("title")== item_data["title"], "Ошибка title не совпадают"


    def test_get_item(self, auth_session):
        response = auth_session.get(self.endpoint)
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert "data" in data, "Ключа data нет"
        assert isinstance(data["data"], list), "data не список"
        assert isinstance(data.get("count"), int), "count не ц.ч"

        #items=data.get("data")

        items = data["data"]  # достаём список
        if items:             # если список не пустой
            item = items[0]   # берём первый элемент
            assert "title" in item
            assert "description" in item
            assert "id" in item
            assert "owner_id" in item

    def test_item_pagination(self, auth_session, many_items):
        assert len(many_items) >= 3, "Недостаточно items"
        params1 = {"skip":0, "limit": 2}
        response1= auth_session.get(items_url, params=params1)
        assert response1.status_code == 200, f"Ошибка при передаче параметров {response1.status_code}!=200"
        data1 = response1.json()["data"]
        assert len(data1) == 2, "limit=2 → должно вернуться 2 элемента"

        params2 = {"skip": 2, "limit": 2}
        response2 =auth_session.get(items_url, params=params2)
        assert response2.status_code == 200, f"Ошибка {response2.status_code}!=200"
        data2 = response2.json()["data"]

        if data2:
            assert data1[0]["id"]!=data2[0]["id"], "Пагинация не работает: дублируется."

        ids_page1 = [item["id"] for item in data1]
        ids_page2 = [item["id"] for item in data2]
        assert not any(i in ids_page1 for i in ids_page2)


    def test_put_update_item(self, auth_session, created_item, updated_data):
        item_id = created_item["id"]
        response = auth_session.put(f"{base_url}/api/v1/items/{item_id}", json=updated_data)
        assert response.status_code == 200, f"Ошибка обновления items"

        data = response.json()
        assert data["title"]==updated_data["title"]
        assert data["description"]==updated_data["description"]

    def test_delete_item(self, auth_session, created_item):
        item_id = created_item["id"]
        response= auth_session.delete(f"{base_url}/api/v1/items/{item_id}")
        assert response.status_code == 200, f"Ошибка при удалении: {response.status_code}, {response.text}"

        get_response = auth_session.get(f"{base_url}/api/v1/items/{item_id}")
        assert get_response.status_code in (404, 422), "Ошибка item не был удалён, ещё доступен."






# Commit 28
# Commit 34
# Commit 38
# Commit 43
# Commit 53
# Commit 25
# Commit 73
# Commit 88
