from django import forms
from django.core.exceptions import ValidationError
from .models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]

MAX_IMAGE_SIZE = 5 * 1024 * 1024


def validate_no_forbidden_words(value):
    value_lower = value.lower()
    for word in FORBIDDEN_WORDS:
        if word in value_lower:
            raise ValidationError(f'Использование слова "{word}" недопустимо.')


def validate_image_size(image):
    if image.size > MAX_IMAGE_SIZE:
        raise ValidationError("Размер файла изображения не должен превышать 5 MB.")


def validate_image_format(image):
    valid_formats = ["image/jpeg", "image/png"]
    if image.content_type not in valid_formats:
        raise ValidationError(
            "Недопустимый формат изображения. Загрузите изображение в формате JPEG или PNG."
        )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "category",
            "stock",
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену продукта"}
        )
        self.fields["category"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберите категорию продукта"}
        )
        self.fields["image"].widget.attrs.update({"class": "form-control-file"})

    def clean_name(self):
        name = self.cleaned_data.get("name")
        validate_no_forbidden_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        validate_no_forbidden_words(description)
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            validate_image_size(image)
            validate_image_format(image)
        return image
