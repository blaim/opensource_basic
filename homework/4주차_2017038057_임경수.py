import operator


student = []


while True:
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('1.데이터 추가')
    print('2.데이터 검색')
    print('3.데이터 삭제')
    print('4.데이터 정렬')
    print('0.종료')
    select = input('0~4중 메뉴를 선택하세요 ==> ')
    select = int(select)
    if select==0:
        exit(0)
    elif select==1:

        if len(student)>5:
            print('5명 까지만 추가할 수 있습니다')

        else:
            stu_name = input('학생의 이름을 입력하세요 ==>')
            stu_number = input('학생의 학번을 입력하세요 ==>')
            stu_major = input('학생의 학과를 입력하세요 ==>')
            stu_kor = input('학생의 국어 성적을 입력하세요 ==>')
            stu_eng = input('학생의 영어 성적을 입력하세요 ==>')
            stu_math = input('학생의 수학 성적을 입력하세요 ==>')

            stu_total = int(stu_eng)+int(stu_math)+int(stu_kor)
            stu_ave =  round(stu_total/3.0, 3)

            if stu_ave >=95:
                stu_credit = 'A+'
            elif stu_ave >=90:
                stu_credit = 'A0'
            elif stu_ave >=85:
                stu_credit = 'B+'
            elif stu_ave >=80:
                stu_credit = 'B0'
            elif stu_ave >= 75:
                stu_credit = 'C+'
            elif stu_ave >=70:
                stu_credit = 'C0'
            elif stu_ave >=65:
                stu_credit = 'D+'
            else:
                stu_credit = 'F0'

            information = {'stu_name':stu_name, 'stu_number':stu_number, 'stu_major':stu_major,
                           'stu_kor':stu_kor, 'stu_eng':stu_eng, 'stu_math':stu_math,
                           'stu_credit':stu_credit, 'stu_total':stu_total, 'stu_ave':stu_ave}


            student.append(information)

    elif select==2:

        search = input('찾으려는 학생의 학번, 또는 이름을 입력해주세요 ==>')

        search_bool = False

        for stu in student:
            if search in stu.values():
                print('*************************')
                print('학생 이름: '+ stu['stu_name'])
                print('학번 : '+ stu['stu_number'])
                print('전공 : ' + stu['stu_major'])
                print('국어점수 : ' + stu['stu_kor'])
                print('영어점수 : ' + stu['stu_eng'])
                print('수학점수 : ' + stu['stu_math'])
                print('총점 : ' + str(stu['stu_total']))
                print('평균점수 : ' + str(stu['stu_ave']))
                print('학점 : ' + stu['stu_credit'])
                print('**************************')
                search_bool = True

        if search_bool == False:
            print('찾으려는 값이 존재하지 않습니다.')


    elif select==3:
        del_name = input('삭제하려는 학생의 이름을 입력하세요 ==>')
        del_number = input('삭제하려는 학생의 학번을 입력하세요 ==>')

        deleted = False

        for stu in student:
            if del_name in stu.values() and del_number in stu.values():
                del(stu)
                print(del_name+' 학생을 삭제했습니다.')
                deleted = True

        if deleted==False:
            print('이름이 '+del_name+' 이면서 학번이 '+del_number+' 인 학생을 찾지 못했습니다.' )

    elif select==4:
        print('이름으로 정렬 : 1')
        print('학번으로 정렬 : 2')
        sort = input('1과 2중 선택해주세요 ==>')

        sort = int(sort)

        if sort==1:
            student = sorted(student, key=operator.itemgetter('stu_name'))
            print(student)
        elif sort==2:
            student = sorted(student, key=operator.itemgetter('stu_number'))
            print(student)

    else:
        print('0에서4사이중 하나를 입력해 주세요')