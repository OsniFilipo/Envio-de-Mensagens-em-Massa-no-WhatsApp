# 🔥 Envio de Mensagens em Massa no WhatsApp

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![PyWhatKit](https://img.shields.io/badge/PyWhatKit-5.4-green)
![License](https://img.shields.io/badge/License-MIT-red)

<div align="">
  <img src="https://www.interakt.shop/wp-content/uploads/2024/04/Bulk-Messages.png" alt="Demo" width="600">
</div>

Ferramenta para envio automatizado de mensagens via WhatsApp com personalização em massa


## 📌 Recursos Principais

- ✨ Envio **personalizado** usando `{variaveis}`
- 📁 Suporte a **anexos** (imagens/PDFs)
- ⏱️ Controle de **intervalo entre envios**
- 📊 Relatório de **envios bem-sucedidos/falhas**
- 📋 Interface simples via **arquivos CSV/TXT**

## Pré-requisitos

- Python 3.8+
- WhatsApp Web logado
- Navegador Chrome/Firefox

## 📋 Configuração

1. Prepare seu arquivo ```contatos.csv```:

```
numero,nome
5511999999999,João Silva
5511888888888,Maria Souza
```

2. Crie seu ```mensagem.txt```:

```
Olá {nome}, tudo bem?
Esta é uma mensagem personalizada.
```

3. (Opcional) Adicione um arquivo ```anexo.jpg``` ou ```anexo.pdf``` na pasta

🚀 Como Usar

1.Abra o WhatsApp Web no seu navegador e faça login

2.Execute o script:

```
python whatsapp_sender.py
```

3.Siga as instruções no terminal

## ⚠️ Limitações Importantes

O WhatsApp pode bloquear envios em massa

Limite de ~30-40 mensagens/hora para evitar bloqueios

Requer que você mantenha a janela do navegador aberta

Não funciona com números que não estão na sua lista de contatos

## 📄 Estrutura de Arquivos

```
whatsapp-bulk-sender/
├── whatsapp_sender.py    # Script principal
├── contatos.csv          # Lista de contatos (exemplo)
├── mensagem.txt          # Modelo de mensagem (exemplo)
├── anexo.jpg             # Arquivo opcional para anexar
├── requirements.txt      # Dependências
└── README.md             # Este arquivo
```