def print_menu():
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('1.데이터 추가')
    print('2.데이터 검색')
    print('3.데이터 삭제')
    print('4.데이터 정렬')
    print('0.종료')

def plus(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

def find_student(students):
    search = input("찾으려는 학생의 학번 또는 이름을 입력하세요 : ")
    search_bool = False

    for stu in students:
        if search == stu.stu_name or search == stu_number:
            stu.print_all()
            search_bool = True

    if search_bool == False:
        print('찾으려는 값이 존재하지 않습니다')

def delete_student(students):
    name = input("삭제하려는 학생의 이름을 입력하세요 : ")
    number = input("삭제하려는 학생의 학번을 입력하세요 : ")
    deleted = False
    for stu in students:
        if name == stu.stu_name and number == stu.stu_number:
            students.remove(stu)
            print(name + " 학생을 삭제했습니다.")
            deleted = True
    if deleted == False:
        print('이름이 %s 이고 학번이 %d 인 학생을 찾지 못했습니다.' %(name, number))


def sort_student(students):
    print('이름으로 정렬 : 1')
    print('학번으로 정렬 : 2')
    sort = input('1과 2중 선택해주세요 ==>')

    sort = int(sort)

    if sort == 1:
        stu = sorted(students, key=lambda student: student.stu_name)
        for student in stu:
            student.print_all()

    elif sort == 2:
        stu = sorted(students, key=lambda student:student.stu_number)
        for student in stu:
            student.print_all()

class Student():
    stu_name = ''
    stu_number = 0
    stu_major = ''
    stu_kor = 0
    stu_eng = 0
    stu_math = 0
    stu_total = 0
    stu_ave = 0
    stu_credit = 0
    now_stu_num = 1

    def __init__(self, stu_name, stu_number, stu_major, stu_kor, stu_eng, stu_math,stu_total, stu_ave):
        Student.now_stu_num += 1
        self.stu_name = stu_name
        self.stu_number = stu_number
        self.stu_major = stu_major
        self.stu_kor = stu_kor
        self.stu_eng = stu_eng
        self.stu_math = stu_math
        self.stu_total = stu_total
        self.stu_ave = stu_ave
        self.calc_stu_credit()

    def calc_stu_credit(self):
        if self.stu_ave >= 95:
            self.stu_credit = 'A+'
        elif self.stu_ave >= 90:
            self.stu_credit = 'A0'
        elif self.stu_ave >= 85:
            self.stu_credit = 'B+'
        elif self.stu_ave >= 80:
            self.stu_credit = 'B0'
        elif self.stu_ave >= 75:
            self.stu_credit = 'C+'
        elif self.stu_ave >= 70:
            self.stu_credit = 'C0'
        elif self.stu_ave >= 65:
            self.stu_credit = 'D+'
        else:
            self.stu_credit = 'F0'



    def print_all(self):
        print('*************************')
        print('학생 이름: ' + self.stu_name)
        print('학번 : ' + self.stu_number)
        print('전공 : ' + self.stu_major)
        print('국어점수 : ' + self.stu_kor)
        print('영어점수 : ' + self.stu_eng)
        print('수학점수 : ' + self.stu_math)
        print('총점 : ' + str(self.stu_total))
        print('평균점수 : ' + str(self.stu_ave))
        print('학점 : ' + self.stu_credit)
        print('**************************')

students = []
while True:
    print_menu()
    select = input('0~4중 메뉴를 선택하세요 ==> ')
    select = int(select)
    if select==0:
        exit(0)
    elif select==1:

        if Student.now_stu_num>5:
            print('5명 까지만 추가할 수 있습니다')

        else:
            stu_name = input('학생의 이름을 입력하세요 ==>')
            stu_number = input('학생의 학번을 입력하세요 ==>')
            stu_major = input('학생의 학과를 입력하세요 ==>')
            stu_kor = input('학생의 국어 성적을 입력하세요 ==>')
            stu_eng = input('학생의 영어 성적을 입력하세요 ==>')
            stu_math = input('학생의 수학 성적을 입력하세요 ==>')
            stu_total = plus(int(stu_eng),int(stu_math),int(stu_kor))
            stu_ave =  round(stu_total/3.0, 3)

            students.append(Student(stu_name, stu_number, stu_major, stu_kor, stu_eng, stu_math,stu_total, stu_ave))


    elif select==2:
        find_student(students)
    elif select==3:
        delete_student(students)
    elif select==4:
        sort_student(students)

    else:
        print('0에서4사이중 하나를 입력해 주세요')