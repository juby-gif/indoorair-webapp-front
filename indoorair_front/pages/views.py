from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect


#Homepage views
def index_page(request):
    return render(request, "pages/homepage/index.html", {})

def contact_page(request):
    return render(request, "pages/homepage/contact.html", {})

#Gateway views
def register_page(request):
    return render(request, "pages/gateway/register.html", {})

def register_success_page(request):
    return render(request, "pages/gateway/register_success.html", {})

def login_page(request):
    return render(request, "pages/gateway/login.html", {})

def logout_page(request):
    return render(request, "pages/gateway/logout.html", {})

#Dashboard views
def dashboard_page(request):
    return render(request, "pages/dashboard/dashboard.html", {
        'user': request.user,
    })

#Instrument views
def i_list_page(request):
    return render(request, "pages/instrument/list.html", {})

def i_create_page(request):
    return render(request, "pages/instrument/create.html", {})

def i_retrieve_page(request, id):
    return render(request, "pages/instrument/retrieve.html", {
        "instrument_id": int(id),
    })

def i_update_page(request, id):
    return render(request, "pages/instrument/update.html", {
        "instrument_id": int(id),
    })

#profile_api views
def profile_retrieve_page(request):
    return render(request, "pages/profile_api/retrieve.html", {})

def profile_update_page(request):
    return render(request, "pages/profile_api/update.html", {})

#report views
def report_list_page(request):
    return render(request, "pages/report/list.html", {})


def report_01_page(request):
    return render(request, "pages/report/report_01.html", {})

#sensor views
def sensor_retrieve_page(request, id):
    return render(request, "pages/sensor/retrieve.html", {
        'id': id,
    })
