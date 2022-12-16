# Задание 19.3.3


# Имя пользователя для логина
username = 'Bot'

# Пароль пользователя для логина
password = 'abc123'

# Данные для добавления нового питомца в магазин
new_pet = {
  "id": 9223372036854606001,
  "category": {
    "id": 0,
    "name": "Собака"
  },
  "name": "Шарик",
  "photoUrls": [
    "None"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Tags"
    }
  ],
  "status": "available"
}

# Данные для обновления питомца
update_pet = {
  "id": 9223372036854606001,
  "category": {
    "id": 0,
    "name": "Собака"
  },
  "name": "Шарик",
  "photoUrls": [
    "None"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Tags"
    }
  ],
  "status": "sold"
}


# Данные для создания заказа на покупку
order = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2022-12-16T15:22:31.704Z",
  "status": "placed",
  "complete": True
}


# Данные для создания пользователей списком
list_users = [
  {
    "id": 111,
    "username": "AAA",
    "firstName": "BBB",
    "lastName": "CCC",
    "email": "ccc@gmal.com",
    "password": "abc",
    "phone": "+76549875026",
    "userStatus": 0
  },
  {
    "id": 222,
    "username": "HHH",
    "firstName": "OOO",
    "lastName": "KKK",
    "email": "kkk2@gmail.com",
    "password": "hok",
    "phone": "+78527539545",
    "userStatus": 0
  }
]


# Данные для создания нового user
created_user = {
  "id": 0,
  "username": "GGG",
  "firstName": "CCC",
  "lastName": "DDD",
  "email": "ddd@gmail.com",
  "password": "gcd",
  "phone": "+79859634275",
  "userStatus": 0
}

# Данные для обновления user
updated_user = {
  "id": 0,
  "username": "GG1",
  "firstName": "CC1",
  "lastName": "DD1",
  "email": "dd!@gmail.com",
  "password": "123",
  "phone": "+79859634275",
  "userStatus": 0
}

# from datetime import datetime
# "shipDate": f"{datetime.now()}",
# что за формат вывода даты и времени доработать
# print(datetime.now())
# print(order)

