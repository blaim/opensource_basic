import threading

class add_to_what():
    text = '1+2+3+.....+ '
    summary = 0
    add_num = 0
    def __init__(self, value):
        self.add_num = int(value)
        self.text += str(value)

    def add(self):
        for num in range(0, self.add_num + 1):
            self.summary += num
        print('%s = %d' %(self.text, self.summary))



add_1000 = add_to_what(1000)
add_100000 = add_to_what(100000)
add_10000000 = add_to_what(10000000)

print(add_1000.add_num)

th1 = threading.Thread(target = add_1000.add)
th2 = threading.Thread(target = add_100000.add)
th3 = threading.Thread(target = add_10000000.add)

th1.start()
th2.start()
th3.start()