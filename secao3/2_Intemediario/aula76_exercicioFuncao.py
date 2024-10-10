# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def fatorizacao(multiplicador):
    def conta(multiplicado):
        return multiplicador * multiplicado
    return conta


duplicar = fatorizacao(2)
triplicar = fatorizacao(3)
quadruplicar = fatorizacao(4)

print(duplicar(15))
print(triplicar(15))
print(quadruplicar(15))
# def multiply(numberA):
#     def equation(numberB):
#         return f'{numberA:>2} x {numberB:>2} = {numberA * numberB:>2}'
#     return equation
 
# multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for operator in multipliers:
#     print(f"\nTabuada de {operator}")
#     equation = multiply(operator)
#     for number in values:
#         print(equation(number))
#     print()
#     if operator == multipliers[-1]:
#         break
#     print("=" * 30)