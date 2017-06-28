from django.db import models

# Create your models here.
class Provider(models.Model):
    """docstring for Provider"""
    """ 설명 """
    cn_name = models.CharField(max_length=50, verbose_name='CHINESE NAME')
    en_name = models.CharField(max_length=50, verbose_name='ENGLISH NAME')
    cn_address = models.CharField(max_length=100, blank=True, null=True, verbose_name='CHINESE ADDRESS')
    en_address = models.CharField(max_length=100, blank=True, null=True, verbose_name='ENGLISH ADDRESS')
    homepage = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cn_name


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag


class Contact(models.Model):
    """docstring for Contact"""
    """ Contact """
    PRESIDENT = 'P'
    VICEPRESIDENT = 'VP'
    SALESDIRECTOR = 'SD'
    SALESMANAGER = 'SM'
    SALESMAN = 'S'
    ROLE = (
        (PRESIDENT, 'President'),
        (VICEPRESIDENT, 'Vice-President'),
        (SALESDIRECTOR, 'SalesDirector'),
        (SALESMANAGER, 'SalesManager'),
        (SALESMAN, 'SalesMan'),
    )

    cn_name = models.CharField(max_length=30, verbose_name='CHINESE NAME')
    en_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='ENGLISH NAME')
    role = models.CharField(max_length=2, choices=ROLE, default=SALESMAN)

    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    fixed = models.CharField(max_length=30, blank=True, null=True)
    wechat = models.CharField(max_length=30, blank=True, null=True)
    qq = models.CharField(max_length=30, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cn_name


class Category(models.Model):
    """docstring for Category"""
    cn_name = models.CharField(max_length=30)
    en_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cn_name

class Product(models.Model):
    """docstring for Product"""
    """ 설명 """
    cn_name = models.CharField(max_length=100, verbose_name='CHINESE NAME')
    en_name = models.CharField(max_length=100, verbose_name='ENGLISH NAME')
    cas_no = models.CharField(max_length=20, verbose_name='CAS NO', blank=True, null=True)
    category = models.ForeignKey(Category)

    cn_hscode = models.CharField(max_length=15, verbose_name='중국 HS CODE')
    ko_hscode = models.CharField(max_length=15, verbose_name='한국 HS CODE')
    etc_hscode = models.CharField(max_length=15, verbose_name='ETC HS CODE', blank=True, null=True)

    molnumber = models.FloatField(max_length=100, verbose_name='분자량', blank=True, null=True)
    chemequal = models.CharField(max_length=100, verbose_name='화학식', blank=True, null=True)
    chemstructure = models.ImageField(verbose_name='구조식', blank=True, null=True, upload_to='chemicalstructure/')
    
    usage = models.TextField(max_length=500, verbose_name='용도', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cn_name

    
class CompanyProduct(models.Model):
    """docstring for CompcanyProduct"""
    provider = models.ForeignKey(Provider)
    product = models.ForeignKey(Product)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.provider, self.product)
        