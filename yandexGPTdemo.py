import requests
#from curl_cffi import requests
import json

#Ниже идет взаимодействие с gpt.
#В переменную temp передается словарь.
#В файле run.py один из примеров его организации.
#Во всяком случае - конструкция файла должна оставаться похожей,
#т.е это простой словарь (dict) с key:text, где text - str(строка)
#
#Если решите делать несколько обращений к gpt, 
#просто копируете функцию def GENERATE_1 и меняете _1 на, например, _2 и т.д
#
#"role": "system" -- это легенда для gpt, т.е кем или чем она является
#"role": "user" -- это сам запрос от пользователя
#Ты опытный проффессиональный рекламщик



def GENERATE_1(temp):
    prompt = {
        "modelUri": "gpt://b1g7in2c2dp5md2dei6m/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
            "text": "Ты книга по истории."
            },
            {
                "role": "user",
            "text": f"Придумай короткий захватывающий грозный захватывающий текст на это - {temp}."
            },
            
        ]
    }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNxvY-FnLp3ZX2L5yk8LjelO89edaWFRmhAX21"
    }
    #session = requests.Session()
    response = requests.post(url, headers=headers, json=prompt)
    result = response
    return result.text

def GENERATE(**temp):
    prompt = {
        "modelUri": "gpt://b1g7in2c2dp5md2dei6m/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
            "text": "Ты книга по истории."
            },
            {
                "role": "user",
            "text": f"Придумай короткий захватывающий рекламный текст на это - {temp}."
            },
            
        ]
    }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNxvY-FnLp3ZX2L5yk8LjelO89edaWFRmhAX21"
    }
    #session = requests.Session()
    interval = requests.post(url, headers=headers, json=prompt)
    result = json.loads(interval.text)
    return result['result']['alternatives'][0]['message']['text']










