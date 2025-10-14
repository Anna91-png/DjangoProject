from django import forms
from django.core.exceptions import ValidationError
from .models import Product

# 🔒 список запрещённых слов
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


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # ✅ добавь поле "image", только если оно есть в модели Product
        fields = ["category", "name", "description", "price"]

        labels = {
            "category": "Категория",
            "name": "Название товара",
            "description": "Описание",
            "price": "Цена (₼)",
        }

    # 🧠 Стилизация формы
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": field.label
            })

        # если появится булево поле
        if "is_active" in self.fields:
            self.fields["is_active"].widget.attrs["class"] = "form-check-input"

    # 🚫 Проверка имени
    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"Слово «{word}» запрещено в названии продукта.")
        return name

    # 🚫 Проверка описания
    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f"Слово «{word}» запрещено в описании продукта.")
        return description

    # 💰 Проверка цены
    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price
