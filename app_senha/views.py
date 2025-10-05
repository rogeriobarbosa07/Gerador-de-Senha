from django.shortcuts import render
import funcao_senha

# Create your views here.

def gerador_senha(request):
    if request.method == 'POST':
        senha = funcao_senha.senha()
        
    context = {
        'senha': senha,
    }

    return render(request, 'app_senha/gerador_senha.html', context) # renderizando página html