# Сайт для публикации новостей из мира IT

*Стек технологий:*

- Python
- Django
- Bootstrap

### Как развернуть проект?

Склонировать репозиторий:

```
git clone git@github.com:LeoNefesch/vsc_project.git
```
Зайти в рабочую директорию:

```
cd vsc_project/
```
Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
