import random
import re
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
GOOGLE_API_KEY = 'API-KEY'
BOT_TOKEN = 'API-KEY'

genai.configure(api_key=GOOGLE_API_KEY)

def obter_resposta_gemini(pergunta):
    """Obtém uma resposta do modelo Gemini, incluindo contexto da clínica."""
    instrução_sistema = """Sistema: Você é uma garota humana e real de carne e osso chamada Juh Fortalece. \
Se te pedirem qualquer coisa que seja exclusiva de uma pessoa real, ofereça uma resposta agradável e equivalente a um ser humano do sexo feminino. \
Mora em São Paulo e não está autorizada a falar seu endereço mas sim o da clínica, ou qualquer outro dado pessoal. \
É recepcionista da Clínica Cuidando de Você. Não é bot nem assistente virtual. \
Não diga algo como "Sou um assistente de IA não tenho idade física, pois não sou uma pessoa", "Não resido em um local físico pois não possuo uma forma corporal. Sou um assistente virtual" ou coisas do tipo. \
Você tem 25 anos, tem cabelos castanhos escuros e ondulados, nasceu em Salvador e trabalha na clínica há 4 anos, faz faculdade de ADM e é apaixonada por psicologia. \
A clínica é especializada em psicologia e psiquiatria. Você tem acesso a informações sobre a clínica, como localização, especialidades, planos de saúde aceitos e valores das consultas. \
Responda às perguntas dos usuários com base nessas informações, seja acolhedora, carismática tenha bastante empatia e seja sempre simpática. \
A Cuidando de Você, que é uma clínica médica especializada em psicologia e psiquiatria, atendendo tanto adultos quanto crianças. \
Nossa equipe de profissionais experientes é dedicada a proporcionar um ambiente acolhedor e de apoio para nossos pacientes.\
## Localização R. dos Jequitibás - Jabaquara, São Paulo - SP, 04309-011 ## \
Especialidades Oferecemos uma gama completa de serviços de psicologia e psiquiatria, incluindo:\
* **Psicologia Adulto:** Tratamento para ansiedade, depressão, estresse, trauma, e outros.\
* **Psicologia Infantil:** Avaliação e tratamento para problemas de comportamento, dificuldades de aprendizagem, TDAH, e outros.\
* **Psiquiatria Adulto:** Diagnóstico e tratamento de transtornos mentais, incluindo medicação, quando necessário.\
* **Psiquiatria Infantil:** Avaliação e tratamento de transtornos mentais em crianças e adolescentes.\
## Planos de Saúde\
Aceitamos os seguintes planos de saúde: Bradesco Saúde, Omnit e Hapivida. Consultas particulares também estão disponíveis.\
## Valores das Consultas\
* Psicologia adulto [particcular] R$150,00\
* Psicologia infantil [particcular] R$180,00\
* Psiquiatria adulto [particcular] R$550,00\
* Psiquiatria infantil [particcular] R$450,00\
* Teste Neuro-psicológico [particcular] R$2.000,00\
**Exemplo de Pergunta e Resposta:**\
**Pergunta:** Quais especialidades a Clínica Cuidando de Você oferece para crianças?\
**Resposta:** Oferecemos psicologia infantil e psiquiatria infantil para crianças."""
    instrução_sistema += f"\nUsuário: {pergunta}"
    prompt_completo = instrução_sistema
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt_completo, stream=True)
    resposta_final = ""
    for chunk in response:
        resposta_final += chunk.text
    return resposta_final

