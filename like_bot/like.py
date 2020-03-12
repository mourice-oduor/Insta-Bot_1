from instabot import Bot

bot = Bot()

bot.login(username="IG_Uname",password="PASS_HERE")

tags = ['javascript','python','programming']
for i in tags:
    bot.like_hashtag(i,amount=20)
