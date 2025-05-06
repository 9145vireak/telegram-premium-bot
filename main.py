# main.py
from aiogram import Bot, Dispatcher, types, executor
from config import BOT_TOKEN, ADMIN_ID

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('សួស្តី! ចុច "បង់ប្រាក់" ដើម្បី មើលរឿងពេញ.')

@dp.message_handler(lambda msg: msg.text.lower() in ["បង់ប្រាក់", "pay"])
async def send_qr_code(message: types.Message):
    with open("qr_code.png", "rb") as qr:
        await bot.send_photo(chat_id=message.chat.id, photo=qr, caption="សូមបង់ប្រាក់ $0.01 តាម QR Code ខាងលើ។")

@dp.message_handler(content_types=['photo'])
async def handle_slip(message: types.Message):
    await bot.forward_message(chat_id=ADMIN_ID, from_chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_message(ADMIN_ID, f"សូមបញ្ជាក់ slip ពី @{message.from_user.username}")
    await message.reply("សូមរង់ចាំ Admin បញ្ជាក់ slip របស់អ្នក។")

@dp.message_handler(lambda msg: msg.reply_to_message and msg.from_user.id == ADMIN_ID and '✅' in msg.text)
async def confirm_payment(message: types.Message):
    user_id = message.reply_to_message.forward_from.id
    await bot.send_message(user_id, "✅ ការទូទាត់របស់អ្នកត្រូវបានបញ្ជាក់! ចូល VIP Channel៖ https://t.me/+YourPrivateInvite")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
