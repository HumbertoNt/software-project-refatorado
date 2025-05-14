from django.shortcuts import render

# Create your views here.
def home_user_view(request):
    return render(request, 'gerenciamentoUsuario/home.html')