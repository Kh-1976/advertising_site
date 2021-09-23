import requests

HOST = 'http://127.0.0.1:5000'

resp_get = requests.get(f'{HOST}/advertisings/1')

'''
resp_post = requests.post(f'{HOST}/advertisings/', json={
    'title': 'Телевизор Sony',
    'description': 'Б.У, 3000 руб.',
    'date_of_creation': '05.07.2021',
    'owner': 'Смирнов'
})
'''
#resp_delete = requests.delete(f'{HOST}/advertisings/1')

print(resp_get.status_code)
print(resp_get.json())

#print(resp_post.status_code)
#print(resp_post.json())

#print(resp_delete.status_code)
#print(resp_delete.json())