# Generate_promo

## Как запустить на локальном компьютере?

#### Загрузите код 
##### Код тестировался на python 3.7.4, Windows 10 
#### Рекомендую создать виртуальное окружение для python , не забудь установить Django!:
```
python -m venv venv
```

#### Активация окружения Python/Django:

Если создавалось вирт.окружение
```
source ./venv/bin/activate 
```
```
pip install django
```

Сгенерируйте промокоды(команду можно проводить сколько угодно раз)
```
python generate_promo.py amount=10 group='name'
```

Запустите сервер
```
python generate_promo.py start
```

Активная ссылка: 
http://127.0.0.1:8000/
