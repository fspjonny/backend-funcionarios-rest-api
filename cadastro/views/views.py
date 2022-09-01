from django.shortcuts import render


def api_list(request):
    return render(request, 'cadastro/cadastro_page.html')

def handler404(request, exception):
    return render(request, 'cadastro/pagina404.html')
