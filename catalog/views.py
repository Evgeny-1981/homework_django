from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm, BlogForm, BlogModeratorForm, CategoryForm
from catalog.models import Product, Blog, Version, Category
from catalog.services import get_categoryes_list


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get_queryset(self):
        return get_categoryes_list()


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания продукта"""
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:categoryes_list')


class ProductListView(ListView):
    """Контроллер отображения страницы с продуктами"""
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        user = self.request.user
        if user.has_perm('catalog.change_published'):
            queryset = queryset.all()
            return queryset
        else:
            queryset = queryset.filter(published=True)
            return queryset

    def get_context_data(self, *args, **kwargs):
        """Метод для получения версии продукта и вывода только активной версии"""
        context = super().get_context_data(*args, **kwargs)
        products = self.get_queryset()
        for product in products:
            product.version_name = product.version.filter(current_version=True).first()
        context["object_list"] = products
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания продукта"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        """Метод для создания формсета"""
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_blog = form.save()
    #         new_blog.slug = slugify(new_blog.title)
    #         new_blog.save()
    #     return super().form_valid(form)

    def form_valid(self, form):
        """Метод валидации формы и формсета"""
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            self.object.slug = slugify(self.object.name)
            formset.instance = self.object
            formset.save()
            self.object.owner = self.request.user
            self.object.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDetailView(DetailView):
    """Контроллер для просмотра продукта"""
    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm('catalog.change_published') and user.has_perm(
                'catalog.change_description_product') and user.has_perm('catalog.change_category_product'):
            return ProductModeratorForm
        else:
            raise PermissionDenied

    def get_success_url(self):
        """ Метод для определения пути, куда будет совершен переход после редактирования продукта"""
        return reverse('catalog:product_info', args=[self.get_object().slug])

    def get_context_data(self, **kwargs):
        """Метод для создания формсета"""
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        """Метод валидации формы и формсета"""
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(LoginRequiredMixin, DeleteView, ):
    """Контроллер для удаления продукта"""
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        else:
            raise PermissionDenied


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(f'Имя:{name}, тел.:{phone}, сообщение: {message}')
        return HttpResponseRedirect(self.request.path)


# def contact(request):
#     """Контроллер отображения страницы с контактами"""
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'Имя:{name}, тел.:{phone}, сообщение: {message}')
#     return render(request, 'catalog/contacts.html')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    # fields = ("title", "content", "preview", "published")
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogModeratorForm
    # fields = ("title", "slug", "content", "preview", "published",)
    success_url = reverse_lazy('catalog:blog_list')

    def get_success_url(self):
        return reverse('catalog:blog_info', args=[self.kwargs.get('slug')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
