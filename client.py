import requests


host = "http://127.0.0.1:5000"

# Создаем пользователя
# res = requests.post(f"{host}/owner-post/", json={
#     "email": "email@mail.ru",
#     "password": "password554564((@#))",
# })

# Логинимся
# res = requests.post(f"{host}/login/", json={
#     "email": "email@mail.ru",
#     "password": "password554564((@#))",
# })

# Создаем объявление
res = requests.post(f"{host}/adv-post/", json={
    "title": "title",
    "description": "advertisement_test",
    "token": '4e5bad0c-f3ca-47ca-b103-fd05aebc1322'
})

# Получаем объявление
# res = requests.get(f"{host}/adv-get/", json={
#     "adv": 2,
# })

# Получаем объявление
# res = requests.delete(f"{host}/adv-delete/", json={
#     "ad": 3,
#     "owner": 2
# })

print(res.text)