# from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


def index(request):
    return_value(request)
    return HttpResponse(return_value(request))
    # this from work for test git and git hub 4/12/2021 4 pm


def return_value(request):
    with connection.cursor() as cursor:
        sql = ('''
            select * from phonebook.ph_book_test1
        ''')
        cursor.execute(sql)
        rows = cursor.fetchall()
    return rows
