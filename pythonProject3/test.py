import requests
from bs4 import BeautifulSoup

url = 'https://support.avito.ru/tickets/new'

# Ваше имя и email
name = 'Роберт'
email = 'rob.pap@mail.ru'

# Тема обращения
subject = 'Тема обращения'

# Текст обращения
message = 'Текст обращения'

# Отправка запроса
response = requests.post(url, data={
    'utf8': '✓',
    'authenticity_token': '',
    'ticket[name]': name,
    'ticket[email]': email,
    'ticket[subject]': subject,
    'ticket[body]': message,
    'commit': 'Отправить'
})

# Проверка статуса ответа
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    success_message = soup.find('div', {'class': 'alert alert-success'})
    if success_message:
        print(success_message.text.strip())
    else:
        print('Не удалось отправить обращение')
else:
    print('Не удалось отправить обращение')