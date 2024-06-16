from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from catalog.models import Product, Version


class FormMixin:
    """Класс для стилизации форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(FormMixin, ModelForm):
    """Класс для создание форм для модели Продукт"""
    locked_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('update_at',)

    def clean_name(self):
        """Метод для проверки валидации названия продукта при создании"""
        cleaned_data = self.cleaned_data['name']
        if cleaned_data.lower() in self.locked_words:
            raise ValidationError(f'Слово {cleaned_data} запрещено использовать в названии продукта!')
        return cleaned_data

    def clean_description(self):
        """Метод для проверки валидации описания продукта при создании"""
        cleaned_data = self.cleaned_data['description']
        if cleaned_data.lower() in self.locked_words:
            raise ValidationError(f'Слово {cleaned_data} запрещено использовать в описании продукта!')
        return cleaned_data


class VersionForm(FormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