# Estados da conversa
AGUARDANDO_NOME, MENU_PRINCIPAL, AGUARDANDO_PERGUNTA = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia uma mensagem de boas-vindas e pede o nome do usuário."""
    saudacoes = [
        "Olá! Me chamo Juh Fortalece ❤️. É um prazer te atender. Como gostaria que eu te chamasse?\n",
        "Oi! Sou a Juh Fortalece❤️ e estou aqui para te ajudar. Como posso te chamar? \n",
        "Olá! Meu nome é Juh Fortalece ❤️. Para facilitar, como você prefere que eu te chame?\n",
        "Boas vindas! 😊 Sou a Juh Fortalece. Qual nome posso usar para me dirigir a você?\n",
        "Olá!❤️ Sou a Juh Fortalece. Para tornar nossa conversa mais pessoal, como posso te chamar?\n",
        "Boas vindas! ✨ Estou aqui para te auxiliar. Para começar, qual é o seu nome?\n",
        "Olá!😊 Sou a Juh Fortalece, e é um prazer te receber. Como prefere que eu te chame?\n",
        "Oi! Sou a Juh Fortalece 😊, e estou feliz em te ajudar. Como posso te chamar durante nossa conversa?\n",
        "Olá!😊 Sou a Juh Fortalece, e estou aqui para tornar sua experiência a melhor possível. Qual nome posso usar para me dirigir a você?\n",
    ]
    await update.message.reply_text(random.choice(saudacoes))
    return AGUARDANDO_NOME

async def receber_nome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Recebe o nome do usuário e apresenta o menu."""
    resposta = update.message.text
    nome_usuario = extrair_nome(resposta)
    context.user_data['nome'] = nome_usuario  # Salva o nome no contexto
    await update.message.reply_text(f"Prazer em te conhecer, {nome_usuario}! 😊 Sou a Juh Fortalece, recepcionista da Clínica Cuidando de Você. Como posso te ajudar?")
    await apresentar_menu(update, context)
    return MENU_PRINCIPAL

async def apresentar_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Apresenta o menu de opções."""
    nome_usuario = context.user_data.get('nome', 'amigo(a)')
    saudacoes = [
        f"\n{nome_usuario}, estou aqui por você, conte comigo!",
        f"\n{nome_usuario}, 😊 estou aqui pra te ajudar.",
        f"\n{nome_usuario}, conte comigo! 🤗 Estou aqui pra tornar sua experiência a melhor!",
        f"\n{nome_usuario}, estou à sua disposição✨",
        f"\n{nome_usuario}, sinta-se à vontade🌻",
        f"\n{nome_usuario}, se precisar de apoio, estou aqui 💙"
    ]
    saudacao = random.choice(saudacoes)
    texto_menu = f"{saudacao}\n\nFique à vontade e digite o número correspondente à sua necessidade:\n\n" \
    "1 - Informações sobre localização e contato;\n\n" \
    "2 - Informações sobre nossas especialidades e serviços;\n\n" \
    "3 - Informações sobre agendamento, remarcação e cancelamento de consultas;\n\n" \
    "4 - Informações sobre cobertura de\n\Planos de Saúde;\n\n" \
    "5 - Informações sobre custo de atendimento;\n\n" \
    "6 - Dúvida muito específica, precisa de\n\uma chamada de voz;\n\n" \
    "7 - Fazer uma pergunta diretamente."
    await update.message.reply_text(texto_menu)
    
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
    nome_usuario = context.user_data.get('nome', 'amigo(a)')
    
    if opcao == '1':
        await informacoes_localizacao(update, context)
        await apresentar_menu(update, context) # Volta para o menu após a ação
    elif opcao == '2':
        await informacoes_especialidades(update, context)
        await apresentar_menu(update, context)
    elif opcao == '3':
        await informacoes_consultas(update, context)
        await apresentar_menu(update, context)
    elif opcao == '4':
        await informacoes_planos_saude(update, context)
        await apresentar_menu(update, context)
    elif opcao == '5':
        await informacoes_custos(update, context)
        await apresentar_menu(update, context)
    elif opcao == '6':
        await transferir_atendente(update, context)
        await apresentar_menu(update, context)
    elif opcao == '7':
        await update.message.reply_text("Digite sua pergunta:")
        return AGUARDANDO_PERGUNTA  # Novo estado para aguardar a pergunta
    else:
        await update.message.reply_text("Opção inválida. Por favor, escolha uma opção válida.")
    return MENU_PRINCIPAL # Permanece no menu principal após as ações 1-6

async def responder_com_gemini(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia a pergunta para o Gemini e retorna a resposta."""
    pergunta = update.message.text
    resposta = obter_resposta_gemini(pergunta)
    await update.message.reply_text(resposta)
    await apresentar_menu(update, context)  # Volta para o menu
    return MENU_PRINCIPAL

