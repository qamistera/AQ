
import  requests



class TestBooking:
    base_url = "https://restful-booker.herokuapp.com"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    json ={"username" : "admin", "password" : "password123"}

    def get_token(self):
        response = (requests.post(f"{self.base_url}/auth",headers=self.headers,json=self.json))
        assert response.status_code == 200,f"Авторизация не удалась: {response.status_code} != 200"
        token = response.json().get("token")
        return token

    def test_create_check_delete_(self):
        session = requests.Session()
        session.headers.update(self.headers)

        token = self.get_token()
        session.headers.update({"Cookie": f"token={token}"})

        booking_data ={
            "firstname" : "Andrew",
            "lastname" : "Mon",
            "totalprice" : 100000,
            "depositpaid" : True,
            "bookingdates" : {
                "checkin": "2025-05-17",
                "checkout": "2025-05-30"
            },
            "additionalneeds": "Colla"
        }

        create_response = session.post(f"{self.base_url}/booking", json=booking_data)
        assert create_response.status_code == 200, f"Ошибка букинга {create_response.status_code} != 200"
        booking_id = create_response.json().get("bookingid")
        assert booking_id is not None , f"ID:{booking_id}  букинга не найден."

        assert create_response.json()["booking"]["firstname"]=="Andrew", "Имя не совпадает с заданным"
        assert create_response.json()["booking"]["lastname"]=="Mon", "Фамилия не совпадает с заданной"
        assert create_response.json()["booking"]["totalprice"]== 100000, "Цена не совпадает с заданной"
        assert create_response.json()["booking"]["additionalneeds"] == "Colla", "Допы ошибка."

        get_response = session.get(f"{self.base_url}/booking/{booking_id}")
        assert get_response.status_code ==200, f"Букинг с таким ID:{booking_id} не найден."

        delete_response = session.delete(f"{self.base_url}/booking/{booking_id}")
        assert delete_response.status_code == 201, f"Ошибка удаления букинга с ID {booking_id}"

        check_delete_response = session.get(f"{self.base_url}/booking/{booking_id}")
        assert check_delete_response.status_code== 404, f"Букинг с ID {booking_id} не удален."


# Commit 9
# Commit 10
# Commit 22
# Commit 35
# Commit 41
# Commit 46
# Commit 75
# Commit 2
# Commit 14
# Commit 28
# Commit 32
# Commit 35
# Commit 51
# Commit 52
# Commit 56
# Commit 60
# Commit 74
# Commit 89
# Commit 90
