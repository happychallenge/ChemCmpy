from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Vendor, Product
# Create your views here.
@login_required
def vendor_list(request):
    vendor_list = Vendor.objects.prefetch_related('tags').all()
    return render(request, 'products/vendor_list.html', {'vendor_list': vendor_list})


@login_required
def vendor_detail(request, id):
    # vendor = get_object_or_404(vendor, id=id)
    vendor = Vendor.objects.prefetch_related('vendorproduct_set').get(id=id)
    return render(request, 'products/vendor_detail.html', {'vendor': vendor})


@login_required
def product_list(request):
    product_list = Product.objects.all()
    return render(request, 'products/product_list.html', {'product_list': product_list})


@login_required
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})