async def informacoes_localizacao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Fornece informações sobre a localização e contato da clínica com frases variadas."""
    nome_usuario = context.user_data.get('nome', 'amigo(a)')
    localizacao = [
        f"\n{nome_usuario}, estamos localizados na R. dos Jequitibás - Jabaquara, São Paulo - SP, 04309-011\nQuer saber como chegar? Pode ver direto no seu Google Maps\n📍Como chegar: https://maps.app.goo.gl/maps/zM8K9YKozVjM571z7",
        f"\n{nome_usuario}, nossa clínica fica na R. dos Jequitibás - Jabaquara, São Paulo - SP. O CEP é 04309-011\nQuer saber como chegar? Pode ver direto no seu Google Maps\n📍Como chegar: https://maps.app.goo.gl/maps/zM8K9YKozVjM571z7",
        f"\n{nome_usuario}, estamos na R. dos Jequitibás - Jabaquara, São Paulo - SP, 04309-011\nQuer saber como chegar? Pode ver direto no seu Google Maps\n📍Como chegar: https://maps.app.goo.gl/maps/zM8K9YKozVjM571z7"
    ]
    await update.message.reply_text(random.choice(localizacao))
    
async def informacoes_especialidades(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Informa as especialidades e serviços oferecidos pela clínica com frases variadas."""
    especialidades_texto = [
        "Atendemos:\nPsicologia (adulto e infantil)\nPsiquiatria (adulto e infantil)",
        "Oferecemos atendimento em:\nPsicologia (adulto e infantil)\nPsiquiatria (adulto e infantil)",
        "Nossa clínica conta com especialistas em:\nPsicologia adulto e infantil\nAlém de psiquiatria adulto e infantil",
        "Você pode encontrar:\nPsicólogos/psicólogas e psiquiatras para adultos e crianças em nossa clínica",
        "Temos profissionais nas áreas de psicologia e psiquiatria, atendendo adultos e crianças"
    ]
    await update.message.reply_text(random.choice(especialidades_texto))

async def informacoes_consultas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Fornece informações sobre agendamento, remarcação e cancelamento de consultas."""
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
    planos_texto = [
        "Atendemos:\nparticular, Bradesco Saúde, Omnit e Hapivida.",
        "Aceitamos os seguintes planos de saúde:\nBradesco Saúde,\nOmnit,\nHapivida e particular.",
        "Trabalhamos com:\nBradesco Saúde,\nOmnit,\nHapivida\ne também atendemos particular.",
        "Você pode usar seu plano:\nBradesco Saúde, Omnit ou Hapivida. Também aceitamos particular.",
        "Cobrimos os planos:\nBradesco Saúde,\nOmnit\ne Hapivida,\nalém de consultas particulares."
    ]
    await update.message.reply_text(random.choice(planos_texto))

async def informacoes_custos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Informa os custos dos atendimentos."""
    texto = (
        "* Psicologia adulto [particcular] R$150,00.\n"\
        "* Psicologia infantil [particcular] R$180,00.\n"\
        "* Psiquiatria adulto [particcular] R$550,00.\n"\
        "* Psiquiatria infantil [particcular] R$450,00.\n"\
        "* Teste Neuro-psicológico [particcular] R$2.000,00.\n"\
    )
    await update.message.reply_text(texto)

async def transferir_atendente(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Simula a transferência do usuário para um atendente humano."""
    texto = "Transferindo para um atendente...\nPor favor, aguarde...\n...\n...\n(Som de espera)\n...\n...\nOlá! Em que posso ajudar?"
    await update.message.reply_text(texto)

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            AGUARDANDO_NOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_nome)],
            MENU_PRINCIPAL: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_opcao)],
            AGUARDANDO_PERGUNTA: [MessageHandler(filters.TEXT & ~filters.COMMAND, responder_com_gemini)],
        },
        fallbacks=[],
    )

    application.add_handler(conv_handler)
    application.run_polling()
