from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import MenuItem, Order
from .forms import MenuItemForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Перенаправление на домашнюю страницу
    return render(request, 'cafe/login.html')


def menu_view(request):
    """Отображает все элементы меню."""
    menu_items = MenuItem.objects.all()
    return render(request, 'cafe/menu.html', {'menu_items': menu_items})


@login_required
def orders_view(request):
    """Отображает все заказы для текущего пользователя."""
    orders = Order.objects.filter(user=request.user)  # Фильтруем заказы по текущему пользователю
    return render(request, 'cafe/orders.html', {'orders': orders})


def order_view(request):
    """Отображает страницу заказа."""
    return render(request, 'cafe/order.html')


def base_view(request):
    """Отображает домашнюю страницу."""
    return render(request, 'cafe/base.html')


def cart_view(request):
    """Отображает корзину."""
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for item_id, quantity in cart.items():
        item = MenuItem.objects.get(id=item_id)
        total_price += item.price * quantity
        cart_items.append({'item': item, 'quantity': quantity})

    return render(request, 'cafe/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart_view(request, item_id):
    """Добавляет элемент в корзину."""
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    request.session['cart'] = cart
    return redirect('cart')


def index(request):
    """Отображает индексную страницу."""
    return render(request, 'cafe/index.html')


@login_required
def add_menu_item(request):
    """Добавляет новый элемент меню."""
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)  # Включите request.FILES для загрузки изображений
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MenuItemForm()
    return render(request, 'cafe/add_menu_item.html', {'form': form})


def register_view(request):
    """Отображает страницу регистрации."""
    return render(request, 'cafe/register.html')


def delivery_view(request):
    """Отображает информацию о доставке."""
    return render(request, 'cafe/delivery.html')


def admin_menu_view(request):
    """Отображает административное меню."""
    menu_items = MenuItem.objects.all()
    return render(request, 'cafe/admin_menu.html', {'menu_items': menu_items})


@login_required
def checkout_view(request):
    """Обрабатывает оформление заказа."""
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('cart')

        order = Order.objects.create(user=request.user)
        total_price = 0

        for item_id, quantity in cart.items():
            item = MenuItem.objects.get(id=item_id)
            total_price += item.price * quantity

        order.totalPrice = total_price
        order.save()

        # Очистить корзину после оформления заказа
        request.session['cart'] = {}
        return redirect('orders')  # Перенаправить на страницу заказов

    return render(request, 'cafe/checkout.html')
