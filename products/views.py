from django.shortcuts import render, HttpResponse

def index(request):
    users = [
        {"id":1, "username":"Farid", "age":33},
        {"id":2, "username":"Ahmed", "age":25},
        {"id":3, "username":"Mohamed", "age":36},
    ]
    context = {
        "users":users,
        "page_title":"Home Page"
    }
    return render(request, 'products/index.html', context)


def about(request):
    return render(request, 'products/about.html')