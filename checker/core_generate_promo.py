from json import load, dumps
from string import ascii_letters, digits, punctuation
from secrets import choice

def check_promo(promo_code, data):
    '''
    Проверка промо-кода на сущуствование в файле
    '''
    fl = False
    for item in data:
        item = dict(item)
        fl = promo_code in item['promo'] 
        if fl:
            promo_code = generate_promo()
            promo_code = check_promo(promo_code, data)
    if not fl:
        return promo_code

def get_json_promo(quantity, name, path = 'checker/data_promo.json'):
    '''
    Генерация кода в файл
    '''
    list_promo = []
    context = {}
    data = False

    #Проверка кода
    try:
        with open(path, 'r') as f:
            data = load(f)
    except(Exception):
        pass

    for _ in range(quantity):
        promo_code = generate_promo()

        if data:
            promo_code = check_promo(promo_code, data)
        
        list_promo.append(promo_code)

    # Создание или вставка следующих кодов
    if list_promo:
        try:
            context["name"] = name
            context["promo"] = list_promo
            with open(path, 'r+') as f:
                if data:
                    text = ',' + dumps(context)
                    f.seek(0, 2)
                    f.seek(f.tell()-1, 0)
                    f.write(text)
                    f.seek(0, 2)
                    f.write(']')

        except(FileNotFoundError):
            with open(path, 'w') as f:
                text = dumps([context])
                f.write(text)

#Генератор случайных символов
def generate_promo():
    alphabet = ascii_letters + digits + punctuation
    return ''.join(choice(alphabet) for i in range(8))