from msilib.schema import Media


n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
n3 = float(input('terceira nota: '))
n4 = float(input('quarta nota: '))
media = (n1+n2+n3+n4)/4
print('sua media final é {:.2}'.format(media))
if media >= 7:
    print('\033[325mAPROVADO!!')   
else:
    print('\033[31m REPROVOU!!')