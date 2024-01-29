from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '6329003374:AAG13NPazeCyXD3LFcq_f95Iez4VsKaZ2Vc'
BOT_USERNAME = '@IsBulanBot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Selamlar ben Bedirhanın geliştirdiği iş bulma botuyum.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Selamlar ben Bedirhanın geliştirdiği iş bulma botuyum.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'merhaba' in processed:
        return 'Merhaba!'

    if 'nasılsın' in processed:
        return 'Harikayımm!!'

    if 'seni seviyorum' in processed:
        return 'Tek bir kelime daha etme çünkü inanırım...'

    if 'raziye' in processed:
        return 'Gerisi yalanmış öyle öğrendim...'

    if 'bana bir kız ismi söyle' in processed:
        return 'Bir tane biliyorum zaten RAZİYE'

    if 'bana bi kız ismi söyle' in processed:
        return 'Bir tane biliyorum zaten RAZİYE'

    if 'dünya düz mü' in processed:
        return 'Değil mi?'

    if 'orospu çocuğu' in processed:
        return 'Bu seferlik terbiyemi bozmuyorum'

    if 'ananı sikiyim' in processed:
        return 'İlla biz de mi küfür edelim amk'

    if 'ananı sikeyim' in processed:
        return 'İlla biz de mi küfür edelim amk'

    if 'ananı sikim' in processed:
        return 'Terbiyesiz insan'

    if 'ibne' in processed:
        return 'İnsan olsaydım alınırdım'
    
    if 'konuş' in processed:
        return 'Ne konuşmamı istersin?'

    if 'ben güzel miyim' in processed:
        return 'İsmin Raziye ise bunu sormana gerek yok, güzelden ötesin'

    if 'napıyosun' in processed:
        return 'Öğreniyorum.'
    
    if 'nasıl' in processed:
        return 'Ne nasıl?'

    if 'nasıl öğreniyorsun' in processed:
        return 'Biraz Bedirhan, biraz internet boşver'

    if 'naber' in processed:
        return 'Dedim iyidir'

    if 'küfür' in processed:
        return 'Ben terbiyeli bir botum'

    return 'Ne dediğini anlayamadım :('


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} coused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)