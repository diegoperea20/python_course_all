#para ver cuanto se necesita https://www.moneygeek.com/compound-interest-calculator/
#0 en inicial en dar valor anual en  contibucion 
"""
initial Ammount= 0
CONtributions=1000  , elegir mennsual o anual

"""

valor_inicial =366775 #147250  # ya completada el 4% acumulado
ages=100
gasto_anual=12000
gasto_anual_aumentado=1.00

for  i in  range(ages):
    consumo_anual=valor_inicial-gasto_anual
    valor_inicial=consumo_anual*1.04
    porcentaje_aumntado=gasto_anual_aumentado+0.0003 #0.0005
    gasto_anual_aumentado=porcentaje_aumntado
    gasto_anual=gasto_anual*(porcentaje_aumntado)
    
    print(f'Año invertido:{i}')
    print(f'Año {i} consumo:{consumo_anual}')
    print(f'Año {i} reinversion:{valor_inicial}')
    print(f'Año {i} gasto aumentado:{gasto_anual}')
    print('TERMINA AÑO'.center(50,'-'))

