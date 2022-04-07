from django.forms import ValidationError
from django.db import models

from colorfield.fields import ColorField

from http.client import REQUESTED_RANGE_NOT_SATISFIABLE


class Slaider(models.Model):
    photo = models.ImageField(upload_to='static/images')


class Category(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name', )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Collection(models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to='static/images/', null=True, blank=True)


class Product(models.Model):
    class Status(models.Model):
        CHOICES = (
            (0, 'Novelties'),
            (1, 'HitSellings'),
        )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    colls =  models.ForeignKey(Collection, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    articul = models.CharField(max_length=150)
    color = ColorField(default='#FF0000')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True) 
    images = models.ImageField(upload_to='static/images', blank=True, null=True)   
    size_row = models.CharField(max_length=25)
    quantity = models.IntegerField()
    fabric_structure = models.CharField(max_length=50)
    fabric = models.CharField(max_length=50)
    status = models.IntegerField(choices=Status.CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True, verbose_name='Есть в наличии?')

    class Meta:
        ordering = ('created_at', )
        verbose_name = 'Product'
        verbose_name = 'Products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.image

    def clean(self):
        if len(ProductImage.objects.filter(product_id=self.product.pk)) >= 8:
            raise ValidationError('The quantity should not exceed 8')


class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_color')
    color = ColorField(default='#F0F8FF')

    def __str__(self):
        return self.product.color

    def clean(self):
        if len(ProductColor.objects.filter(product_id=self.product.pk)) >= 8:
            raise ValidationError('The quantity should not exceed 8')


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


class AboutUsImage(models.Model):
    about = models.ForeignKey(AboutUs, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.about.title

    def clean(self):
        if len(AboutUsImage.objects.filter(about_id=self.about.pk)) >= 3:
            raise ValidationError('The quantity should not exceed 3')


class News(models.Model):
    image = models.ImageField(upload_to='static/images/')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title    


class Advantages(models.Model):
    icon = models.ImageField(upload_to='static/images/')
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title  


class PublicOffers(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title  


class Help(models.Model):
    question = models.TextField()
    answer = models.TextField()
    photo = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.question  


class Footer(models.Model):
    class Type(models.Model):
        CHOICES = (
        (0, 'Number'),
        (1, 'Email'),
        (2, 'Instagram'),
        (3, 'Telegram'),
        (4, 'WhatsApp'),
        )
    logotype = models.ImageField(upload_to='static/images/')
    info = models.TextField()
    id_header = models.IntegerField() 
    number = models.IntegerField(choices=Type.CHOICES)
    email = models.CharField(max_length=100, choices=Type.CHOICES)
    instagram = models.CharField(max_length=100, choices=Type.CHOICES)
    telegram = models.CharField(max_length=100, choices=Type.CHOICES)
    whatsapp = models.IntegerField(choices=Type.CHOICES)