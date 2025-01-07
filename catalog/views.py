from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    # Получаем последние 5 продуктов
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Выводим продукты в консоль
    print("Последние 5 созданных продуктов:")
    for product in latest_products:
        print(f" - {product.name}, цена: {product.price}")

    return render(request, 'home.html', {'latest_products': latest_products})


def contact(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})

