from django.shortcuts import render

def products(request):
    title = 'продукты/каталог'
    context = {
        'title': title
    }
    return render(request, 'products.html', context)
