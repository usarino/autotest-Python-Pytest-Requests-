"""
Samoilenko (Kolorado) autotest Python + Pytest + Requests
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
header = {'Content-Type': 'application/json','trainer_token': '0cd1e67cdb55b3ed2dff15384d3eb220'}
body = {
    "name": "generate",
    "photo": "generate"
}
body2 = {
    "pokemon_id": "29642",
    "name": "SVETLAN",
    "photo": "https://dolnikov.ru/pokemons/albums/888.png"
}
body3 = {
    "pokemon_id": "29642"
}
# response = requests.post(url=f'{URL}/trainers/reg', json=body, headers=header, timeout=5)
# print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')
# print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

response = requests.get(url=f'{URL}/trainers', params={'level': 5}, timeout=5)
print(f'Статус код: {response.status_code}.')

"""
1.Создание покемона
"""
response = requests.post(url=f'{URL}/pokemons', json=body, headers=header, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}, Номер покемона: {response.json()["id"]}')

"""
2.Смена имени покемона
"""
response = requests.put(url=f'{URL}/pokemons', json=body2, headers=header, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')

"""
3.Поймать покемона в покебол
"""
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body3, headers=header, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')





# a = 5
# b = 7
# sum = a + b

# if sum == 12:
#     print('OK')
# else:
#     print('BAD')
# # print(f'Результат сложения: {sum}') - f-стринга