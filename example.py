import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, to_lang, from_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(to_lang, from_lang),
    }


    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

link0 = input('Введите путь к файлу с текстом для перевода: ')
link1 = input('Введите путь для сохранения перевода: ')

language0 = input('Введите язык исходного текста: ')
if language0 == 'немецкий':
    to_lang = 'de'
elif language0 == 'испанский':
    to_lang = 'es'
elif language0 == 'французский':
    to_lang = 'fr'
else:
    to_lang = 'en'

language1 = input('Введите язык на который перевести: ')
if language1 == 'английский':
    from_lang = 'en'
else:
    from_lang = 'ru'

with open(link0, 'r', encoding='utf-8') as f:
    text = f.read()
    text = translate_it(text, to_lang, from_lang)
    print(text)

with open(link1, 'w', encoding='utf-8') as f:
    f.write(text)



# requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))
