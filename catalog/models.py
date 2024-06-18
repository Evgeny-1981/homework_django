from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    """Модель для категории"""
    name = models.CharField(max_length=120, verbose_name="наименование")
    description = models.TextField(max_length=255, verbose_name="описание", **NULLABLE)

    def __str__(self):
        return f"Наименование категории: {self.name}, описание: {self.description}"

    class Meta:
        db_table = "category"
        verbose_name = "категорию"
        verbose_name_plural = "категории"
        ordering = ("name",)


class Product(models.Model):
    """Модель для продукта"""
    name = models.CharField(max_length=120, verbose_name="наименование")

    description = models.TextField(max_length=255, verbose_name="описание", **NULLABLE)
    image = models.ImageField(
        upload_to="media/product_image/", verbose_name="изображение", **NULLABLE
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, verbose_name="категория", **NULLABLE
    )
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name="цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="количество")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    update_at = models.DateTimeField(auto_now_add=True, verbose_name="дата последнего изменения")

    # manufactured_at = models.DateTimeField(verbose_name='дата производства продукта', default=datetime.datetime.now())

    def __str__(self):
        return f"Наименование продукта: {self.name}, категория продукта: {self.category}, цена: {self.price}"

    def product_id(self):
        return f'{self.id:04}'

    class Meta:
        db_table = "product"
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("name",)


class Blog(models.Model):
    """Модель для блога"""
    title = models.CharField(max_length=120, verbose_name="заголовок", unique=True)
    slug = models.CharField(max_length=120, verbose_name="слаг")
    content = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(upload_to="blog/images", verbose_name="превью(изображение)", **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name="дата создания")
    published = models.BooleanField(verbose_name="признак публикации", default=False)
    count_views = models.PositiveIntegerField(verbose_name="счетчик просмотров", default=0, **NULLABLE)

    class Meta:
        db_table = "blog"
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = ("count_views",)

    def __str__(self):
        return f"{self.title}, {self.content}"

class Version(models.Model):
    """Модель для версии продукта"""
    product = models.ForeignKey(Product, related_name='version', verbose_name='продукт', on_delete=models.CASCADE)
    version_number = models.PositiveIntegerField(verbose_name=' номер версии', **NULLABLE)
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    current_version = models.BooleanField(default=True, verbose_name='признак текущей версии')

    class Meta:
        db_table = "version"
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('version_name',)

    def __str__(self):
        return f"{self.version_name}, {self.version_number}"
