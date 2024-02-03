"""
Kolorado autotest
"""
import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
header = {'Content-Type': 'application/json'}

def test_get_trainers_LEVEL():
    """
    1. autotest
    """
    response = requests.get(url=f'{URL}/trainers', params={'level': 5}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

CASES = [
    (4655, 'Zimbabve', 'Pupsen'),
    (3462, 'Toronto', 'Пикачу'),
]

@pytest.mark.parametrize('id, city, trainer_name', CASES)
def test_get_trainers_ID(id, city, trainer_name):
    """
    1.1 autotest - Тест на получение 2х покемонов из БД, в т.ч. моего ПИкачу
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': id}, timeout=5)
    assert response.json()['city'] == city, '888'
    assert response.json()['trainer_name'] == trainer_name, '888'


# body = {
#     "trainer_token": "0cd1e67cdb55b3ed2dff15384d3eb220",
#     "email": "usarino@yandex.ru",
#     "password": "Iloveqa1"
# }

# response = requests.post(url=f'{URL}/trainers/reg', json=body, headers=header, timeout=5)
# print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')
# print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

# response = requests.get(url=f'{URL}/trainers', params={'level': 5}, timeout=5)
# print(f'Статус код: {response.status_code}.')
