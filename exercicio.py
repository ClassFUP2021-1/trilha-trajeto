import sys

num1 = int(sys.argv[1])
num2 = sys.argv[2]

cont = 0 
cont_num2 = 0
num1_valido = True

while True:
   
    if num1 < 0 or num1 > 9:
        num1_valido = False
        break        
    else:      
        unidade = num2 % 10          
        if num1 == unidade:
            cont = cont + 1     
        
        num2 = num2//10 
        cont_num2 = cont_num2 + 1  


if  num1_valido== True or (cont_num2 == 8 or cont_num2 == 9):
    print(cont)
elif (num1_valido == False) or (cont_num2 != 8) or (cont_num2 != 9):
    print('entrada invalida')
