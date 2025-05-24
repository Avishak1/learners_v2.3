from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from vendors.models import Vendor, MenuItem
from .models import Order, OrderItem

@login_required
def place_order(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    menu_items = MenuItem.objects.filter(vendor=vendor, available=True)

    if request.method == 'POST':
        # Extract selected items and quantities
        selected_items = []
        for item in menu_items:
            qty_str = request.POST.get(f'quantity_{item.id}')
            try:
                qty = int(qty_str)
            except (TypeError, ValueError):
                qty = 0
            if qty > 0:
                selected_items.append((item, qty))

        if not selected_items:
            return render(request, 'orders/place_order.html', {
                'vendor': vendor,
                'menu_items': menu_items,
                'error': 'Please select at least one item with quantity > 0.'
            })

        # Create order
        order = Order.objects.create(customer=request.user, vendor=vendor)
        # Create OrderItems
        for item, qty in selected_items:
            OrderItem.objects.create(order=order, menu_item=item, quantity=qty)

        return redirect('order_success')

    return render(request, 'orders/place_order.html', {
        'vendor': vendor,
        'menu_items': menu_items
    })

@login_required
def order_success(request):
    return render(request, 'orders/order_success.html')

