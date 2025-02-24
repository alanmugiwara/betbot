[![made Language {generic badge}](https://img.shields.io/badge/Made%20with-Python%203-8A2BE2)](https://github.com/alanmugiwara)
[![create date](https://badges.pufler.dev/created/alanmugiwara/betbot?color=8A2BE2)](https://github.com/alanmugiwara)
[![last update date](https://badges.pufler.dev/Updated/alanmugiwara/betbot?color=8A2BE2)](https://github.com/alanmugiwara)
[![Commits Badge](https://img.shields.io/github/commit-activity/m/alanmugiwara/betbot.svg?color=8A2BE2)](https://github.com/alanmugiwara)
[![last release](https://img.shields.io/github/v/release/alanmugiwara/betbot?color=8A2BE2&label=release&style=flat)](https://github.com/alanmugiwara)
[![downloads counter](https://img.shields.io/github/downloads/alanmugiwara/betbot/total?color=8A2BE2)](https://github.com/alanmugiwara)

[![contributors](https://img.shields.io/github/contributors/alanmugiwara/betbot?color=8A2BE2)](https://github.com/alanmugiwara)
[![issues counter](https://img.shields.io/github/issues/alanmugiwara/betbot?color=8A2BE2)](https://github.com/alanmugiwara)
[![repo size](https://img.shields.io/github/repo-size/alanmugiwara/betbot?color=8A2BE2)](https://github.com/alanmugiwara)
[![directory size](https://img.shields.io/github/directory-file-count/alanmugiwara/betbot?color=8A2BE2)](https://github.com/alanmugiwara)
[![maintainability](https://api.codeclimate.com/v1/badges/6982b78246699cd2458f/maintainability)](https://codeclimate.com/github/alanmugiwara/betbot/maintainability) 
[![test Coverage](https://api.codeclimate.com/v1/badges/6982b78246699cd2458f/test_coverage)](https://codeclimate.com/github/alanmugiwara/betbot/test_coverage)

# Beti Fortalece: chatbot da clínica 'Cuidando de Você'

Este é um chatbot para Telegram que simula uma recepcionista humana chamada Beti Fortalece, da Clínica fictícia Cuidando de Você. O bot usa o modelo de linguagem Gemini Pro da Google AI para responder a perguntas, fornecer informações sobre a clínica e interagir com os usuários de forma natural e acolhedora. 

Beti Fortacele é uma sátira ao hit 'Beth fortalece' imortalizado em 2016 em terras soteropolitanas.

[Beti Fortacele no youtube](https://www.youtube.com/watch?v=sPK7JUE68dU)

## Funcionalidades

- **Personalidade Simulada:** A Beti possui uma personalidade amigável e acolhedora, simulando uma recepcionista humana.
- **Informações da Clínica:** Fornecimento de informações sobre a localização, especialidades, planos de saúde aceitos e valores das consultas da clínica.
- **Menu Interativo:** Navegação por um menu de opções para acessar informações desejadas através de números.
- **Respostas Inteligentes:** Utilização do modelo Gemini Pro para responder a perguntas gerais de forma inteligente e contextualizada.
- **Detecção de Nomes:** A Beti usa expressões regulares para identificar o nome do usuário nas mensagens e personalizar as interações.

## Tecnologias Utilizadas

- [Python](https://cloud.google.com/ai-platform/): Linguagem de programação principal.
- [Google AI Platform](https://aistudio.google.com/app/): Plataforma para acessar o modelo de linguagem Gemini Pro e gerar a API Key.
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot): Biblioteca Python para interagir com a API do Telegram.
- [google-generativeai](https://pypi.org/project/google-generativeai/): Biblioteca de AI do Gemini para interagir com a API do Google.

## Containerização
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-Betbot-2496ED?logo=docker)](https://hub.docker.com/repository/docker/alanmugiwara/betbot/general)

O projeto está containerizado e disponível no Docker Hub. O container pode ser criado para arquiteturas arm64 e amd64.

Para executar o container:
```
docker pull alanmugiwara/betbot
docker run -d --name betbot alanmugiwara/betbot
```

## Implantação
Para que o bot fique online 24/7, além do container você também pode hospedar o script junto às variáveis de ambinente em um servidor. Plataformas como [Heroku](https://www.heroku.com/), [PythonAnywhere](https://www.pythonanywhere.com/), [Google Cloud Platform](https://cloud.google.com/) e [Amazon Web Services](https://aws.amazon.com/) oferecem opções de hospedagem para bots do Telegram. Consulte a documentação da plataforma escolhida para obter instruções de implantação.

Personalização
--------------

-   Adapte o contexto: Modifique a variável `instrucao_sistema` na função `obter_resposta_gemini` para personalizar o contexto do bot com as informações do seu interesse.
-   Ajuste a personalidade: Experimente diferentes prompts e instruções no contexto para ajustar a personalidade do bot.
-   Adicione novas funcionalidades: Utilize a biblioteca `python-telegram-bot` para adicionar mais recursos ao seu bot, como botões, menus inline, etc.

## Demonstração
------------

![Demonstração](https://github.com/alanmugiwara/alanmugiwara.github.io/blob/main/img/bet_demo.gif?raw=true)

Converse com a Beti [Beti Fortalece - Telgram Bot](https://t.me/BetiFortalece_bot)

## Compatbilidade
-------

python-telegram-bot: A versão mínima do Python para utilizar a biblioteca é `a 3.7.`

google-generativeai: A versão mínima do Python para utilizar a biblioteca é `a 3.9.`
* * * * *

## Como Executar

1. **Obtenha uma chave de API do Google AI Platform:**
   - Acesse [Google AI Studio](https://aistudio.google.com/app/).
   - Crie uma chave de API e copie-a.

2. **Crie um bot no Telegram:**
   - No Telegram, procure por [@BotFather](https://t.me/BotFather).
   - Envie o comando `/newbot` e siga as instruções.
   - Anote o token de acesso que o BotFather fornecerá.

3. **Configure as variáveis de ambiente:**
   - No código-fonte, na arquivo "betbot\app\.env", substitua `API-KEY` em GOOGLE_API_KEY pela sua chave de API do Gemini e `API-KEY` em BOT_TOKEN pelo token do seu bot do Telegram.

4. **Instale as bibliotecas necessárias:**
   - Abra o terminal na pasta raiz do projeto e rode o requirements.
   ```bash
   pip install -r requirements
    ```

Contato
-------

Para dúvidas, sugestões ou problemas, entre em contato com Álan Cruz:

<div>
<a href="https://instagram.com/alanmugiwaras" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"></a>
<a href="mailto:alanufrb@gmail.com"><img loading="lazy" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail"></a>
<a href="https://linkedin.com/in/alansilvadacruz" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin"></a>
</div>

Licença
-------

Este projeto é licenciado sob a licença [GPL-3.0 license] - consulte o arquivo [LICENÇA](https://github.com/alanmugiwara/betbot?tab=GPL-3.0-1-ov-file) para obter detalhes.
* * * * *
