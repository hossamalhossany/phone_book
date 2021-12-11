from django.db import connection
from django.shortcuts import render


from .forms import contact_form


def index(request):
    html_page = "ph_book/index.html"
    return render(request, html_page, {'contact_form': contact_form})

def put_data_to_databasa():
  with connection.cursor() as cursor:
        sql = ('''
            insert into phonebook.ph_book_test1 (first_name, last_name) VALUES
            ("ahmed","ali")
        ''')
        cursor.execute(sql)
