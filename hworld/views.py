from django.http import HttpResponse

def index(response):
    return HttpResponse("Hello, world. you're looking at me") 


