first=input("Input three number, Fist=")
int(first)
second=input("input Second number=")
int(second)
third=input("input Third number=")
int(third)
if (first==second) and (second==third) and (third==first):
    print(3)
elif (first == second) or (second == third) or (third == first):
    print(2)
else: print(0)