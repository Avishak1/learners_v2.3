from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vendor
from .forms import MenuItemForm
from django.contrib.auth.models import User

@login_required
def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendors/vendor_list.html', {'vendors': vendors})

@login_required
def add_menu_item(request):
    vendor = get_object_or_404(Vendor, user=request.user)

    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.vendor = vendor
            menu_item.save()
            return redirect('vendor_menu')  # Define this view & URL later
    else:
        form = MenuItemForm()

    return render(request, 'vendors/add_menu_item.html', {'form': form})

@login_required
def vendor_menu(request):
    vendor = get_object_or_404(Vendor, user=request.user)
    menu_items = vendor.menu_items.all()
    return render(request, 'vendors/vendor_menu.html', {'menu_items': menu_items})
