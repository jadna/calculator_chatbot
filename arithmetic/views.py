from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
	return render(request, 'arithmetic/home.html')

# Create your views here.
@csrf_exempt
def webhook(request):
    res = {}
    # build a request object
    req = json.loads(request.body)

    # get action from json
    action = req.get('sessionInfo').get('parameters')
    operacao = action.get('operacao')
    print("ACTION: ", action)
    n1 = int(action.get('numero_1'))
    n2 = int(action.get('numero_2'))

    print("N1: ", n1)
    print("N2: ", n2)
    print("OP: ", operacao)

       
    if operacao == "Adição":
         resposta = n1+n2

    elif operacao == "Subtração":
         resposta = n1-n2
   
    elif operacao == 'Divisão':
        resposta = n1/n2
    else:
        resposta =  n1*n2


    fulfillmentResponse = {
        'fulfillmentResponse': {
            'messages': [{
                'text': {
                    'text': [resposta],
                },
            }]
        },
    }
   
    return JsonResponse(fulfillmentResponse, safe=False)
    
