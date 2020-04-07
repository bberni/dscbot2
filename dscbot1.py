import discord  
import asyncio  
from discord.ext import commands 

client =  commands.Bot(command_prefix = '.')

@client.event 
async def on_ready(): 
      print('ready')  

@client.event 
async def on_message(message):  
     print('1') 
     print(message.author.id)
     if message.author.id ==459253782627221506:  
         print('1') 
         channel = message.channel
         await channel.send('')

@client.command() 
async def purge(ctx, amount = 2):
    await ctx.channel.purge(limit = amount +1)




 

client.run('Njk2NjQxNTk3NTcxNTk2Mjk5.XoxHLw.M8jOdqfBPzFqdpRP4lmk3vLUamI')
