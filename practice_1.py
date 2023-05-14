def gradingstudents(grades):
    for i in range(len(grades)):
        num = round(grades[i]/5) * 5 
        if num % 5 == 0 and grades[i] > 33 :
            print(num)
        else:
            print(grades[i])

s = list(map(int, input().split(" ")))
gradingstudents(s)