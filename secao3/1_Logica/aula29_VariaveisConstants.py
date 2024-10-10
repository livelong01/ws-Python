"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
    No python nao existe constante de verdade
    entao o que os programadores fazem é
    por a variavel em letras maiusculas
    SINALIZANDO que sao CONSTANTES!!! 
    exemplo: 
"""
velocidade = 65
local_carro = 101

RADAR_1 = 60 #velocidade maxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 esta
RADAR_RANGE = 1 # A distancia onde o radar pega

#VARIAVEIS ABAIXO PARA REDUZIR O CODIGO:
vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1\
        and vel_carro_pass_radar_1 
#uso das variaveis criadas acima: (RESUMIDAS)
if vel_carro_pass_radar_1:
    print("Velocidade carro passou do radar 1")

if carro_passou_radar_1:
    print("Carro passou no radar 1")

if carro_multado_radar_1:
    print("carro multado em radar 1")

'''
IMPORTANTE, SE VC POR O CURSOR DO MOUSE EM CIMA DA
VARIAVEL, E APERTAR F2. VOCE PODE ALTERAR O NOME DA VARIAVEL
E ISSO FAZ COM QUE O NOME MUDE EM TODOS OS LUGARES QUE ELA FOI
USADA!!!!

'''


