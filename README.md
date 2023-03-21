# calculator_chatbot

É uma calculadora utilizando Django como webhook e chatbot do Google Dialogflow.

Antes de prosseguirmos, você precisa ter as seguintes coisas:

- Python
- Django — estrutura da web Python para lidar com webhook
- Ngrok — Para acessar seu localhost em todo o mundo
- Google Dialogflow

## Passos para executar

#### Executar o ngrok

```
ngrok http 8000
```

#### Executar o Django

Para executar o servidor, use o comando abaixo,

```
python3 manage.py runserver
```

O projeto foi baseado no [Calculator chatbot using Django and Dialogflow](https://medium.com/analytics-vidhya/calculator-chatbot-dialo-e9f8e08d07af).