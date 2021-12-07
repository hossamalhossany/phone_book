from django.shortcuts import render
# from django.http import HttpResponse
# from django.db import connection

from .forms import contact_form


def index(request):
    html_page = "ph_book/index.html"
    return render(request, html_page, {contact_form})
    # return HttpResponse("ph_book/index.html")
#     return_value(request)
#     return HttpResponse(return_value(request))
#
#
# def return_value(request):
#     with connection.cursor() as cursor:
#         sql = ('''
#             insert into phonebook.ph_book_test1 (first_name, last_name) VALUES
#             ("ahmed","ali")
#         ''')
#         cursor.execute(sql)
#
#         sql = ('''
#             select * from phonebook.ph_book_test1
#         ''')
#         cursor.execute(sql)
#         rows = cursor.fetchall()
#     return rows
