# Juh Fortalece: chatbot da clínica 'Cuidando de Você'

Este é um chatbot para Telegram que simula uma recepcionista humana chamada Juh Fortalece, da Clínica fictícia Cuidando de Você. O bot usa o modelo de linguagem Gemini Pro da Google AI para responder a perguntas, fornecer informações sobre a clínica e interagir com os usuários de forma natural e acolhedora.

## Funcionalidades

- **Personalidade Simulada:** Juh Fortalece possui uma personalidade amigável e acolhedora, simulando uma recepcionista humana.
- **Informações da Clínica:** Fornecimento de informações sobre a localização, especialidades, planos de saúde aceitos e valores das consultas da clínica.
- **Menu Interativo:** Navegação por um menu de opções para acessar informações desejadas través de números.
- **Respostas Inteligentes:** Utilização do modelo Gemini Pro para responder a perguntas gerais de forma inteligente e contextualizada.
- **Detecção de Nomes:** Juh Fortalece usa expressões regulares para identificar o nome do usuário nas mensagens e personalizar as interações.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- [Google AI Platform](https://cloud.google.com/ai-platform/): Plataforma para acessar o modelo de linguagem Gemini Pro.
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot): Biblioteca Python para interagir com a API do Telegram.


Para que o bot fique online 24/7, você precisará hospedá-lo em um servidor. Plataformas como [Heroku](https://www.heroku.com/), [PythonAnywhere](https://www.pythonanywhere.com/), [Google Cloud Platform](https://cloud.google.com/) e [Amazon Web Services](https://aws.amazon.com/) oferecem opções de hospedagem para bots do Telegram. Consulte a documentação da plataforma escolhida para obter instruções de implantação.

Personalização
--------------

-   Adapte o contexto: Modifique a variável `instrucao_sistema` na função `obter_resposta_gemini` para personalizar o contexto do bot com as informações da sua clínica.
-   Ajuste a personalidade: Experimente diferentes prompts e instruções no contexto para ajustar a personalidade e o tom de voz do bot.
-   Adicione novas funcionalidades: Utilize a biblioteca `python-telegram-bot` para adicionar mais recursos ao seu bot, como botões, menus inline, etc.

Demonstração
------------

![Demonstração](https://github.com/alanmugiwara/alanmugiwara.github.io/blob/main/img/juh.gif?raw=true)

Converse com a Juh [Jug Fortalece Telgram Bot](https://t.me/juh_fortalece_bot).

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

Este projeto é licenciado sob a licença [GPL-3.0 license] - consulte o arquivo [LICENÇA](https://github.com/alanmugiwara/juh_bot?tab=GPL-3.0-1-ov-file) para obter detalhes.
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
   - No código-fonte do bot (jujuh-telegarm-bot.py), substitua `API-KEY` pela sua chave de API e `API-KEY` pelo token do seu bot.

4. **Instale as bibliotecas necessárias:**
   ```bash
   pip install python-telegram-bot google-generativeai
