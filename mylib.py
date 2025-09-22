class mainfunc:
    def myfunc(a, b):

        for i in range(b):
            for j in range(b):
                if i < j:
                    print(" ", end=' ')
                else:
                    print(a, end=' ')
            print(" ")
