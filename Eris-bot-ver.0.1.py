import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time


    
BotToken = 'NDYyMTg1NzA5MzM2NTI2ODU4.Dh802Q.6gUekSvudxHEJQrbvCS_tJhngEk'
BotUUID = "<@462185709336526858>"
Client = discord.Client()
BotCall = commands.Bot(command_prefix = "!")
EnglishBadWords = "GOD, FUCK, SUCK, ASS, BUTT, DUMB, IDIOT, WHORE, BITCH, ASSHOLE, RETARD, OMG, DAMN"

#IS ONLINE EVENT
@BotCall.event
async def on_ready():
    print("It is alive! \n\n\n")
    
#MESSAGE TRIGGER EVENT
@BotCall.event
async def on_message(AnyonePost):
    AuthorUUID = AnyonePost.author.id



#Command Name: MENTIONED
#Command Description: Eris hearts when mentioned
#Command Format(not case sensitive): @BotTag
    if AnyonePost.content.upper() == BotUUID:
        AuthorUUID = AnyonePost.author.id
        await BotCall.send_message(AnyonePost.channel, "<@%s> :purple_heart:"%(AuthorUUID))



#Command Name: MENTIONED WITH QUESTION
#Command: Eris says string when mentioned with a question mark.
#Command Format(not case sensitive): @BotTag [ANYTHING] [?]
    if BotUUID in AnyonePost.content.upper() and "?" in AnyonePost.content.upper():
        await BotCall.send_message(AnyonePost.channel, "<@%s> That is a mystery for us both."%(AuthorUUID))



#Command Name: MENTIONED WITH EXCLAMATION
#Command Description: Eris says string when mentioned with an exclamation mark.
#Command Format(not case sensitive): @BotTag [ANYTHING] [!]
    if BotUUID in AnyonePost.content.upper() and "!" in AnyonePost.content.upper():
        await BotCall.send_message(AnyonePost.channel, "<@%s> What if I say, no\?"%(AuthorUUID))



#Command Name: SAY
#Command Description: Tell Eris to say something, or call a command by itself. (DANGEROUS)
#Command Format(not case sensitive): @BotTag .SAY
    if AnyonePost.content.upper().startswith(BotUUID + ' .SAY'):
        args = AnyonePost.content.split(" ")
    #This will tell the bot to join and then send all strings after 3rd string in the array or array[2]
        await BotCall.send_message(AnyonePost.channel, "%s" % (" ".join(args[2:])))



#Command Name: UUID
#Command Description: Eris tells your .UUID
    if AnyonePost.content.upper().startswith(BotUUID + ' .UUID'):
        await BotCall.send_message(AnyonePost.channel, "<@%s>'s Discord UUID is: \<\@%s\>" % (AuthorUUID,AuthorUUID))



#Command Name: DELETE
#Command Description: Eris deletes your post(s) among the last messages it encounters.
#Command Format(not case sensitive): @BotTag .DELETE [LIMITER] [TARGET]
#[LIMITER] = Integer Number. Limit the messages number checked by the program from the latest messages.
#[TARGET] = - ALL to delete all message(s) in limiter range
#           - UUID or User (e.g <@12345677889> or @UserTag)for specific message(s) authored bt the AuthorID.
#           - None to delete messages by the command caller.
#This will check if the command is mentioned, and to make the command, not case sensitive.
    if AnyonePost.content.upper().startswith(BotUUID + ' .DELETE') :
    #This will tell the bot to split the strings into an array with " " as separator.
        args = AnyonePost.content.upper().split(" ")
        argsLength = len(args)
    #This adds a timer, made from the time "time" library. requires:
    #import time
    #at the beginning
        now = time.localtime()
    #"now" will have an array, if we run printed(now) it will look like:
    #time.struct_time(tm_year=2018, tm_mon=7, tm_mday=7, tm_hour=18, tm_min=46, tm_sec=16, tm_wday=5, tm_yday=188, tm_isdst=0)
    #and if we run print(now[5]) it will look like:
    #16
    #This will string-format-time for easier read.
        nowTimeFormat = time.strftime("%Y/%m/%d, %H:%M:%S", now)
        print(nowTimeFormat)
    #Get Command length in array, and command evoker.
        print("DELETE command evoked by <@%s>!" % (AuthorUUID))
        print("The command is %s word(s) long." % (argsLength))

    #This checks limiter from the command call. It checks the 3rd input, or array[2]
    #Also checks the value. If the limiter number <= 1 Botcall.logs_from() function will fail, so it needs bigger number, minimum 2.
        if argsLength >= 3: #if command line is less than or equal to 3 components do...
            if args[2] != 0: #if the 3rd component is not none
                Limiter = int(args[2])
            if Limiter < 1 or Limiter == None:
                Limiter = 2
            else:    
                Limiter = Limiter + 1
        else:
            print("Error: Unable to find limiter in the command.")

    #This will give permission to delete all or specific messages under authorID. It checks the 4th input, or array[3]
        if len(args) >= 4:
            if str(args[3]) == "ALL":
                DeleteAll = 1
                print("Deleting All Permitted!")
        else:
            DeleteAll = 0

    #Get the initial sum of the to be deleted messages
        LimiterInit = Limiter
        
    #This will assume no message has been deleted yet...   
        AuthorDeletedSum = 0   
        AnyDeletedSum = 0

    #checking the messages...
        async for log in BotCall.logs_from(AnyonePost.channel, limit = Limiter):
        #If deleteAll is 0, only the post belongs to the author, will be deleted.
            if DeleteAll == 0:
                print("Searching from the latest %s post(s) for post(s) made by <@%s>..." % (Limiter, AuthorUUID))
            else:
                print("Deleting all post from the latest %s post(s)..." % (Limiter))
            if log.author == AnyonePost.author:
                await BotCall.delete_message(log)
                AuthorDeletedSum = AuthorDeletedSum + 1
                AnyDeletedSum = AnyDeletedSum + 1
            #Counting down the range...
                Limiter = Limiter - 1
                
        #If DeleteAll is 1 and the encountered post doesn't belong to the author, it will be deleted...
            elif log.author != AnyonePost.author and DeleteAll == 1:
                await BotCall.delete_message(log)
                AnyDeletedSum = AnyDeletedSum + 1
            #Counting down the range...
                Limiter = Limiter - 1
                
        #FINAL. When the count is down to zero...
            if Limiter == 0:
                if DeleteAll == 0:
                    print("DONE IS DONE! Among the latest %s post(s), %s post(s) from <@%s> deleted." % (LimiterInit, AnyDeletedSum, AuthorUUID))
                if DeleteAll == 1:
                    print("DONE IS DONE! All from the latest %s post(s) deleted." % (LimiterInit))
                    print("Among the total %s, %s post(s) from <@%s> deleted.\n\n\n" % (AnyDeletedSum, AuthorDeletedSum, AuthorUUID))


#RUN BOT WITH TOKEN - Should always be in the end of the events program.
BotCall.run(BotToken)
