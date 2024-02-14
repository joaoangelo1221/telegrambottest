import logging
from telegram import LabeledPrice, ShippingOption, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( 
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
    filters, CallbackQueryHandler
)

# Configurar o logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# Ajustar o nível de log para httpx para evitar logs desnecessários
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Token do provedor de pagamento (Substitua pelo seu token real)
TOKEN_DO_PROVEDOR_DE_PAGAMENTO = "SEU_TOKEN_AQUI"

async def boas_vindas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mensagem de boas-vindas com comandos disponíveis."""
    mensagem = (
        "Bem-vindo(a) ao Botinho!\n"
        "Aqui estão alguns comandos que você pode usar:\n"
        "/servicos - Aqui você conhecerá os serviços prestados pela JoTech.\n"
        "/ajuda - Aqui será sanadas suas dúvidas.\n"
        "/contatos - Aqui você encontra informações para o contato direto com o pessoal da JoTech."
    )

    await update.message.reply_text(mensagem)

async def servicos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Escolha de serviços com opções de pagamento."""
    mensagem = (
        "Escolha um serviço:"
    )

    teclado = [
        [
            InlineKeyboardButton("Bot", callback_data='bot'),
            InlineKeyboardButton("Programa", callback_data='programa')
        ],
        [
            InlineKeyboardButton("Cybersecurity", callback_data='cybersecurity'),
            InlineKeyboardButton("Design", callback_data='design')
        ]
    ]
    resposta_markup = InlineKeyboardMarkup(teclado)

    # Envia a mensagem com os botões
    await update.message.reply_text(mensagem, reply_markup=resposta_markup)


# Adicione essa função para processar os cliques nos botões
async def processar_botao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    botao_clicado = query.data

    # Adicione lógica adicional conforme necessário para cada botão
    if botao_clicado == 'bot':
        await bot(update, context)
    elif botao_clicado == 'programa':
        await programa(update, context)
    elif botao_clicado == 'cybersecurity':
        await cybersecurity(update, context)
    elif botao_clicado == 'design':
        await design(update, context)


async def bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Bot comercial/outros."""
    mensagem = (
        "A JoTech presta-se à criação de bots diversos no Telegram, uma plataforma segura e confiável.\n"
        "Ao escolher o serviço de bots de nossa marca para o seu negócio, ouvimos suas necessidades e a implementamos conforme o seu pedido.\n"
        "Para antendermos você, cliente, mostramos exemplos de bots comerciais os quais você os observará, e terá um noção da efeciência deste recurso."
        "Para consultar nossas amostras, entre com o comando /AmostraBot\n"

    )

    if update.message:
        await update.message.reply_text(mensagem)
    else:
        await context.bot.send_message(update.effective_user.id, mensagem)

async def programa(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Programa logístico/outros\n"""
    mensagem = (
        "A JoTech tem como escopo no âmbito da programação o sistema escritorial e logístico, para os quais usa em sua lógica a dinamização e a praticidade no seu propósito.\n"
        "Pontualmente, atendemos o cliente e entregamos o produto atendendo suas necessidades.\n"
        "Para consultar nossas amostras, entre com o comando XXX\n"

    )

    if update.message:
        await update.message.reply_text(mensagem)
    else:
        await context.bot.send_message(update.effective_user.id, mensagem)

async def cybersecurity(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """3. Serviço de segurança cibernética\n"""
    mensagem = (
        "Na área da segurança cibernética, a JoTech atua em XXX.\n"
        "Para consultar nossas amostras, entre com o comando XXX\n"

    )

    if update.message:
        await update.message.reply_text(mensagem)
    else:
        await context.bot.send_message(update.effective_user.id, mensagem)

async def design(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """4. Arte/Vídeo comercial/outros\n"""
    mensagem = (
        "a JoTech atua também com a criação de artes digitais, e até impressões para sua marca/empreendimentos, como também vídeos dinâmicos para comerciais e propagandas.\n"
        "Para consultar nossas amostras, entre com o comando XXX\n"

    )

    if update.message:
        await update.message.reply_text(mensagem)
    else:
        await context.bot.send_message(update.effective_user.id, mensagem)

async def inicio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Retorna ao início da conversa."""
    mensagem = (
        "Você retornou ao início.\n"
        "Aqui estão alguns comandos que você pode usar:\n"
        "/servicos - Deixe os serviços a serem preenchidos.\n"
        "/ajuda - Deixe a ajuda a ser preenchida.\n"
        "/contatos - Deixe os contatos a serem preenchidos."
    )
    await update.message.reply_text(mensagem)

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Central de ajuda."""
    mensagem = (
       "A JoTech, como prestadora de serviços, tem como canal inicial este assistente virtual/bot para os clientes interessados em adquirir nossos serviços.\n"
       "Por este canal de comunicação, não será cobrado nada, servindo unicamente para a exposição e ponte de aquisição dos produtos\n"
       "Caso queira falar diretamente com um responsável, entrar em /contatos para mais informações\n"
       "Para voltar ao início, clique em /inicio"
    )

    await update.message.reply_text(mensagem)

async def contatos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Contatos para a comunicação direta."""
    mensagem = (
        "João Angelo\n"
        "Celular para contato: (69) 98119-2025\n"
        "Ou se preferir, link para o Whatsapp: https://w.app/TvQC0c\n"
        "Para voltar ao início, clique em /inicio"

    )

    await update.message.reply_text(mensagem)


def main() -> None:
    """Executa o bot."""
    # Cria a aplicação e passa o token do seu bot
    aplicacao = Application.builder().token("6759114349:AAF4oP5xjCM5C0ZVJsQczsxJ5x4n8snZFgg").build()

    # Função de boas-vindas
    aplicacao.add_handler(CommandHandler("start", boas_vindas))

    # Comandos para preenchimento
    aplicacao.add_handler(CommandHandler("servicos", servicos))
    aplicacao.add_handler(CommandHandler("ajuda", ajuda))
    aplicacao.add_handler(CommandHandler("contatos", contatos))
    # Comandos dos serviços
    aplicacao.add_handler(CommandHandler("bot", bot))
    aplicacao.add_handler(CommandHandler("programa", programa))
    aplicacao.add_handler(CommandHandler("cybersecurity", cybersecurity))
    aplicacao.add_handler(CommandHandler("design", design))

    # Retornar ao início
    aplicacao.add_handler(CommandHandler("inicio", boas_vindas))



    aplicacao.add_handler(CallbackQueryHandler(processar_botao))


    # Executa o bot até que o usuário pressione Ctrl-C
    aplicacao.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
