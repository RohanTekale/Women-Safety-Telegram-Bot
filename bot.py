# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters
# from telegram.ext import CallbackContext
# from geopy.geocoders import Nominatim
# from twilio.rest import Client
# import asyncio

# # Bot Token
# TOKEN = '7301100617:AAEHhxXDe56UuD3kZYer8DxT6t1uLdS5anM'  # Replace with your actual bot token

# # Twilio credentials
# TWILIO_ACCOUNT_SID = 'AC75b9b3136f9bfe8465c667ddcdd6d779'  # Replace with your Twilio Account SID
# TWILIO_AUTH_TOKEN = 'c5ff0f2be1d2a1511ccbd234a28c110e'  # Replace with your Twilio Auth Token
# TWILIO_PHONE_NUMBER = '+14806464571'  # Replace with your Twilio phone number

# # Logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# def get_location(address):
#     geolocator = Nominatim(user_agent="safety_bot")
#     try:
#         location = geolocator.geocode(address)
#         if location:
#             return location.latitude, location.longitude
#         else:
#             return None, None
#     except Exception as e:
#         logger.error(f"Error in geocoding address '{address}': {e}")
#         return None, None

# def reverse_geocode(lat, lon):
#     geolocator = Nominatim(user_agent="safety_bot")
#     try:
#         location = geolocator.reverse((lat, lon))
#         return location.address if location else None
#     except Exception as e:
#         logger.error(f"Error in reverse geocoding coordinates ({lat}, {lon}): {e}")
#         return None

# def send_sms(to, message):
#     client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#     try:
#         message = client.messages.create(
#             body=message,
#             from_=TWILIO_PHONE_NUMBER,
#             to=to
#         )
#         return message.sid
#     except Exception as e:
#         logger.error(f"Error sending SMS: {e}")
#         return None

# async def send_alert(update: Update, context: CallbackContext, lat, lon):
#     phone_number = "+919307802374"  # Replace with your phone number
#     message = f"Emergency! Check location: {reverse_geocode(lat, lon)}"
#     sms_sid = send_sms(phone_number, message)
#     if sms_sid:
#         await update.message.reply_text(f"Alert sent to {phone_number}: {message}")
#     else:
#         await update.message.reply_text("Failed to send alert.")

# async def handle_message(update: Update, context: CallbackContext):
#     text = update.message.text.lower()
#     if text == "help me":
#         lat, lon = get_location("Address")  # Replace with actual method to get user location
#         if lat and lon:
#             await send_alert(update, context, lat, lon)
#         else:
#             await update.message.reply_text("Could not determine your location.")
#     else:
#         await update.message.reply_text("Command not recognized. Please send 'help me' for assistance.")

# async def start(update: Update, context: CallbackContext):
#     await update.message.reply_text('Welcome to the Women Safety Bot!')

# def main():
#     try:
#         application = Application.builder().token(TOKEN).build()
#         application.add_handler(CommandHandler("start", start))
#         application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

#         # Start the bot
#         application.run_polling()
#     except Exception as e:
#         logger.error(f"Error in bot initialization: {e}")

# if __name__ == '__main__':
#     main()


# import logging
# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
# from telegram.ext import Application, CommandHandler, MessageHandler, filters
# from telegram.ext import CallbackContext
# from geopy.geocoders import Nominatim
# from twilio.rest import Client
# import asyncio

# # Bot Token
# TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Replace with your actual bot token

# # Twilio credentials
# TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'  # Replace with your Twilio Account SID
# TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'  # Replace with your Twilio Auth Token
# TWILIO_PHONE_NUMBER = 'YOUR_TWILIO_PHONE_NUMBER'  # Replace with your Twilio phone number

# # Logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# def get_location(address):
#     geolocator = Nominatim(user_agent="safety_bot")
#     try:
#         location = geolocator.geocode(address)
#         if location:
#             return location.latitude, location.longitude
#         else:
#             return None, None
#     except Exception as e:
#         logger.error(f"Error in geocoding address '{address}': {e}")
#         return None, None

# def reverse_geocode(lat, lon):
#     geolocator = Nominatim(user_agent="safety_bot")
#     try:
#         location = geolocator.reverse((lat, lon))
#         return location.address if location else None
#     except Exception as e:
#         logger.error(f"Error in reverse geocoding coordinates ({lat}, {lon}): {e}")
#         return None

# def send_sms(to, message):
#     client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#     try:
#         message = client.messages.create(
#             body=message,
#             from_=TWILIO_PHONE_NUMBER,
#             to=to
#         )
#         return message.sid
#     except Exception as e:
#         logger.error(f"Error sending SMS: {e}")
#         return None

