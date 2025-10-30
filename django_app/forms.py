import re
from django import forms
from django.core.exceptions import ValidationError
from django_app.models import Category, Product, Supplier, News

from django import forms
from django.core.exceptions import ValidationError
from .models import News, Category
import re


class NewsForm ( forms.ModelForm ) :
    class Meta :
        model = News
        fields = '__all__'

        widgets = {
            'title' : forms.TextInput ( attrs={
                'class' : 'form-control rounded-3 border-primary mb-0',
            } ),
            'content' : forms.Textarea ( attrs={
                'class' : 'form-control rounded-3 border-primary',
                'rows' : 6,
                'style' : 'resize: vertical; min-height: 120px;'
            } ),
            'photo' : forms.ClearableFileInput ( attrs={
                'class' : 'form-control rounded-3 border-primary',
            } ),
            'bool' : forms.CheckboxInput ( attrs={
                'class' : 'form-check-input',
            } ),
            'category' : forms.Select ( attrs={
                'class' : 'form-select rounded-3 border-primary',
            } ),
        }

    def clean_title(self) :
        title = self.cleaned_data.get ( 'title', '' )
        if re.match ( r'\d', title ) :
            raise ValidationError ( 'Title must not contain digits' )
        return title


class CategoryForm ( forms.ModelForm ) :
    class Meta :
        model = Category
        fields = ['category_name', 'description', 'image']
        widgets = {
            'category_name' : forms.TextInput ( attrs={
                'class' : 'form-control rounded-3 border-primary mb-0',
                'placeholder' : 'Enter category name',
            } ),
            'description' : forms.Textarea ( attrs={
                'class' : 'form-control rounded-3 border-primary',
                'rows' : 6,
                'style' : 'resize: vertical; min-height: 120px;',
                'placeholder' : 'Enter description (e.g., Toys and games for kids)',
            } ),
            'image' : forms.ClearableFileInput ( attrs={
                'class' : 'form-control rounded-3 border-primary',
            } ),
        }

    def __init__(self, *args, **kwargs) :
        super ().__init__ ( *args, **kwargs )
        self.fields['description'].required = False
        self.fields['image'].required = False

    def clean_category_name(self) :
        category_name = self.cleaned_data.get ( 'category_name', '' ).strip ()

        if not category_name :
            raise ValidationError ( 'Category name is required' )

        if not category_name[0].isupper () :
            raise ValidationError ( 'Category name must start with an uppercase letter' )

        if re.search ( r'\d', category_name ) :
            raise ValidationError ( 'Category name must not contain digits' )

        return category_name


class ProductForm ( forms.ModelForm ) :
    class Meta :
        model = Product
        fields = "__all__"
        widgets = {
            'product_name' : forms.TextInput ( attrs={
                'class' : 'form-control rounded-3 border-primary mb-0',
                'placeholder' : 'Enter product name',
            } ),
            'category' : forms.Select ( attrs={
                'class' : 'form-select rounded-3 border-primary',
            } ),
            'unit_price' : forms.NumberInput ( attrs={
                'class' : 'form-control rounded-3 border-primary',
                'placeholder' : 'Enter unit price',
            } ),
            'description' : forms.Textarea ( attrs={
                'class' : 'form-control rounded-3 border-primary',
                'rows' : 6,
                'style' : 'resize: vertical; min-height: 120px;',
                'placeholder' : 'Enter description (e.g., Database design principles)',
            } ),
            'image' : forms.ClearableFileInput ( attrs={
                'class' : 'form-control rounded-3 border-primary',
            } ),
        }

    def __init__(self, *args, **kwargs) :
        super ().__init__ ( *args, **kwargs )
        self.fields['description'].required = False
        self.fields['image'].required = False

    def clean_product_name(self) :
        product_name = self.cleaned_data.get ( 'product_name', '' ).strip ()

        if not product_name :
            raise ValidationError ( 'Product name is required' )

        if not re.match ( r'^[a-zA-Z\s]+$', product_name ) :
            raise ValidationError ( 'Product name must contain only letters and spaces (no digits or punctuation)' )

        return product_name

    def clean_unit_price(self) :
        unit_price = self.cleaned_data.get ( 'unit_price' )

        if unit_price is None :
            raise ValidationError ( 'Unit price is required' )

        if unit_price <= 1 :
            raise ValidationError ( 'Unit price must be greater than $1' )

        if unit_price >= 10000 :
            raise ValidationError ( 'Unit price must be less than $10000' )

        return unit_price


class SupplierForm ( forms.ModelForm ) :
    class Meta :
        model = Supplier
        exclude = ['supplier_id']

        widgets = {
            'company_name' : forms.TextInput ( attrs={
                'class' : 'form-control rounded-3 border-primary mb-0',
                'placeholder' : 'Enter company name',
            } ),
            'contact_name' : forms.TextInput ( attrs={
                'class' : 'form-control rounded-3 border-primary mb-0',
                'placeholder' : 'Enter contact name',
            } ),
            'contact_title' : forms.TextInput ( attrs={
                'class' : 'form-control rounded-3 border-primary mb-0',
                'placeholder' : 'Enter contact title',
            } ),
            'address' : forms.Textarea ( attrs={
                'class' : 'form-control rounded-3 border-primary',
                'rows' : 2,
                'style' : 'resize: vertical; min-height: 60px;',
                'placeholder' : 'Enter address',
            } ),
            'city' : forms.TextInput ( attrs={
                'class' : 'form-control rounded-3 border-primary mb-0',
                'placeholder' : 'Enter city',
            } ),
            'region' : forms.TextInput ( attrs={
                'class' : 'form-control rounded-3 border-primary mb-0',
                'placeholder' : 'Enter region',
            } ),
            'image' : forms.ClearableFileInput ( attrs={
                'class' : 'form-control rounded-3 border-primary',
            } ),
        }

    def __init__(self, *args, **kwargs) :
        super ().__init__ ( *args, **kwargs )
        self.fields['image'].required = False
        self.fields['region'].required = False

    def clean_company_name(self) :
        company_name = self.cleaned_data.get ( 'company_name', '' )
        if re.match ( r'\d', company_name ) :
            raise ValidationError ( 'Company name must not contain digits' )
        return company_name

    def clean_city(self) :
        city = self.cleaned_data.get ( 'city', '' ).strip ()
        if not city :
            raise ValidationError ( 'City field is required' )
        if not city[0].isupper () :
            raise ValidationError ( 'City name must start with an uppercase letter' )
        if len ( city ) < 3 or len ( city ) > 50 :
            raise ValidationError ( 'City name must be between 3 and 50 characters long' )
        return city

    def clean_region(self) :
        region = self.cleaned_data.get ( 'region' )

        if not region :
            return None

        region = str ( region ).strip () if region else None

        if not region :
            return None

        if not region[0].isupper () :
            raise ValidationError ( 'Region name must start with an uppercase letter' )

        if len ( region ) < 3 or len ( region ) > 50 :
            raise ValidationError ( 'Region name must be between 3 and 50 characters long' )

        return region