import requests, config

def translate_yandex(text, lang):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = config.yandex_translate_API_key
    r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
    text_in_squares = r.text.split(",")[2].split(":")[1]
    s = text_in_squares.replace('["', '')
    result = s.replace('"]}', '')
    return result