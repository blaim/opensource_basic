from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import Restaurant_Marker
import django
import csv

yes_num = 0
no_num = 0
names = []


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
    if request.method == 'POST' and request.POST.get('menu_name', False) != False:
        menu_name = request.POST['menu_name']
        filename = 'res_data.csv'
        names.clear()
        temp = []
        with open(filename, 'r') as file:
            cs_reader = csv.reader(file)
            lists = list(cs_reader)
            for v in lists:
                if menu_name in v[9]:
                    names.append(v)
                    temp.append(v[2])
        return render(request, 'results.html', {'results':temp})

    if request.method == 'POST' and request.POST.get('to_map', False) != False:
        mapping = Restaurant_Marker.RestaurantMarker()

        for res in names:

            print(res[5] + ", " + res[6])
            latitude = float(res[5])
            longitude = float(res[6])

            mapping.restaurant_marker(res[2], latitude, longitude)
        mapping.center_marker()
        mapping.save_html()
        print("succes")
        return render(request, 'restaurant_marked_map.html')

    return render(request, 'menu_search.html')

def price_search(request):
    if request.method =='POST' and request.POST.get('min_number', False)!=False:
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
        return render(request, 'results.html', {'results':prices})

    return render(request, 'price_search.html')

    if request.method == 'POST' and request.POST.get('to_map', False) != False:
        mapping = Restaurant_Marker.RestaurantMarker()

        for res in names:

            print(res[5] + ", " + res[6])
            latitude = float(res[5])
            longitude = float(res[6])

            mapping.restaurant_marker(res[2], latitude, longitude)
        mapping.center_marker()
        mapping.save_html()
        print("succes")
        return render(request, 'restaurant_marked_map.html')

def res_name_search(request):


    if request.method == 'POST' and request.POST.get('res_name', False)!=False:
        search_name = request.POST['res_name']
        filename = 'res_data.csv'
        temp = []
        names.clear()
        with open(filename, 'r') as file:
            cs_reader = csv.reader(file)
            lists = list(cs_reader)
            for v in lists:
                if search_name in v[2] and v[8] != '':
                    names.append(v)
                    temp.append(v[2])

        if request.method == 'POST' and request.POST.get('to_map', False) != False:
            mapping = Restaurant_Marker.RestaurantMarker()

            for res in names:
                print(res[5] + ", " + res[6])
                latitude = float(res[5])
                longitude = float(res[6])

                mapping.restaurant_marker(res[2], latitude, longitude)
            mapping.center_marker()
            mapping.save_html()
            print("succes")
            return render(request, 'restaurant_marked_map.html')

        return render(request, 'results.html', {'results':temp})

    if request.method == 'POST' and request.POST.get('to_map', False) != False:
        mapping = Restaurant_Marker.RestaurantMarker()

        for res in names:

            print(res[5] + ", " + res[6])
            latitude = float(res[5])
            longitude = float(res[6])

            mapping.restaurant_marker(res[2], latitude, longitude)
        mapping.center_marker()
        mapping.save_html()
        print("succes")
        return render(request, 'restaurant_marked_map.html')

    return render(request, 'res_name_search.html')


