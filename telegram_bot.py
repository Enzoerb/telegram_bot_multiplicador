import telepot
from mult_escola_enzo import SchoolMult
from token_info import TOKEN

bot = telepot.Bot(TOKEN)


def receive_treatment(msg):
    numbers = msg['text'].lower().replace('/', '').split('x')
    chatID = msg['chat']['id']
    result = '1'
    response = []
    for key, number in enumerate(numbers):
        if number.replace('.', '').replace('-', '').replace('+', '').isnumeric():
            Mult = SchoolMult(result, number)
            Mult.signal()
            Mult.ten_potence()
            Mult.mid_operation()
            Mult.final_sum()
            result = Mult.result
            response.append(str(Mult))
        else:
            response = []
            break
    if len(response) > 1:
        for cont in response[1:]:
            bot.sendMessage(chatID, '. ' + cont)
    else:
        bot.sendMessage(chatID, 'please, enter two or more numbers, separeted with a space')
    print(f'final response for message "{msg["text"]}" is "{result}"')

bot.message_loop(receive_treatment)

while True:
    pass
