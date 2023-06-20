from django.http import HttpResponse

def saludo(request):
    ##return HttpResponse("Hola mundo.");
    documento="""""<html>
    <body>
    <h1>Hola mundo
    </h1>
    </body>
    </html>""""
    def despedida(request):
    return HttpResponse("Hasta luego");