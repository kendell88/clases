# def multipordos():
#  print("ingrese un numero")
#  num=int(input())
#  print(num*2)



# def resta():
#  print("ingrese un numero")
#  num=int(input())
#  print(num-5)
 
# multipordos()
# resta(5): 


# def validarfolio():
#     ticket_valido=False
#     folio_valido=123
#     print("ingrese el numero de folio")
#     n_folio=int(input())

#     if n_folio==folio_valido:
#         ticket_valido=True

# validafolio()        





def suma():
    print("ingrese dos numero")
    num1=int(input())
    num2=int(input())
    
    print(suma(num1,num2))
    print(resta(num1,num2))



# def suma (num1, num2):
#         resul=num1+num2
#         return resul
    
# print(suma(5,5))



def area(L,A):
    return(L*A)

def  perimetro(L,A):
    return (2*L+2*A)

Largo=int(input("ingresar largo"))
Ancho=int(input("ingresar ancho"))

print(area(Largo,Ancho))
print(perimetro(Largo,Ancho))


