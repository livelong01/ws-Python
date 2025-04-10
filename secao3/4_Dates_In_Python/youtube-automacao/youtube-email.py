# https://www.youtube.com/watch?v=4kPRm8D8Vx0
# 4 Automações com Python que Vão SALVAR Seu Tempo no Trabalho

# 1 AUTOMACAO DE E-MAILS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enviar_email():
    remetente = ''
    senha = ''  # refazer a senha
    destinatario = ''
    assunto = 'Relatório do dia de hoje'
    corpo = 'Este é um e mail automatico do relatorio de vendas do dia de hoje. Batemos a meta'

    mensagem = MIMEMultipart()
    mensagem['from'] = remetente
    mensagem['to'] = destinatario
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(corpo, "plain"))

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatario, mensagem.as_string())
    servidor.quit()
    print('Email enviado com sucesso.')


enviar_email()
