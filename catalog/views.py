from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, TemplateView

from catalog.forms import ProductForm
from catalog.models import Product, Contact


class HomeView(TemplateView):
    template_name = "catalog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context


class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, "catalog/contacts.html", {"contacts": contacts})

    def post(self, request):
        name = request.POST.get("name")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProductForm()
        return render(request, "catalog/product_create.html", {"form": form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            messages.success(request, "Продукт успешно создан.")
            return redirect("catalog:home")
        return render(request, "catalog/product_create.html", {"form": form})


class ProductEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if request.user != product.owner and not request.user.is_moderator:
            messages.error(request, "У вас нет прав для редактирования этого продукта.")
            return redirect("catalog:home")
        form = ProductForm(instance=product)
        return render(
            request, "catalog/product_edit.html", {"form": form, "product": product}
        )

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if request.user != product.owner and not request.user.is_moderator:
            messages.error(request, "У вас нет прав для редактирования этого продукта.")
            return redirect("catalog:home")
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("catalog:product_detail", pk=product.pk)
        return render(
            request, "catalog/product_edit.html", {"form": form, "product": product}
        )


class ProductDelete(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        if request.user != product.owner and not request.user.is_moderator:
            messages.error(request, "У вас нет прав для удаления этого продукта.")
            return redirect("catalog:home")
        product.delete()
        messages.success(request, "Продукт успешно удалён.")
        return redirect("catalog:home")


class ProductUnpublish(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        if request.user != product.owner and not request.user.is_moderator:
            messages.error(request, "У вас нет прав для отмены этого продукта.")
            return redirect("catalog:home")
        product.is_published = False
        product.save()
        messages.success(request, "Продукт успешно отменён.")
        return redirect("catalog:home")
