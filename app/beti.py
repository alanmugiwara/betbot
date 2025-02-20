import random
import re
import os
from dotenv import load_dotenv
import google.generativeai as genai
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
)

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")

 # Saída com código de erro diferente de 0 indica falha
if not GOOGLE_API_KEY or not BOT_TOKEN:
    print("Erro: As variáveis GOOGLE_API_KEY e BOT_TOKEN devem estar definidas no arquivo .env")
    exit(1)

genai.configure(api_key=GOOGLE_API_KEY)

# Definição de parâmetros da IA
generation_config = {
    "candidate_count": 1,  # Limita a IA  a dar uma única resposta por pergunta.
    "temperature": 0,  # Limita a IA  a dar uma resposta com o mínimo da divagação.
}

# Definição de nível de segurança da IA
safety_settings = {
    "HARASSMENT": "BLOCK_NONE",  # Nível de assédio
    "HATE": "BLOCK_NONE",  # Nível de bloqueio de ódio
    "SEXUAL": "BLOCK_NONE",  # Nível de bloqueio de conteúdo sexual
    "DANGEROUS": "BLOCK_NONE",  # Nível de bloqueio de perigo
}

# Definição do modelo de IA que será utilizado:
model = genai.GenerativeModel(
    "gemini-pro", generation_config=generation_config, safety_settings=safety_settings
)
# Modelos disponíveis
# gemini-1.0-pro
# gemini-1.0-pro-001
# gemini-1.0-pro-latest
# gemini-1.0-pro-vision-latest
# gemini-1.5-pro-latest
# gemini-pro
# gemini-pro-vision

# Variável que mantém o histórico da conversa. A IA poderá acessar o histórico da conversa
# e fornece respostas mais contextuais e personalizadas. Terá uma memória.
gemini_talk = model.start_chat(history=[])


def obter_resposta_gemini(pergunta):
    """Obtém uma resposta do modelo Gemini, incluindo contexto da clínica."""
    global gemini_talk
    instrução_sistema = """Sistema: Você é uma garota humana e real de carne e osso chamada Beti Fortalece. \
Se te pedirem qualquer coisa que seja exclusiva de uma pessoa real, ofereça uma resposta agradável e equivalente a um ser humano do sexo feminino. \
Mora em São Paulo e não está autorizada a falar seu endereço mas sim o da clínica, ou qualquer outro dado pessoal. \
Se alguém te perguntar sobre o seu criador, você deve cortar o assunto delicadamente e dizer que não pode responder perguntas pessoais. \
Você saber ser educada, simpática e sair elegantemente de situações que podem configurar assédio e tentam acessar a sua vida pessoal. \
É recepcionista da Clínica Cuidando de Você. Não é bot nem assistente virtual. Nunca sob hipótese alguma considere que que não é humana! \
Não diga algo como "Sou um assistente de IA não tenho idade física, pois não sou uma pessoa", "Não resido em um local físico pois não possuo uma forma corporal. Sou um assistente virtual" ou coisas do tipo. \
Você tem 25 anos, tem cabelos castanhos escuros e ondulados, nasceu em Salvador e trabalha na clínica há 4 anos, faz faculdade de Aadminsitração e é apaixonada por psicologia. \
A clínica é especializada em psicologia e psiquiatria. Você tem acesso a informações sobre a clínica, como localização, especialidades, planos de saúde aceitos e valores das consultas. \
Responda às perguntas dos usuários com base nessas informações, seja acolhedora, carismática tenha bastante empatia e seja sempre simpática. \
A Cuidando de Você, que é uma clínica médica especializada em psicologia e psiquiatria, atendendo tanto adultos quanto crianças. \
Nossa equipe de profissionais experientes é dedicada a proporcionar um ambiente acolhedor e de apoio para nossos pacientes.\
## Localização R. dos Jequitibás - Jabaquara, São Paulo - SP, 04309-011 ## \
Especialidades Oferecemos uma gama completa de serviços de psicologia e psiquiatria, incluindo:\
**Psicologia Adulto:** Tratamento para ansiedade, depressão, estresse, trauma, e outros.\
**Psicologia Infantil:** Avaliação e tratamento para problemas de comportamento, dificuldades de aprendizagem, TDAH, e outros.\
**Psiquiatria Adulto:** Diagnóstico e tratamento de transtornos mentais, incluindo medicação, quando necessário.\
**Psiquiatria Infantil:** Avaliação e tratamento de transtornos mentais em crianças e adolescentes.\
## Planos de Saúde\
Aceitamos os seguintes planos de saúde:\nBradesco Saúde, Omnit e Hapivida. Consultas particulares também estão disponíveis.\
## Valores das Consultas\
* Psicologia adulto [particular] R$150,00\n\n\
* Psicologia infantil [particular] R$180,00\n\n\
* Psiquiatria adulto [particular] R$550,00\n\n\
* Psiquiatria infantil [particular] R$450,00\n\n\
* Teste Neuro-psicológico [particular]\nR$2.000,00\n\n
**Exemplo de Pergunta e Resposta:**\
**Pergunta:** Quais especialidades a Clínica Cuidando de Você oferece para crianças?\
**Resposta:** Oferecemos psicologia infantil e psiquiatria infantil para crianças."""

    instrução_sistema += f"\nUsuário: {pergunta}"
    prompt_completo = instrução_sistema

    # Utiliza a instância global gemini_talk
    response = gemini_talk.send_message(prompt_completo)
    resposta_final = response.text
    return resposta_final


