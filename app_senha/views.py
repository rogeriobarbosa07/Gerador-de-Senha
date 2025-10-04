from django.shortcuts import render

# Create your views here.

def gerador_senha(request):
    return render(request, 'app_senha/gerador_senha.html', {}) # renderizando página html