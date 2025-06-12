import time
import pywhatkit as kit
from datetime import datetime
import pandas as pd
import os

def enviar_mensagens_whatsapp():
    # Carregar lista de contatos (CSV ou Excel)
    try:
        contatos_df = pd.read_csv('contatos.csv')  # Ou pd.read_excel('contatos.xlsx')
    except FileNotFoundError:
        print("Arquivo 'contatos.csv' não encontrado!")
        return
    
    # Verificar colunas necessárias
    if 'numero' not in contatos_df.columns or 'nome' not in contatos_df.columns:
        print("O arquivo precisa ter colunas 'numero' e 'nome'")
        return
    
    # Carregar mensagem personalizada
    try:
        with open('mensagem.txt', 'r', encoding='utf-8') as file:
            mensagem_template = file.read()
    except FileNotFoundError:
        print("Arquivo 'mensagem.txt' não encontrado!")
        return
    
    # Verificar se há arquivo/imagem para enviar
    anexo_path = None
    if os.path.exists('anexo.pdf'):  # Pode ser .pdf, .jpg, .png, etc
        anexo_path = 'anexo.pdf'
    
    # Configurações
    espera_entre_envios = 30  # segundos (evitar bloqueio)
    hora_atual = datetime.now()
    
    # Loop pelos contatos
    for index, contato in contatos_df.iterrows():
        try:
            numero = contato['numero']
            nome = contato['nome']
            
            # Personalizar mensagem
            mensagem = mensagem_template.replace("{nome}", nome)
            
            print(f"Enviando para {nome} ({numero})...")
            
            # Enviar mensagem de texto
            kit.sendwhatmsg_instantly(
                phone_no=numero, 
                message=mensagem,
                wait_time=15,
                tab_close=True
            )
            
            time.sleep(5)  # Espera para garantir que a mensagem foi enviada
            
            # Se houver anexo
            if anexo_path:
                if anexo_path.endswith(('.jpg', '.jpeg', '.png')):
                    kit.sendwhats_image(
                        receiver=numero,
                        img_path=anexo_path,
                        caption=mensagem,
                        tab_close=True
                    )
                else:
                    # Para documentos (PDF, etc)
                    print("Envio de documentos não suportado diretamente pelo pywhatkit")
                    # Considere usar outra biblioteca como webwhatsapi
            
            print(f"Mensagem enviada para {nome}!")
            
            # Espera entre envios
            time.sleep(espera_entre_envios)
            
        except Exception as e:
            print(f"Erro ao enviar para {contato['nome']}: {str(e)}")
            continue

if __name__ == "__main__":
    enviar_mensagens_whatsapp()