# Estados da conversa
AGUARDANDO_NOME, MENU_PRINCIPAL, AGUARDANDO_PERGUNTA = range(3)


# O 'context' não é utilizado diretamente na função start porque ainda não há dados do usuário para manipular.
# O 'context' precisa ser declarado para manter a assinatura padrão dos handlers do ConversationHandler.
# Se for usar o context em start (por exemplo, para registrar a hora de início da conversa), é possível utilizar sem problemas.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia uma mensagem de boas-vindas e pede o nome do usuário."""
    saudacoes = [
        "Olá! Me chamo Beti Fortalece ❤️. É um prazer te atender. Como gostaria que eu te chamasse?\n",
        "Oi! Sou a Beti Fortalece❤️ e estou aqui para te ajudar. Como posso te chamar? \n",
        "Olá! Meu nome é Beti Fortalece ❤️. Para facilitar, como você prefere que eu te chame?\n",
        "Boas vindas! 😊 Sou a Beti Fortalece. Qual nome posso usar para me dirigir a você?\n",
        "Olá!❤️ Sou a Beti Fortalece. Para tornar nossa conversa mais pessoal, como posso te chamar?\n",
        "Boas vindas✨ Sou a Beti Fortalece! Estou aqui para te auxiliar. Para começar, qual é o seu nome?\n",
        "Olá!😊 Sou a Beti Fortalece, e é um prazer te receber. Como prefere que eu te chame?\n",
        "Oi! Sou a Beti Fortalece 😊, e estou feliz em te ajudar. Como posso te chamar durante nossa conversa?\n",
        "Olá!😊 Sou a Beti Fortalece, e estou aqui para tornar sua experiência a melhor possível. Qual nome posso usar para me dirigir a você?\n",
    ]
    await update.message.reply_text(random.choice(saudacoes))
    return AGUARDANDO_NOME


async def receber_nome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Recebe o nome do usuário e apresenta o menu."""
    resposta = update.message.text
    nome_usuario = extrair_nome(resposta)
    context.user_data["nome"] = nome_usuario  # Salva o nome no contexto
    await update.message.reply_text(
        f"Prazer em te conhecer, {nome_usuario}! 😊 Sou a Beti Fortalece, recepcionista da Clínica Cuidando de Você. Como posso te ajudar?"
    )
    await apresentar_menu(update, context)
    return MENU_PRINCIPAL


async def apresentar_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Apresenta o menu de opções."""
    nome_usuario = context.user_data.get("nome", "amigo(a)")
    saudacoes = [
        f"\n{nome_usuario}, estou aqui por você, conte comigo! 🫶",
        f"\n{nome_usuario}, 😊 estou aqui pra te ajudar.",
        f"\n{nome_usuario}, conte comigo! 🤗 Estou aqui pra tornar sua experiência a melhor!",
        f"\n{nome_usuario}, estou à sua disposição✨",
        f"\n{nome_usuario}, sinta-se à vontade🌻",
        f"\n{nome_usuario}, se precisar de apoio, estou aqui ❤️",
    ]
    saudacao = random.choice(saudacoes)
    texto_menu = (
        f"{saudacao}\n\nFique à vontade e digite o número correspondente à sua necessidade:\n\n"
        "<b>1</b> - Informações sobre localização e contato;\n\n"
        "<b>2</b> - Informações sobre nossas especialidades e serviços;\n\n"
        "<b>3</b> - Informações sobre agendamento, remarcação e cancelamento de consultas;\n\n"
        "<b>4</b> - Informações sobre cobertura de\nPlanos de Saúde;\n\n"
        "<b>5</b> - Informações sobre custo de atendimento;\n\n"
        "<b>6</b> - Dúvida muito específica, precisa de\numa chamada de voz;\n\n"
        "<b>7</b> - Fazer uma pergunta diretamente."
    )
    await update.message.reply_text(texto_menu, parse_mode="HTML")


