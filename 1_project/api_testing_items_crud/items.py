import requests


base_url = "https://api.pomidor-stage.ru"
login_url= f"{base_url}/api/v1/login/access-token"
items_url= f"{base_url}/api/v1/items/"

headers = {
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

def get_auth_token():
    response= requests.post(login_url, headers=headers, data= auth_data)
    assert response.status_code==200, f"Ошибка получения токен получен {response.status_code}!=200 "
    return response.json().get("access_token")

def create_item(title, description, token):
    headers_auth={
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    data_item= {
        "title": "title",
        "description": "description"

    }

    response= requests.post(items_url, headers= headers_auth, json=data_item)
    assert response.status_code in (200, 201), f"Ошибка items код: {response.status_code}"
    item =response.json()
    print(f"{item['title']} (ID: {item['id']})")

if __name__=="__main__":
        token =get_auth_token()
        for i in range(20):
            create_item(f"Test Item {i}", f"Description {i}", token)# Commit 2
# Commit 3
# Commit 11
# Commit 20
# Commit 24
# Commit 25
# Commit 27
# Commit 40
# Commit 44
# Commit 47
# Commit 76
# Commit 17
# Commit 19
# Commit 24
# Commit 26
# Commit 39
# Commit 48
# Commit 67
# Commit 92
# Commit 95
# Commit 103
