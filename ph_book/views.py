from django.db import connection
from django.shortcuts import render
from .forms import contact_form
from .models import test1
def index(request):
    html_page = "ph_book/index.html"
    return render(request, html_page, {'contact_form': contact_form})
def put_data_to_databasa(request):
    test = test1()
    test.first_name = request.POST.get('first_name')
    test.last_name = request.POST.get('last_name')
    test.save()
    with connection.cursor() as cursor:
        sql = ''' select * from phonebook.ph_book_test1 '''
        cursor.execute(sql)
        rows = cursor.fetchall()
    html_page = "ph_book/index.html"
    return render(request, html_page, {'rows': rows})