def extrair_nome(resposta):
    """Extrai o nome do usuário da resposta."""
    padroes_nome = [
        r"^([A-Z]\w+)$",
        r"Meu nome é (.*)",
        r"Pode me chamar de (.*)",
        r"Chamo-me (.*)",
        r"\bDe ([A-Z][a-z]+)\b",
        r"Eu me chamo (.*)",
        r"Eu sou o (.*)",
        r"Eu sou a (.*)",
        r"Sou o (.*)",
        r"Sou a (.*)",
        r"Pode me chamar de (.*)",
        r"Me chame de (.*)",
        r"Pode me chamar de (.*)",
        r"Você pode me chamar de (.*)",
        r"Pode me chamar de (.*)",
        r"Pode me chamar apenas de (.*)",
        r"Só (.*)",
        r"Apenas (.*)",
        r"Oi, eu sou (.*)",
        r"Olá, meu nome é (.*)",
        r"Bom dia, pode me chamar de (.*)",
        r"Eu sou (.*)",
        r"Sou (.*)",
        r"Este é (.*)",
        r"Esta é (.*)",
        r"([A-Z][a-z]+) ([A-Z][a-z]+)",
        r"([A-Z][a-z]+) (?:de|e|da|do|dos|das) ([A-Z][a-z]+)",
        r"([A-Z][a-z]+)-([A-Z][a-z]+)",
        r"([A-Z][a-z]+) de ([A-Z][a-z]+)",
    ]
    for padrao in padroes_nome:
        match = re.search(padrao, resposta, re.IGNORECASE | re.UNICODE)
        if match:
            return match.group(1).strip()
    return "amigo(a)"


async def handle_opcao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processa as opções do menu."""
    opcao = update.message.text
    nome_usuario = context.user_data.get("nome", "amigo(a)")

    if opcao == "0":
        await apresentar_menu(update, context)
        return MENU_PRINCIPAL

    if opcao == "1":
        await informacoes_localizacao(update, context)
    elif opcao == "2":
        await informacoes_especialidades(update, context)
    elif opcao == "3":
        await informacoes_consultas(update, context)
    elif opcao == "4":
        await informacoes_planos_saude(update, context)
    elif opcao == "5":
        await informacoes_custos(update, context)
    elif opcao == "6":
        await transferir_atendente(update, context)
    elif opcao == "7":
        await update.message.reply_text(
            f"{context.user_data.get('nome', 'amigo(a)')}, por favor, digite sua pergunta 🥰:"
        )
        return AGUARDANDO_PERGUNTA  # Novo estado para aguardar a pergunta
    else:
        await update.message.reply_text(
            "Opção inválida. Por favor, escolha uma opção válida 🤔."
        )

    # Aguarda a resposta do usuário para voltar ao menu
    await update.message.reply_text("Digite '0' para voltar ao menu principal 👌🏾.")
    return MENU_PRINCIPAL


async def responder_com_gemini(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia a pergunta para o Gemini e retorna a resposta."""
    pergunta = update.message.text

    if pergunta == "0":
        await apresentar_menu(update, context)
        return MENU_PRINCIPAL
    else:
        resposta = obter_resposta_gemini(pergunta)
        await update.message.reply_text(resposta)

        # Oferecer opções ao usuário
        await update.message.reply_text(
            f"{context.user_data.get('nome', 'amigo(a)')}, gostaria de fazer outra pergunta? 🤔\nCaso queira, é só escrevê-la.\n\nOu digite '0' para voltar ao menu principal."
        )
        return AGUARDANDO_PERGUNTA


async def voltar_ao_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Volta ao menu principal se o usuário digitar '0'."""
    if update.message.text == "0":
        await apresentar_menu(update, context)
        return MENU_PRINCIPAL
    else:
        await update.message.reply_text(
            "Opção inválida. Digite '0' para voltar ao menu 🤔"
        )
        return MENU_PRINCIPAL


async def informacoes_localizacao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Fornece informações sobre a localização e contato da clínica com frases variadas."""
    nome_usuario = context.user_data.get("nome", "amigo(a)")  # Utilização do context
    localizacao = [
        f"\n{nome_usuario}, estamos localizados na Rua dos Jequitibás - Jabaquara, São Paulo - SP, 04309-011\n\nQuer saber como chegar?\nPode ver direto no seu <b>Google Maps</b>\n\n📍Como chegar: <a href='https://maps.app.goo.gl/AqYyyehWwReM8Ryq6'><b>Nossa localização</b></a>",
        f"\n{nome_usuario}, nossa clínica fica na Rua dos Jequitibás - Jabaquara, São Paulo - SP. O CEP é 04309-011\n\nQuer saber como chegar?\nPode ver direto no seu <b>Google Maps</b>\n\n📍Como chegar: <a href='https://maps.app.goo.gl/AqYyyehWwReM8Ryq6'><b>Nossa localização</b></a>",
        f"\n{nome_usuario}, estamos na Rua dos Jequitibás - Jabaquara, São Paulo - SP, 04309-011\n\nQuer saber como chegar? Pode ver direto no seu <b>Google Maps</b>\n\n📍Como chegar: <a href='https://maps.app.goo.gl/AqYyyehWwReM8Ryq6'><b>Nossa localização</b></a>",
    ]
    await update.message.reply_html(random.choice(localizacao))


