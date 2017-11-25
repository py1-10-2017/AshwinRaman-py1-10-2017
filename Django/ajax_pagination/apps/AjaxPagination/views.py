from django.shortcuts import render, redirect, HttpResponse
from .models import *
import json
# Create your views here.
def index(request):
    num_users = User.objects.all().count()
    num_pages = int(num_users/10)+1
    context = {
        "users": User.objects.all()[:10],
        "pagination": range(1,num_pages+1)
    }
    request.session['name'] = ""
    request.session['start'] = ""
    request.session['end'] = ""
    return render(request, 'AjaxPagination/index.html', context)

def show(request):

    page_number = 1
    if request.method == "GET":
        try:
            if 'name' in request.GET:
                request.session['name'] = request.GET['name']
        except:
            pass

        try:
            if 'start' in request.GET:
                request.session['start'] = request.GET['start']
        except:
            pass
        try:
            if 'end' in request.GET:
                request.session['end'] = request.GET['end']
        except:
            pass

    else:
        page_number = int(request.POST['page_number'])
        print("Looking for page: "+str(page_number))

    users = User.objects.all()
    if (request.session['name'] != ""):
        users = users.filter(first_name__istartswith=request.session['name']) | User.objects.filter(last_name__istartswith=request.session['name'])

    if (request.session['start']):
        users = users.filter(created_at__gte=request.session['start'])

    if (request.session['end']):
        users = users.filter(created_at__lte=request.session['end'])

    if (page_number == 1):
        users = users[:10]
    else:
        offset = 10*(page_number-1)
        users = users[offset:offset+10]

    html_str = '<table class="table-striped"><tr><th>User ID</th><th>First Name</th><th>Last Name</th><th>Registration Date</th><th>Email</th></tr>'
    for user in users:
        html_str += '<tr><td>'+str(user.id)+'</td><td>'+user.first_name+'</td><td>'+user.last_name+'</td><td>'+str(user.created_at).split(" ")[0]+'</td><td>'+user.email+'</td></tr>'
    html_str += '</table>'
    num_pages = int(users.count()/10)+1
    response = {
        "list": html_str,
        "num_page": num_pages
    }
    return HttpResponse(json.dumps(response))
