from django.shortcuts import render, HttpResponse, redirect

items = [
    {
        'item': 'Dojo Tshirt',
        'price': 19.99,
        'id': 1
    },
    {
        'item': 'Dojo Sweater',
        'price': 29.99,
        'id': 2
    },
    {
        'item': 'Dojo Cup',
        'price': 4.99,
        'id': 3
    },
    {
        'item': 'Algorithm Book',
        'price': 49.99,
        'id': 4
    },
]
def index(request):
    if "last_transaction" in request.session.keys():
        del request.session['last_transaction']
    context = {
        'items': items
    }
    return render(request, 'amadon_app/index.html', context)

def buy(request, item_id):
    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])

    try:
        request.session['total_charged']
    except KeyError:
        request.session['total_charged'] = 0

    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0

    request.session['last_transaction'] = amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['total_charged'] += amount_charged

    return redirect('/Amadon/checkout')

def checkout(request):
    return render(request, 'amadon_app/checkout.html')

def reset(request):
    for sesh in request.session.keys():
        del request.session[sesh]
    return redirect('/')
