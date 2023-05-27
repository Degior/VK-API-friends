import requests
from config import API_KEY

user_id = 'user_id'

response = requests.get(
    f'https://api.vk.com/method/friends.get?user_id={user_id}&fields=first_name,last_name&access_token={API_KEY}&v=5.131')
data = response.json()

if 'response' in data:
    friends = data['response']['items']
    for friend in friends:
        print(friend['first_name'], friend['last_name'])
else:
    print('Ошибка при получении списка друзей:', data)
