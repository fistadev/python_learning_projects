euro = 5.87

# net_euro = input("Salário em Euro: ")
net_euro = 1500
net = float(net_euro) * euro
tax = float(net) * 0.2
gross = float(net) + float(tax)
gross_euro = gross / euro
tax_euro = tax / euro

print(f'Euro para o Real: {euro} reais')
print('------------------------------')
print(f'Salário líquido é em Euro €{net_euro}')
print(f'Imposto é em Euro €{tax_euro}')
print('------------------------------')
print(f'Salário líquido é R${net}')
print(f'Imposto é R${tax}')
print('------------------------------')
print(f'Salario total é R${gross}, salário líquido é R${net}, e o valor do imposto é R${tax}')
print(f'Salario total é €{gross_euro}, salário líquido é €{net_euro}, e o valor do imposto é €{tax_euro}')
print('------------------------------')
