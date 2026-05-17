class Empty:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


pessoa = Empty('vini','maia',5000)
print(pessoa.email)
print(pessoa.pay)