# async def send_alert(update: Update, context: CallbackContext, lat, lon):
#     phone_number = "+919307802374"  # Replace with your phone number
#     address = reverse_geocode(lat, lon)
#     if address:
#         message = f"Emergency! Check location: {address}"
#         sms_sid = send_sms(phone_number, message)
#         if sms_sid:
#             await update.message.reply_text(f"Alert sent to {phone_number}: {message}")
#         else:
#             await update.message.reply_text("Failed to send alert.")
#     else:
#         await update.message.reply_text("Could not determine the location.")

# async def handle_message(update: Update, context: CallbackContext):
#     text = update.message.text.lower()
#     if text == "help me":
#         # Send a request for location sharing
#         keyboard = [[KeyboardButton("Share my location", request_location=True)]]
#         reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
#         await update.message.reply_text("Please share your location by pressing the button below.", reply_markup=reply_markup)
#     else:
#         await update.message.reply_text("Command not recognized. Please send 'help me' for assistance.")

# async def handle_location(update: Update, context: CallbackContext):
#     user_location = update.message.location
#     if user_location:
#         lat, lon = user_location.latitude, user_location.longitude
#         await send_alert(update, context, lat, lon)
#     else:
#         await update.message.reply_text("Failed to get location.")

# async def start(update: Update, context: CallbackContext):
#     await update.message.reply_text('Welcome to the Women Safety Bot!')

# def main():
#     try:
#         application = Application.builder().token(TOKEN).build()
#         application.add_handler(CommandHandler("start", start))
#         application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
#         application.add_handler(MessageHandler(filters.LOCATION, handle_location))

#         # Start the bot
#         application.run_polling()
#     except Exception as e:
#         logger.error(f"Error in bot initialization: {e}")

# if __name__ == '__main__':
#     main()
import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.ext import CallbackContext
from geopy.geocoders import Nominatim
from twilio.rest import Client
import asyncio

# Bot Token
TOKEN = ''  # Replace with your actual bot token

# Twilio credentials
TWILIO_ACCOUNT_SID = ''  # Replace with your Twilio Account SID
TWILIO_AUTH_TOKEN = ''  # Replace with your Twilio Auth Token
TWILIO_PHONE_NUMBER = ''  # Replace with your Twilio phone number

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def get_location(address):
    geolocator = Nominatim(user_agent="safety_bot")
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except Exception as e:
        logger.error(f"Error in geocoding address '{address}': {e}")
        return None, None

def reverse_geocode(lat, lon):
    geolocator = Nominatim(user_agent="safety_bot")
    try:
        location = geolocator.reverse((lat, lon))
        return location.address if location else None
    except Exception as e:
        logger.error(f"Error in reverse geocoding coordinates ({lat}, {lon}): {e}")
        return None

def send_sms(to, message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to
        )
        return message.sid
    except Exception as e:
        logger.error(f"Error sending SMS: {e}")
        return None

async def send_alert(update: Update, context: CallbackContext, lat, lon):
    phone_number = "+919307802374"  # Replace with your phone number
    address = reverse_geocode(lat, lon)
    if address:
        logger.info(f"Sending alert to {phone_number} with location: {address}")
        message = f"Emergency! Check location: {address}"
        sms_sid = send_sms(phone_number, message)
        if sms_sid:
            await update.message.reply_text(f"Alert sent to {phone_number}: {message}")
        else:
            await update.message.reply_text("Failed to send alert. Please check Twilio settings.")
    else:
        await update.message.reply_text("Could not determine the location.")

async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if text == "help me":
        # Send a request for location sharing
        keyboard = [[KeyboardButton("Share my location", request_location=True)]]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        await update.message.reply_text("Please share your location by pressing the button below.", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Command not recognized. Please send 'help me' for assistance.")

async def handle_location(update: Update, context: CallbackContext):
    user_location = update.message.location
    if user_location:
        lat, lon = user_location.latitude, user_location.longitude
        logger.info(f"Received location: Latitude={lat}, Longitude={lon}")
        await send_alert(update, context, lat, lon)
    else:
        await update.message.reply_text("Failed to get location.")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Welcome to the Women Safety Bot!')

def main():
    try:
        application = Application.builder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        application.add_handler(MessageHandler(filters.LOCATION, handle_location))

        # Start the bot
        application.run_polling()
    except Exception as e:
        logger.error(f"Error in bot initialization: {e}")

if __name__ == '__main__':
    main()

