'''

PARA CRIAR O AMBIENTE VIERTUAL USE:

python -m venv venv

para ativar o ambiente virtual: venv\Scripts\activate
para desativar o ambiente virtual: deactivate

A vantagem do ambiente virtual é que vc tem uma mini BOLHA DO TEMPO, 
onde tem um python com a versao congelada e os arquivos do projeto
que vc trabalhou e ela fica APENAS ali. 
Fazendo assim, a versao e a compatibilidade do seu projeto, sera sempre FUNCIONAL.

pip install pymysql (pode mudar o mysql pra outra coisa)
pip install pymysql==1.0.0 (escolhe a versao depois do igual.)
pip uninstall pymysql (desinstala o pymysql)
pip freeze mostra o q vc tem instalado na maquina virtual

se vc tiver num projeto e adc varios modulos e precisa das versoes deles no futuro
voce pode, ao inves de enviar tudo pro repositorio (git), que vai ficar mt pesado,
pode criar o arquivo "REQUIReMENTS", onde vai salvar apenas as versoes dos modulos em um txt
assim, preservando as versoes.

qd quiser basta chamar:
pip install [modulox]==[numero da versao.]

para criar esse arquivo txt, basta usar o COMANDO:

pip freeze > requirements.txt #freeze serve pra explicitar as versoes de todos
os modulos externos q vc ta utilizando.

PARA CHAMAR DE VOLTA O AMBIENTE VIRTUAL JA CRIADO
ATRAVES DO REQUIRIMENTS.TXT basta usar:

pip install -r .\requirements.txt
"-r de requirements"

SE QUISER ATUALIZAR AS VERSOES DOS MODULOS BASTA:

python -m pip install pip --upgrade


'''
