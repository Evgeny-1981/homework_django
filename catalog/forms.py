from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from catalog.models import Product, Version, Blog


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
        exclude = ('update_at', 'owner',)

    def clean_name(self):
        """Метод для проверки валидации названия продукта при создании"""
        list_words = []
        cleaned_data = self.cleaned_data['name']
        for word in self.locked_words:
            if word in cleaned_data:
                list_words.append(word)
        result_locked_words = ", ".join(list_words)
        if len(result_locked_words) != 0:
            raise ValidationError(f'Запрещено использовать в названии слова: {result_locked_words}')
        return cleaned_data

    def clean_description(self):
        """Метод для проверки валидации описания продукта при создании"""
        list_words = []
        cleaned_data = self.cleaned_data['description']
        for word in self.locked_words:
            if word in cleaned_data:
                list_words.append(word)
        result_locked_words = ", ".join(list_words)
        if len(result_locked_words) != 0:
            raise ValidationError(f'Запрещено использовать в описании слова: {result_locked_words}')
        return cleaned_data


class VersionForm(FormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ProductModeratorForm(FormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'description', 'published',)


class BlogForm(FormMixin, ModelForm):
    class Meta:
        model = Blog
        exclude = ('count_views', 'slug', 'created_at',)


class BlogModeratorForm(FormMixin, ModelForm):
    class Meta:
        model = Blog
        exclude = ('count_views', 'created_at',)
