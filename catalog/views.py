from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, TemplateView

from catalog.models import Product, Contact


class HomeView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()  # Получаем все товары
        return context


class ContactView(View):
    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, 'catalog/contacts.html', {'contacts': contacts})  # Передаем контекст в шаблон

    def post(self, request):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
