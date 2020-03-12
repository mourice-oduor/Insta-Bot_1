from instabot import Bot

bot = Bot()
bot.login(username="IG_Uname",password="PASSWORD_HERE")
bot.upload_photo(photo="moryso.jpg", caption="Hello this is #bot_testing")
#locate the api package directory
user_id=fields.One2many("/home/net/.local/lib/python3.7/site-packages/instabot/api/api.py")
