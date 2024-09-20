from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Replace these with your contact details and bot information
ABOUT_TEXT = "This is a bot that helps you manage and explore various commands. You can edit existing bots or create new ones."
PORTFOLIO_TEXT = """
Here are some of the bots and Fiverr gigs we've worked on:
1. [AvaTrades](https://t.me/aavtradebot)
2. [Bot 2](http://example.com/bot2)
3. [Fiverr Gig 1](http://example.com/fiverrgig1)
4. [Fiverr Gig 2](http://example.com/fiverrgig2)
"""

EDIT_BOT_CONTACT = "You can contact me to edit existing bots [here](http://example.com/contact)."
CREATE_BOT_CONTACT = "You can contact me to create a new bot [here](http://example.com/contact)."

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("About", callback_data='about')],
        [InlineKeyboardButton("Portfolio", callback_data='portfolio')],
        [InlineKeyboardButton("What Do You Want", callback_data='what_do_you_want')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Please choose an option:', reply_markup=reply_markup)

async def button(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'about':
        await query.edit_message_text(text=ABOUT_TEXT)
    elif query.data == 'portfolio':
        await query.edit_message_text(text=PORTFOLIO_TEXT, parse_mode='Markdown')
    elif query.data == 'what_do_you_want':
        keyboard = [
            [InlineKeyboardButton("Edit Existing Bot", url='http://example.com/contact')],
            [InlineKeyboardButton("Create a New Bot", url='http://example.com/contact')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="What do you want to do?", reply_markup=reply_markup)

def main():
    # Replace 'YOUR_API_TOKEN' with the token provided by BotFather
    app = ApplicationBuilder().token('7390391307:AAH04U3GHdvnusyTQmQ0HwGJw2Vn7bnjuFY').build()

    # Add command and callback query handlers
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button))

    # Run the bot
    app.run_polling()

if __name__ == '__main__':
    main()
