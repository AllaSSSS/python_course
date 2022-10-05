from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def log(update: Update):
    with open ('bot.log', 'a') as file:
        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update)
    msg = update.message.text
    print(msg)
    cmd, item1, item2 = tuple(msg.split(' '))
    await update.message.reply_text(f'{item1} + {item2} = {int(item1) + int(item2)}')

async def sub(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update)
    msg = update.message.text
    print(msg)
    cmd, item1, item2 = tuple(msg.split(' '))
    await update.message.reply_text(f'{item1} - {item2} = {int(item1) - int(item2)}')

async def mul(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update)
    msg = update.message.text
    print(msg)
    cmd, item1, item2 = tuple(msg.split(' '))
    await update.message.reply_text(f'{item1} * {item2} = {int(item1) * int(item2)}')

async def div(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update)
    msg = update.message.text
    print(msg)
    cmd, item1, item2 = tuple(msg.split(' '))
    await update.message.reply_text(f'{item1} / {item2} = {int(item1) // int(item2)}')

app = ApplicationBuilder().token("5321360449:AAEr-pJC28jn8Bev4gTI6CizuJO0dl3zYBE").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum))
app.add_handler(CommandHandler("sub", sub))
app.add_handler(CommandHandler("mul", mul))
app.add_handler(CommandHandler("div", div))

app.run_polling()
