from rich import print
from rich.table import Table
tabela = Table(title="Tabela de preços")

tabela.add_column('nome', justify="right")
tabela.add_column('preço', justify="center")
tabela.add_row("Lapis", "R$1,50")
tabela.add_row("Borracha",'R$4,50')

print(tabela)