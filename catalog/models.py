from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
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
    create_at = models.DateTimeField(verbose_name="дата создания")
    update_at = models.DateTimeField(verbose_name="дата последнего изменения")

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
    title = models.CharField(max_length=120, verbose_name="заголовок")
    slug = models.CharField(max_length=120, verbose_name="слаг")
    content = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(upload_to="blog/images", verbose_name="превью(изображение)", **NULLABLE)
    created_at = models.DateField(verbose_name="дата создания")
    published = models.BooleanField(verbose_name="признак публикации", default=False)
    count_views = models.PositiveIntegerField(verbose_name="счетчик просмотров", default=0, **NULLABLE)

    class Meta:
        db_table = "blog"
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = ("count_views",)

    def __str__(self):
        return f"{self.title}, {self.content}"
