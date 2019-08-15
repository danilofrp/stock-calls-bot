# Stock Calls Bot
Este reposítório tem como objetivo o desenvolvimento de scrappers e de um bot para notificações de call de ações e opções da Bovespa.

## Requisitos

 - [Python 3.7](https://www.python.org/downloads/)
 - Conta disponível no site do se deseja extrair os calls.
 - Bot no telegram configurado. (Veja [aqui](https://core.telegram.org/bots) como criar e configurar um bot). Será necessário o token do bot e o chat_id de cada usuário para o qual se deseja enviar uma mensagem. 


## Instalação
 1. Clonar o repositório com `git clone https://github.com/danilofrp/stock-calls-bot`.
 2. Adicionar as credenciais do site ao arquivo `src/credentials/login-credentials.json` seguindo o seguinte modelo:
 ```javascript
 {
    "email": "example@example.com",
    "password": "Ex4mpl3_P@ssw0rd"
 }
 ```
 3. Adicionar as configurações do bot do telegram ao arquivo `src/bot_specs/bot_config.json`, conforme exemplo abaixo. Cada chat_id é um usuário para o qual será enviada uma mensagem.
 
 ```javascript
 {
    "token": "123456789:your_bot_token_here",
    "chat_ids": [
      "12345678",
      "98765432"
    ]
  }
 ```
 4. Criar um [ambiente virtual](https://docs.python.org/3/library/venv.html) no python 3. Após criado, ativar este ambiente.
 5. Instalar, utilizadno o [Pip](https://pip.pypa.io/en/stable/), os pacotes listados no arquivo `requirements.txt`. Utilizar o comando `pip install -r requirements.txt`
 6. Atualizar os paths nos arquivos `run_scrapper.sh`
 
 7. (Opcional) Para rodar o script regularmente, editar o crontab com o comando crontab -e e inserir a linha contida no arquivo `crontab.txt`, lembrando de atualizar os paths necessários. Este exemplo faz com que o script rode a cada 5 minutos e, em caso de erro ou warning, escreva a saída no arquivo `cron.log`.
 ```bash
 */5 * * * * /home/danilofrp/workspace/stock-calls-bot/run_scrapper.sh > /home/danilofrp/workspace/stock-calls-bot/cron.log 2>&1
 ```
 
 
 ## Trabalhos Futuros
 No presente momento, este script verifica apenas os calls dados no curso [A Grande Tacada](http://blog.fernandogoes.com/curso-online-de-opcoes-grande-tacada/). O objetivo expandi-lo para verificar calls de outras fontes, tanto abertas quanto fechadas.  
