inicial=1000000
ages=[1,2,3,4,5]
for age in ages:
    resultado=inicial*1.10
    inicial=resultado

    print(f'año: {age}')
    print(f'resultado:{resultado}')
    print('TERMINA AÑO'.center(50,'-'))
