base_url = "https://api.pomidor-stage.ru"
login_url= f"{base_url}/api/v1/login/access-token"
items_url= f"{base_url}/api/v1/items/"

headers_a = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}


auth_data = {
    "grant_type": "password",
    "username": "prime@mail.ru",
    "password": "123456789",
    "scope":"",
    "client_id": "",
    "client_secret":""
}


api_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
