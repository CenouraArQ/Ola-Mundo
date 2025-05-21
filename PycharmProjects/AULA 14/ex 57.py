sexo = str(input('Digite o seu sexo [Masculino/Feminino]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Digite novamente.')
    sexo = str(input('Digite o seu sexo [Masculino/Feminino]: ')).strip().upper()[0]
if sexo == 'M':
    print('O sexo Masculino foi registrado com sucesso.')
if sexo == 'F':
    print('O sexo Feminino foi registrado com sucesso.')
