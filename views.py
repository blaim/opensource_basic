'''made by 임경수'''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import Restaurant_Marker
import csv
from . import GraphMake
from . import board_add
from datetime import datetime
from . import review_add
from . import Babkinator_file

#기본 메뉴 출력
def main(request):

    return render(request, 'main.html')

#밥키네이터
def akinator(request):
    yes_num = 0
    no_num = 0;
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

    if request.method == 'POST' and request.POST.get('babkinator_code', False) !=False:
        bab_code = request.POST.get('babkinator_code', False)

        bab_class = Babkinator_file.Bapkinator()
        bab_class.open_csv()
        chosen_food = bab_class.make_food_list(bab_code)


        return render(request, 'results.html', {'results': chosen_food})




    return render(request, 'akinator.html', {'yes':yes_num, 'no':no_num})

#메뉴 검색하는 페이지
def menu_search(request):
    if request.method == 'POST' and request.POST.get('menu_name', False) != False:
        menu_name = request.POST['menu_name']
        filename = 'res_data.csv'
        names = []
        temp = []
        with open(filename, 'r') as file:
            cs_reader = csv.reader(file)
            lists = list(cs_reader)
            for v in lists:
                if menu_name in v[9]:
                    names.append(v)
                    temp.append(v[2])

        mapping = Restaurant_Marker.RestaurantMarker()
        #test_graph = GraphMake.GraphMake()

        for res in names:
            print(res[5] + ", " + res[6])
            latitude = float(res[5])
            longitude = float(res[6])

            mapping.restaurant_marker(res[2], latitude, longitude)
            #test_graph.Add(res[2], int(res[8]))


        #test_graph.Graph('graph');

        mapping.center_marker()
        mapping.save_html()

        return render(request, 'results.html', {'results':temp})
    #지도데이터 출력
    if request.method == 'POST' and request.POST.get('to_map', False) != False:
        return render(request, 'restaurant_marked_map.html')



    #세부정보 출력
    if request.method == 'POST' and request.POST.get('infor', False) !=False:
        res_name = request.POST.get('infor', False)
        filename = 'res_data.csv'
        with open(filename, 'r') as file:
            cs_reader = csv.reader(file)
            lists = list(cs_reader)


            for v in lists:
                if res_name in v[2]:
                    result = v
                    break


        return render(request, 'information.html', {'information':result})


    return render(request, 'menu_search.html')


#가격 검색하는 페이지
def price_search(request):
    if request.method =='POST' and request.POST.get('min_number', False)!=False:
        min_number = request.POST['min_number']
        max_number = request.POST['max_number']

        filename = 'res_data.csv'
        names = []
        temp = []
        with open(filename, 'r') as file:
            cs_reader = csv.reader(file)
            lists = list(cs_reader)
            for v in lists:
                if v[8] >= min_number and v[8] <= max_number:
                    names.append(v)
                    temp.append(v[2])

        mapping = Restaurant_Marker.RestaurantMarker()

        for res in names:

            latitude = float(res[5])
            longitude = float(res[6])

            mapping.restaurant_marker(res[2], latitude, longitude)
        mapping.center_marker()
        mapping.save_html()

        return render(request, 'results.html', {'results':temp})


    #지도데이터 화면에 출력
    if request.method == 'POST' and request.POST.get('to_map', False) != False:

        return render(request, 'restaurant_marked_map.html')

    #세부정보출력
    if request.method == 'POST' and request.POST.get('infor', False) !=False:
        res_name = request.POST.get('infor', False)
        filename = 'res_data.csv'
        with open(filename, 'r') as file:
            cs_reader = csv.reader(file)
            lists = list(cs_reader)


            for v in lists:
                if res_name in v[2]:
                    result = v
                    break


        return render(request, 'information.html', {'information':result})

    return render(request, 'price_search.html')


#식당이름 검색하는 페이지
def res_name_search(request):
    #리뷰, 평점 추가
    if request.method == 'POST' and request.POST.get('review_name', False)!=False:
        review_name = request.POST.get('review_name', False)
        grade = request.POST.get('grade', False)
        review = request.POST.get('review', False)

        add_review = review_add.review()
        add_review.reviewAdd(int(review_name), int(grade), review)
        print(review_name)
        print(grade)
        print(review)


    if request.method == 'POST' and request.POST.get('res_name', False)!=False:

        search_name = request.POST['res_name']
        filename = 'res_data.csv'
        temp = []
        names = []
        with open(filename, 'r') as file:
            cs_reader = csv.reader(file)
            lists = list(cs_reader)
            for v in lists:
                if search_name in v[2] and v[8] != '':
                    names.append(v)
                    temp.append(v[2])
        mapping = Restaurant_Marker.RestaurantMarker()


        for res in names:

            latitude = float(res[5])
            longitude = float(res[6])

            mapping.restaurant_marker(res[2], latitude, longitude)
        mapping.center_marker()
        mapping.save_html()

        return render(request, 'results.html', {'results': temp})

    if request.method == 'POST' and request.POST.get('to_map', False) != False:

        return render(request, 'restaurant_marked_map.html')





    #세부정보 페이지 출력
    if request.method == 'POST' and request.POST.get('infor', False) !=False:
        res_name = request.POST.get('infor', False)
        filename = 'res_data.csv'
        with open(filename, 'r') as file:
            cs_reader = csv.reader(file)
            lists = list(cs_reader)


            for v in lists:
                if res_name in v[2]:
                    result = v
                    break


        return render(request, 'information.html', {'information':result})

    return render(request, 'res_name_search.html')

#변경할 내용 보내는 기능
def request_correction(request):
    if request.method == 'POST' and request.POST.get('correction', False) != False:
        print('data confirmed')
        res_name = request.POST.get('res_name', False)
        correction = request.POST.get('correction', False)
        #print(res_name)
        #print(correction)
        res_name = res_name + str(datetime.today())
        add_correction = board_add.board()
        add_correction.boardAdd(res_name, correction)

        return render(request, 'main.html')

    return render(request, 'request_correction.html')


#세부사항 출력하는 페이지
def information(request):
    return render(request, 'restaurant_one_map.html')


