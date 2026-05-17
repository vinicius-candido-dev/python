
def all():
    with open("birthdays.txt",'r',encoding="utf-8") as f:
        for line in f:
            lin = line.strip().split(',')
            obj = {
            "day": lin[0],
            "Month": lin[1],
            "Name": lin[2] }
            print(f"A pessoa {obj['Name']} faz aniversário  no mês {obj['Month']} e no dia {obj['day']}")
            

print(all())