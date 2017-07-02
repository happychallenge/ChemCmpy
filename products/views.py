from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from .models import Vendor, Product, Contact
from .forms import VendorForm, ContactForm
# Create your views here.
@login_required
def vendor_list(request):
    vendor_list = Vendor.objects.prefetch_related('tags').all()
    return render(request, 'products/vendor_list.html', {'vendor_list': vendor_list})


@login_required
def vendor_detail(request, id):
    # vendor = get_object_or_404(vendor, id=id)
    vendor = Vendor.objects.prefetch_related('vendorproduct_set', 'contact_set').get(id=id)
    return render(request, 'products/vendor_detail.html', {'vendor': vendor})


@staff_member_required
def vendor_add(request, template_name='products/vendor_add.html'):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            vendor = form.save()
            messages.success(request, 'Vendor was successfully added!!!')
            return redirect('chemical:vendor_list')
    else:
        form = VendorForm()

    return render(request, template_name, {'form':form})


@staff_member_required
def vendor_update(request, id, template_name='products/vendor_update.html'):
    vendor = get_object_or_404(Vendor, id=id)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            vendor = form.save()
            messages.success(request, 'Vendor was successfully updated!!!')
            return redirect('chemical:vendor_list')
    else:
        form = VendorForm(instance=vendor)

    return render(request, template_name, {'form':form})


@login_required
def product_list(request):
    product_list = Product.objects.all()
    return render(request, 'products/product_list.html', {'product_list': product_list})


@login_required
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})


@login_required
def contact_list(request):
    contact_list = Contact.objects.select_related('vendor').all()
    return render(request, 'products/contact_list.html', {'contact_list': contact_list})


@staff_member_required
def contact_add(request, template_name='products/contact_add.html'):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contact was successfully added!!!')
            return redirect('chemical:contact_list')
    else:
        form = ContactForm()

    return render(request, template_name, {'form':form})


@staff_member_required
def contact_update(request, id, template_name='products/contact_update.html'):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'contact was successfully updated!!!')
            return redirect('chemical:contact_list')
    else:
        form = ContactForm(instance=contact)

    return render(request, template_name, {'form':form})
