from django.shortcuts import render

# Create your views here.


def main(request):
    content = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    links_menu = [
        {'href': 'products', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'same_products': 'same_products'
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    content = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contact.html', context=content)
