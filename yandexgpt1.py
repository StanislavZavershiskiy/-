import requests

def send_to_gpt(data):
  api_key = "Ключ"
  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

  headers = {
      "Authorization": f"Api-Key {api_key}",
      "Content-Type": "application/json",
  }

  response = requests.post(url, headers=headers, json=data)
  answer = response.json()
  # print(answer)
  # print(answer['result'])
  
  return answer['result']['alternatives'][0]['message']['text']

# Функция для взаимодействия с YandexGPT
def ask_yandex_gpt(prompt):
        
    data = {
      "modelUri": "gpt://b1gki30urbqs5444u5kk/yandexgpt/latest",
      "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "2000"
      },
      "messages": [
        {
          "role": "system",
          "text": "Ты — умный ассистент"
        },
        {
          "role": "user",
          "text": prompt,
        }
      ]
    }

    return send_to_gpt(data)

def talk_to_yandex_gpt(messages):
  _messages = [
    {
      "role": "system",
      "text": "Ты — умный ассистент"
    },
  ]
  
  data = {
    "modelUri": "gpt://b1gki30urbqs5444u5kk/yandexgpt/latest",
    "completionOptions": {
      "stream": False,
      "temperature": 0.6,
      "maxTokens": "2000"
    },
    "messages": _messages + messages
  }
  
  return send_to_gpt(data)
  