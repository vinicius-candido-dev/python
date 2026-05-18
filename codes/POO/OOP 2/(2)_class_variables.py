class Empty:

    many = 0
    dolar =  5
    

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Empty.many += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply(self):
        self.pay = int(self.pay * self.dolar/100 + self.pay)


pessoa = Empty('vini','maia',5000)
pessoa1 = Empty('mari','victoria',6000)
'''
print(pessoa.pay)
pessoa.apply()
print(pessoa.pay)

print(Empty.__dict__)'''

print(Empty.many)