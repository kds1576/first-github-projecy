a = """
개발자 : Milk

기계 클래스

1. 제품명
2. 제조 번호 (규칙 : 만들어인 날짜 + 만들어진 순서, 8자리  ex)  03270001   )
3. 제조사

"""

import time

class Machine:

    date = time.strftime("%m%d", time.localtime(time.time()))
    num = 0

    def __init__(self, person):
        Machine.num += 1

        self.__person = person
        self.__name = "model 1"
        self.__num = str(Machine.date) + str(Machine.num).zfill(4)
        self.__fac = "M machine"

    def instruction(self):
        print("{}의 제품" .format(self.__person))
        print("모델명 : {}, 제품번호 : {}, 제조사 : {}" .format(self.__name, self.__num, self.__fac))


print(a)

m1 = Machine("kim")
m2 = Machine("Park")
m3 = Machine("Lee")
m4 = Machine("Choi")

m1.instruction()
m2.instruction()
m3.instruction()
m4.instruction()