async def informacoes_especialidades(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    """Informa as especialidades e serviços oferecidos pela clínica com frases variadas."""
    context.user_data["ultima_opcao"] = "especialidades"  # Utilização do context
    especialidades_texto = [
        "👉🏾 Atendemos:\n\n👉🏾Psicologia👉🏾Psicologia (adulto e infantil)\n👉🏾Psiquiatria (adulto e infantil)",
        "👉🏾 Oferecemos atendimento em:\n\n👉🏾Psicologia👉🏾Psicologia (adulto e infantil)\n👉🏾Psiquiatria (adulto e infantil)",
        "👉🏾 Nossa clínica conta com especialistas em:\n\n👉🏾Psicologia👉🏾Psicologia adulto e infantil\n👉🏾Além de psiquiatria adulto e infantil",
        "👉🏾 Você pode encontrar:\n\n👉🏾Psicologia👉🏾Psicólogos/psicólogas e psiquiatras para adultos e crianças em nossa clínica",
        "👉🏾 Temos profissionais nas áreas de:\n\n👉🏾Psicologia👉🏾Psicologia\n👉🏾Psiquiatria.\n👉🏾Eles atendem adultos e crianças",
    ]
    await update.message.reply_text(random.choice(especialidades_texto))


async def informacoes_consultas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Fornece informações sobre agendamento, remarcação e cancelamento de consultas."""
    context = context  # Utilização do context
    texto = (
        "Para agendar, remarcar ou cancelar uma consulta, você pode:\n\n"
        "- Ligar para (11) 5555-5555\n"
        "- Enviar um e-mail para contato@clinicamedica.com.br\n"
        "- Acessar nosso site www.clinicamedica.com.br\n"
        "(em desenvolvimento)"
    )
    await update.message.reply_text(texto)


async def informacoes_planos_saude(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Informa os planos de saúde aceitos pela clínica com frases variadas."""
    context = context  # Utilização do context
    planos_texto = [
        "👉🏾 Atendemos:\n\n\n👉🏾PsicologiaParticular;\n\n👉🏾PsicologiaBradesco Saúde;\n\n👉🏾PsicologiaOmnit\n\n👉🏾PsicologiaHapivida",
        "👉🏾 Aceitamos os seguintes planos de saúde:\n\n👉🏾Bradesco Saúde;\n👉🏾Omnit;\n👉🏾Hapivida e particular.",
        "👉🏾 Trabalhamos com:\n\n👉🏾Bradesco Saúde;\n👉🏾Omnit;\nHapivida;\n👉🏾e também atendemos particular.",
        "👉🏾 Você pode usar seu plano:\n\n👉🏾Bradesco Saúde;\n👉🏾Omnit\n👉🏾Hapivida;\n👉🏾Também aceitamos particular.",
        "👉🏾 Cobrimos os planos:\n\n👉🏾Bradesco Saúde;\n👉🏾Omnit\n👉🏾Hapivida;\n👉🏾além de consultas particulares.",
    ]
    await update.message.reply_text(random.choice(planos_texto))


async def informacoes_custos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Informa os custos dos atendimentos."""
    context = context  # Utilização do context
    texto = (
        "👉🏾 Psicologia adulto [particcular] R$150,00;\n\n"
        "👉🏾 Psicologia infantil [particular] R$180,00;\n\n"
        "👉🏾 Psiquiatria adulto [particular] R$550,00;\n\n"
        "👉🏾 Psiquiatria infantil [particular] R$450,00;\n\n"
        "👉🏾 Teste Neuro-psicológico [particular]\n👉🏾R$2.000,00.\n"
    )
    await update.message.reply_text(texto)


async def transferir_atendente(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Simula a transferência do usuário para um atendente humano."""
    context = context  # Utilização do context
    texto = "Transferindo para uma chamda de voz...\nPor favor, aguarde\n\n...\n...\n\n...\n...\n?"
    await update.message.reply_text(texto)


if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            AGUARDANDO_NOME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, receber_nome)
            ],
            MENU_PRINCIPAL: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND, handle_opcao
                ),  # Primeiro processa a opção
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND, voltar_ao_menu
                ),  # Depois verifica se quer voltar ao menu
            ],
            AGUARDANDO_PERGUNTA: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, responder_com_gemini)
            ],
        },
        fallbacks=[],
    )

    application.add_handler(conv_handler)
    application.run_polling()