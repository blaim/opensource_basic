from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import main_form
import csv

yes_num = 0
no_num = 0


def main(request):
    if request.method == 'POST':

        data = request.POST['menu']
        if data == '아키네이터':
            return HttpResponseRedirect('/akinator')
        elif data == '식당이름검색':
            return HttpResponseRedirect('/ressearch')
        elif data == '식당메뉴검색':
            return HttpResponseRedirect('/mnsearch')
        elif data == '가격대검색':
            return HttpResponseRedirect('/prsearch')

    return render(request, 'main.html')

def akinator(request):
    global yes_num
    global no_num
    if request.method == 'POST':
        if request.POST.get('yes', ''):
            print(request.POST.get('yes', ''))
            yes_num += 1
        elif request.POST.get('no', ''):
            print(request.POST.get('no', ''))
            no_num += 1
        elif request.POST.get('reset', ''):
            yes_num=0
            no_num=0
        render(request, 'akinator.html', {'yes':yes_num, 'no':no_num})

    return render(request, 'akinator.html', {'yes':yes_num, 'no':no_num})

def menu_search(request):
    if request.method == 'POST':
        menu_name = request.POST['menu_name']
        filename = 'res_data.csv'
        menus = []
        with open(filename, 'r') as file:
            cs_reader = csv.reader(file)
            lists = list(cs_reader)
            for v in lists:
                if menu_name in v[8]:
                    menus.append(v[2])
        return render(request, 'menu_result.html', {'menus':menus})

    return render(request, 'menu_search.html')

def price_search(request):
    if request.method =='POST':
        min_number = request.POST['min_number']
        max_number = request.POST['max_number']
        filename = 'res_data.csv'
        prices = []
        with open(filename, 'r') as file:
            cs_reader = csv.reader(file)
            lists = list(cs_reader)
            for v in lists:
                if v[7] >= min_number and v[7] <= max_number:
                    prices.append(v[2])
        return render(request, 'price_result.html', {'price':prices})

    return render(request, 'price_search.html')

def res_name_search(request):
    if request.method == 'POST':
        search_name = request.POST['res_name']
        filename = 'res_data.csv'
        names = []
        find = []
        with open(filename, 'r') as file:
            cs_reader = csv.reader(file)
            lists = list(cs_reader)
            for v in lists:
                names.append(v[2])
            for rn in names:
                if search_name in rn:
                    find.append(rn)


        return render(request, 'res_name_result.html', {'find_name':find})


    return render(request, 'res_name_search.html')


