from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse

from .forms import contact_form
from .models import test1

def index(request):
    html_page = "ph_book/index.html"
    return render(request, html_page, {'contact_form': contact_form})


def put_data_to_databasa(request):
    test1 = test1
    test1.first_name = request.POST.get('first_name')
    test1.last_name = request.POST.get('last_name')
    test1.save()
    # first_name = request.GET['first_name']
    # last_name = request['last_name']
    # with connection.cursor() as cursor:
        # sql = ('''
        #     insert into phonebook.ph_book_test1 (first_name , last_name) VALUES
        #     (request.POST.get('first_name'),request.POST.get('last_name'))
        #
        # ''')
        # return sql
        # cursor.execute(sql)
