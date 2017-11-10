import json
import os

from aiotg import Bot

bot = Bot(api_token=os.environ["API_TOKEN"])

@bot.command(r'/start')
async def start(chat, match):

    markup = {
            'type': 'InlineKeyboardMarkup',
            'inline_keyboard': [
                [{'type': 'InlineKeyboardButton',
                  'text': 'Button A',
                  'callback_data': 'buttonclick-A'},
                 {'type': 'InlineKeyboardButton',
                  'text': 'Button B',
                  'callback_data': 'buttonclick-B'}],
                [{'type': 'InlineKeyboardButton',
                  'text': 'Nohandle Button',
                  'callback_data': 'no_callback_data'}],
                ]
            }

    await chat.send_text('Hello', reply_markup=json.dumps(markup))


@bot.default
async def unhandled_callbacks(chat, cq):
    await chat.send_text('Unhandled callback fired')


@bot.callback(r"buttonclick-(\w+)")
async def handled_callbacks(chat, cq, match):
    await chat.send_text('You clicked {}'.format(match.group(1)))


bot.run(debug=True)