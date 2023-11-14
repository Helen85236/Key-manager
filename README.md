# Key-manager
Менеджер ключей - HTTP сервис для одноразовых секретов наподобие https://onetimesecret.com/.
Он позволяет создать секрет, задать кодовую фразу для его открытия и cгенерировать код, 
по которому можно прочитать секрет только один раз.

# Развертывание проекта:
- python3 -m venv venv
# Активировать виртуальное окружение
- venv/bin/activate
# Установить зависимости проекта, указанные в файле requirements.txt
- pip install -r requirements.txt
# Создать файл .env Записать в файл настройки, как в .env.sample
# Работа с миграциями
- python manage.py makemigrations 
- python manage.py migrate
# Запуск сервера Django
- python manage.py runserver
# Запуск сервера Django c использованием docker-compose
- docker-compose build
- docker-compose up
# Для остановки сервера
- docker-compose down
