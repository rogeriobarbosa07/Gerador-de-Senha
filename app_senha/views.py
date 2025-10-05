from django.shortcuts import render
from .funcao_senha import senha
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def gerador_senha(request):
    senha_gerada = ''
    if request.method == 'POST':
        senha_gerada = senha()

    context = {
        'senha_gerada': senha_gerada,
    }

    return render(request, 'app_senha/gerador_senha.html', context) # renderizando página html