import re
from django import forms
from django.core.exceptions import ValidationError
from django_app.models import Category, Product, Supplier, News


class NewsForm ( forms.Form ) :
    title = forms.CharField (
        max_length=100,
        label='Title',
        widget=forms.TextInput ( attrs={
            'class' : 'form-control rounded-3 border-primary mb-0',
        } )
    )
    content = forms.CharField (
        required=False,
        label='Content',
        widget=forms.Textarea ( attrs={
            'class' : 'form-control rounded-3 border-primary',
            'rows' : 6,
            'style' : 'resize: vertical; min-height: 120px;'
        } )
    )
    photo = forms.ImageField (
        required=False,
        widget=forms.ClearableFileInput ( attrs={
            'class' : 'form-control rounded-3 border-primary',
        } )
    )
    bool = forms.BooleanField (
        required=False,
        initial=False,
        label='Bool',
        widget=forms.CheckboxInput ( attrs={
            'class' : 'form-check-input',
        } )
    )
    category = forms.ModelChoiceField (
        queryset=Category.objects.all (),
        widget=forms.Select ( attrs={
            'class' : 'form-select rounded-3 border-primary',
        } )
    )

    def clean_title(self) :
        title = self.cleaned_data.get ( 'title', '' )
        if re.match ( r'\d', title ) :
            raise ValidationError ( 'Title must not contain digits' )
        return title


class CategoryForm ( forms.Form ) :
    category_name = forms.CharField (
        max_length=100,
        widget=forms.TextInput ( attrs={
            'class' : 'form-control rounded-3 border-primary mb-0',
            'placeholder' : 'Enter category name',
        } )
    )
    description = forms.CharField (
        required=False,
        widget=forms.Textarea ( attrs={
            'class' : 'form-control rounded-3 border-primary',
            'rows' : 6,
            'style' : 'resize: vertical; min-height: 120px;',
            'placeholder' : 'Enter description (e.g., Toys and games for kids)',
        } )
    )
    image = forms.ImageField (
        required=False,
        widget=forms.ClearableFileInput ( attrs={
            'class' : 'form-control rounded-3 border-primary',
        } )
    )

    def clean_category_name(self) :
        category_name = self.cleaned_data.get ( 'category_name', '' ).strip ()

        if not category_name :
            raise ValidationError ( 'Category name is required' )

        if not category_name[0].isupper () :
            raise ValidationError ( 'Category name must start with an uppercase letter' )

        if re.search ( r'\d', category_name ) :
            raise ValidationError ( 'Category name must not contain digits' )

        return category_name


class ProductForm ( forms.Form ) :
    product_name = forms.CharField (
        max_length=50,
        widget=forms.TextInput ( attrs={
            'class' : 'form-control rounded-3 border-primary mb-0',
            'placeholder' : 'Enter product name',
        } )
    )
    category = forms.ModelChoiceField (
        queryset=Category.objects.all (),
        widget=forms.Select ( attrs={
            'class' : 'form-select rounded-3 border-primary',
        } )
    )
    unit_price = forms.IntegerField (
        widget=forms.NumberInput ( attrs={
            'class' : 'form-control rounded-3 border-primary',
            'placeholder' : 'Enter unit price',
        } )
    )
    description = forms.CharField (
        required=False,
        widget=forms.Textarea ( attrs={
            'class' : 'form-control rounded-3 border-primary',
            'rows' : 6,
            'style' : 'resize: vertical; min-height: 120px;',
            'placeholder' : 'Enter description (e.g., Database design principles)',
        } )
    )
    image = forms.ImageField (
        required=False,
        widget=forms.ClearableFileInput ( attrs={
            'class' : 'form-control rounded-3 border-primary',
        } )
    )

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


class SupplierForm ( forms.Form ) :
    company_name = forms.CharField (
        max_length=50,
        widget=forms.TextInput ( attrs={
            'class' : 'form-control rounded-3 border-primary mb-0',
            'placeholder' : 'Enter company name',
        } )
    )
    contact_name = forms.CharField (
        max_length=50,
        widget=forms.TextInput ( attrs={
            'class' : 'form-control rounded-3 border-primary mb-0',
            'placeholder' : 'Enter contact name',
        } )
    )
    contact_title = forms.CharField (
        max_length=50,
        widget=forms.TextInput ( attrs={
            'class' : 'form-control rounded-3 border-primary mb-0',
            'placeholder' : 'Enter contact title',
        } )
    )
    address = forms.CharField (
        max_length=50,
        widget=forms.Textarea ( attrs={
            'class' : 'form-control rounded-3 border-primary',
            'rows' : 2,
            'style' : 'resize: vertical; min-height: 60px;',
            'placeholder' : 'Enter address',
        } )
    )
    city = forms.CharField (
        max_length=50,
        widget=forms.TextInput ( attrs={
            'class' : 'form-control rounded-3 border-primary mb-0',
            'placeholder' : 'Enter city',
        } )
    )
    region = forms.CharField (
        max_length=50,
        widget=forms.TextInput ( attrs={
            'class' : 'form-control rounded-3 border-primary mb-0',
            'placeholder' : 'Enter region',
        } )
    )
    image = forms.ImageField (
        required=False,
        widget=forms.ClearableFileInput ( attrs={
            'class' : 'form-control rounded-3 border-primary',
        } )
    )

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
        region = self.cleaned_data.get ( 'region', '' ).strip ()

        if region and not region[0].isupper () :
            raise ValidationError ( 'Region name must start with an uppercase letter' )

        if region and (len ( region ) < 3 or len ( region ) > 50) :
            raise ValidationError ( 'Region name must be between 3 and 50 characters long' )

        return region