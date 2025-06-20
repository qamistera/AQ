#test_2booker.py
import  requests

from hw2.conftest import booking_data
from hw2.constant import base_url


class TestBooking:

    def test_ping_get(self):
        ping_status = requests.get(f"{base_url}/ping")
        assert ping_status.status_code == 201, f"Ошибка сервера {ping_status.status_code}!=200"


    def test_create_check_delete_(self, booking_data, auth_session):

        create_booking = auth_session.post(f"{base_url}/booking", json=booking_data) #POST-запрос
        assert create_booking.status_code == 200, f"Ошибка при создании букинга {create_booking.status_code} != 200"
        booking_id = create_booking.json().get("bookingid")   # GET-запрос
        assert booking_id is not None , f"ID:{booking_id}  букинга не найден."

        assert create_booking.json()["booking"]["firstname"]==booking_data["firstname"], "Имя не совпадает с заданным"
        assert create_booking.json()["booking"]["lastname"]==booking_data["lastname"], "Фамилия не совпадает с заданной"
        assert create_booking.json()["booking"]["totalprice"]== booking_data["totalprice"], "Цена не совпадает с заданной"
        assert create_booking.json()["booking"]["additionalneeds"] == booking_data["additionalneeds"], "Допы ошибка."

        get_response_id = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert get_response_id.status_code ==200, f"Букинг с таким ID:{booking_id} не найден."

        delete_response_id_del = auth_session.delete(f"{base_url}/booking/{booking_id}")  # DELETE-запрос
        assert delete_response_id_del.status_code == 201, f"Ошибка удаления букинга с ID {booking_id}"

        check_delete_id_response = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert check_delete_id_response.status_code== 404, f"Букинг с ID {booking_id} не удален."



    def test_put_updated_get(self, updated_data, session_and_booking_id):
        auth_session, booking_id = session_and_booking_id  # распаковываем два значения из фикстуры created_booking

        put_resp = auth_session.put(f"{base_url}/booking/{booking_id}", json=updated_data) # PUT-запрос
        assert put_resp.status_code == 200, f"Изменение не произошло {put_resp.status_code}!=200"

        for key in ["firstname", "lastname", "totalprice", "additionalneeds"]:
            assert put_resp.json()[key]==updated_data[key], f"{key} не совпадают."

        assert put_resp.json()["bookingdates"]["checkin"]==updated_data["bookingdates"]["checkin"], f'Дата {put_resp.json()["bookingdates"]["checkin"]} не совпадает c {updated_data["bookingdates"]["checkin"]}.'
        assert put_resp.json()["bookingdates"]["checkout"] == updated_data["bookingdates"]["checkout"] , f'Дата {put_resp.json()["bookingdates"]["checkout"]} не совпадает c {updated_data["bookingdates"]["checkout"]}.'

        del_resp = auth_session.delete(f"{base_url}/booking/{booking_id}")
        assert del_resp.status_code==201, f"Ошибка удаления после обновления ID {booking_id} через PUT."

        del_check=auth_session.get(f"{base_url}/bookining/{booking_id}")
        assert del_check.status_code==404, f"Букинг с ID {booking_id} не удален."


    def test_patch(self, patch_data, session_and_booking_id):
        auth_session, booking_id = session_and_booking_id

        patch_resp = auth_session.patch(f"{base_url}/booking/{booking_id}", json = patch_data)
        assert patch_resp.status_code == 200, f"Ошибка частичного изменения {patch_resp.status_code}!=200"
        for key in ["firstname", "lastname"]:
            assert patch_resp.json()[key] == patch_data[key], f"Ошибка строкм {key} не совпадают после PATCH"

        patch_resp = auth_session.delete(f"{base_url}/booking/{booking_id}")
        assert patch_resp.status_code == 201, f"Ошибка удаления ID {booking_id} , {patch_resp.status_code}!=200."

        patch_resp=auth_session.get(f"{base_url}/bookking/{booking_id}")
        assert patch_resp.status_code == 404, f"Букинг с ID {booking_id} не удален после PATCH."
