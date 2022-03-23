print("Quiz-2 Task-3. Kim Yoon Hyuk 20165732")
money = 100000
interest = 0.05
year = 10
for i in range(year): money += interest * money
print(int((money//100)*100))