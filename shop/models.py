from django.db import models

class Category(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField('Наименование', max_length=60)
    description = models.TextField('Описание')
    price = models.PositiveSmallIntegerField('Цена', default=0)
    image = models.ImageField('Изображение', upload_to='media/product/')
    url = models.SlugField(max_length=160, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    quantity = models.PositiveIntegerField('Количество', default=0)
    draft = models.BooleanField('Черновик', default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Favorite(models.Model):
    add = models.BooleanField('Добавить в избранное', default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.add} - {self.product}'

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'    

class Reviews(models.Model):
    email = models.EmailField('Почта')
    name = models.CharField('Имя', max_length=150)
    text = models.TextField('Отзыв')
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.product}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'