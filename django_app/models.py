from django.db import models


class Category ( models.Model ) :
    category_id = models.AutoField ( primary_key=True )
    category_name = models.CharField ( max_length=100 )
    description = models.TextField ( blank=True, null=True )
    image = models.ImageField ( upload_to='photo/%Y/%m/%d', blank=True, null=True )

    def __str__(self) :
        return self.category_name

    class Meta :
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product ( models.Model ) :
    product_id = models.AutoField ( primary_key=True )
    product_name = models.CharField ( max_length=50 )
    category = models.ForeignKey ( Category, on_delete=models.CASCADE )
    unit_price = models.IntegerField ()
    description = models.TextField ( blank=True, null=True )
    image = models.ImageField ( upload_to='photo/%Y/%m/%d', blank=True, null=True )

    def __str__(self) :
        return self.product_name

    class Meta :
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-product_name']


class Supplier ( models.Model ) :
    supplier_id = models.AutoField ( primary_key=True )
    company_name = models.CharField ( max_length=50 )
    contact_name = models.CharField ( max_length=50 )
    contact_title = models.CharField ( max_length=50 )
    address = models.CharField ( max_length=50 )
    city = models.CharField ( max_length=50 )
    region = models.CharField ( max_length=50 )
    image = models.ImageField ( upload_to='photo/%Y/%m/%d', blank=True, null=True )

    class Meta :
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'


class News ( models.Model ) :
    news_id = models.IntegerField ()
    title = models.CharField ( max_length=100, verbose_name='Title' )
    content = models.TextField ( blank=True, null=True, verbose_name='Content' )
    created_at = models.DateTimeField ( auto_now_add=True, verbose_name='Add_date' )
    updated_at = models.DateTimeField ( auto_now=True )
    photo = models.ImageField ( upload_to='photo/%Y/%m/%d', blank=True, null=True )
    bool = models.BooleanField ( default=False, verbose_name='Bool' )
    category = models.ForeignKey ( Category, on_delete=models.CASCADE, default=1 )

    def __str__(self) :
        return self.title

    class Meta :
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ['-created_at']