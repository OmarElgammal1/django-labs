from django.shortcuts import render

def menu_list(request):
    dishes = [
        {'id': 1, 'name': 'Ice Cream', 'category': 'Dessert', 'price': 60, 'available': True},
        {'id': 2, 'name': 'Tiramisu', 'category': 'Dessert', 'price': 90, 'available': False},
        {'id': 3, 'name': 'Margherita Pizza', 'category': 'Main Course', 'price': 150, 'available': True},
        {'id': 4, 'name': 'Caesar Salad', 'category': 'Appetizer', 'price': 80, 'available': True},
        {'id': 5, 'name': 'Grilled Chicken', 'category': 'Main Course', 'price': 180, 'available': True},
    ]

    q = request.GET.get('q', '').lower().strip()
    category = request.GET.get('category', '').strip()

    filtered_dishes = dishes
    if q:
        filtered_dishes = [d for d in filtered_dishes if q in d['name'].lower()]
    if category and category != 'All Categories':
        filtered_dishes = [d for d in filtered_dishes if d['category'] == category]

    categories = list(set([d['category'] for d in dishes]))
    categories.sort()

    context = {
        'dishes': filtered_dishes,
        'categories': categories,
        'q': q,
        'selected_category': category
    }
    return render(request, 'menu_list.html', context)
