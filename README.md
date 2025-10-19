[![made Language {generic badge}](https://img.shields.io/badge/Made%20with-Python-8A2BE2)](https://github.com/alanmugiwara)
![create date](https://img.shields.io/badge/Created-May%2011,%202024-8A2BE2)
[![Last update](https://img.shields.io/github/last-commit/alanmugiwara/betbot?color=8A2BE2&label=Last%20Commit)](https://github.com/alanmugiwara/alanmugiwara)
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

- [Python 3.12.3](https://www.python.org/downloads/release/python-3123//): Linguagem de programação utilizada;
- [Google AI Platform](https://aistudio.google.com/app/): Plataforma para acessar o modelo de linguagem Gemini Pro e gerar a API Key;
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot): Biblioteca Python para interagir com a API do Telegram;
- [google-generativeai](https://pypi.org/project/google-generativeai/): Biblioteca de AI do Gemini para interagir com a API do Google.

## Containerização

[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-Betbot-2496ED?logo=docker)](https://hub.docker.com/r/alanmugiwara/betbot)

O projeto está containerizado e disponível no Docker Hub. O container pode ser criado para arquiteturas arm64 e amd64. Para maiores informações de build, acesse a bsdge do DockerHub acima.

**Para baixar a imgem para arm64:**

```bash
docker pull --platform linux/arm64 alanmugiwara/betbot:0.3-arm64
```

**Para baixar a imgem para amd64**

```bash
docker pull --platform linux/amd64 alanmugiwara/betbot:0.3-amd64
```

## Implantação

Para que o bot fique online 24/7, além do container você também pode hospedar o script junto às variáveis de ambinente em um servidor. Plataformas como [Heroku](https://www.heroku.com/), [PythonAnywhere](https://www.pythonanywhere.com/), [Google Cloud Platform](https://cloud.google.com/) e [Amazon Web Services](https://aws.amazon.com/) oferecem opções de hospedagem para bots do Telegram. Consulte a documentação da plataforma escolhida para obter instruções de implantação.

## Personalização

- Adaptação de contexto: Modificando a variável `instrucao_sistema` na função `obter_resposta_gemini` para personalizar o contexto do bot com informações.
- Ajuste de personalidade: É possível incluir diferentes prompts e instruções no contexto para ajustar a personalidade do bot.
- Novas features: A biblioteca `python-telegram-bot` permite adicionar mais recursos ao bot, como botões, menus, etc.

## Demonstração

---

![Demonstração](https://github.com/alanmugiwara/alanmugiwara.github.io/blob/main/img/bet_demo.gif?raw=true)

Converse com a Beti [Beti Fortalece - Telgram Bot](https://t.me/BetiFortalece_bot)

## Compatbilidade

---

python-telegram-bot: A versão mínima do Python para utilizar a biblioteca é `a 3.7.`

google-generativeai: A versão mínima do Python para utilizar a biblioteca é `a 3.9.`

---

## Como Executar

1. **Obtenha uma chave de API do Google AI Platform:**

   - Acesse [Google AI Studio](https://aistudio.google.com/app/).
   - Crie uma chave de API e copie-a.

2. **Crie um bot no Telegram:**

   - No Telegram, procure por [@BotFather](https://t.me/BotFather).
   - Envie o comando `/newbot` e siga as instruções.
   - Anote o token de acesso que o BotFather fornecerá.

3. **Configure as variáveis de ambiente:**

   - No código-fonte, na arquivo "betbot\app\\.env", substitua `API-KEY` em GOOGLE_API_KEY pela sua chave de API do Gemini e `API-KEY` em BOT_TOKEN pelo token do seu bot do Telegram.

4. **Instale as bibliotecas necessárias:**
   - Abra o terminal na pasta raiz do projeto e rode o comando abaixo pra instalar as dependências.
   - Se o seu SO for baseado em Linux, apenas inverta as barras "\\" "/"
   ```bash
   cd \betbot\app
   pip install -r requirements
   ```

## Contato

Para dúvidas, sugestões ou problemas, entre em contato com Álan Cruz:

<a href="https://instagram.com/alancruz_tec" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"></a>
<a href="mailto:contato@alancruztec.com.br"><img loading="lazy" src="https://img.shields.io/badge/E--Mail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail"></a>
<a href="https://linkedin.com/in/alansilvadacruz" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin"></a>
<a href="https://alancruztec.com.br" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-My%20Website-%230077B5?style=for-the-badge&logo=wordpress&logoColor=white" alt="Website"></a>

## Licença

Este projeto é licenciado sob a licença [GPL-3.0 license] - consulte o arquivo [LICENÇA](https://github.com/alanmugiwara/betbot?tab=GPL-3.0-1-ov-file) para obter detalhes.

---
