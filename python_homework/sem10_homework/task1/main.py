import telebot
import cmath

apiToken = ''
with open('api-token.txt', 'r') as file:
    apiToken = file.read()

bot = telebot.TeleBot(apiToken)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
This is my stack-based calculator. Supports real and complex numbers.

/start - show the menu
/sum - sum last two numbers
/sub - subtract the last number from the previous one
/mul - multiply last two numbers
/div - divide the previous number by the last one

Just send a number to add it to the stack.
""")

def format_num(num):
    if num.imag == 0:
        return str(num.real)
    if num.imag > 0:
        return f'{num.real} + {num.imag}j'
    else:
        return f'{num.real} - {-num.imag}j'



stack = []

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    msg = message.text
    if msg.startswith('/'):
        # parse a command
        if len(stack) < 2:
            bot.reply_to(message, 'Unavailable operation')
            return
        match msg:
            case '/sum': 
                stack.append(+stack.pop() + stack.pop())
            case '/sub':
                stack.append(-stack.pop() + stack.pop())
            case '/mul':
                stack.append(stack.pop() * stack.pop())
            case '/div':
                numerator = stack.pop()
                nominator = stack.pop()
                stack.append(nominator / numerator)
    else:
        num = 0
        try:
            num = complex(msg)
        except:
            bot.reply_to(message, 'Invalid number')
            return    

        stack.append(num)

    bot.reply_to(message, ", ".join(map(lambda n: format_num(n), stack)))


bot.infinity_polling()