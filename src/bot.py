import discord
import urllib
import asyncio
import wget
import os
import requests
import googletrans
from googletrans import Translator
from lang import *
from urllib import parse
from discord.ext.commands import Bot
from discord.ext import commands 

# Bot token
TOKEN = 'token-here' 
# Every command starts with t/ 
BOT_PREFIX = 't/'
bot = Bot(command_prefix=BOT_PREFIX)
translator = Translator()

#Initialize speak command 
@bot.command(name='speak',
                pass_context=True)
async def speak(context, *args):
    # Converts specified language to language code for VoiceRSS
    lang = voiceRSS_lang(context.args[1])
    # Default error message
    if (lang == "not found"):
        await context.send("There may have been an error or your language isn't included! :(")
    else:
        # Grabs everything after the language argument starting at index 2
        src = '{}'.format(' '.join(context.args[2:]))
        # Generates the parameters to append to the url used to send a wget request
        params = parse.urlencode({'hl': lang, 'src': src})
        url = "http://api.voicerss.org/?key=e2c99f5f32a44c988ef3784609ea9325&c=MP3&f=48khz_16bit_stereo&" + params
        tts = wget.download(url)
        # Downloads and sends mp3 file, then deletes the file afterwards to clear up space
        with open('download.wget', 'rb') as mp3:
            await context.send(file=discord.File(mp3, 'result.mp3'))
        os.remove("download.wget")

# Initialize translate command
@bot.command(name='translate',
                pass_context=True)
async def translate(context, *args):
    # Gets target language at last argument 
    lang = google_lang(context.args[len(args)])
    # Default error message
    if(lang == "not found"):
        await context.send("There may have been an error or your language isn't included! :(")
    else:
        # Parse text from arguments and translate to specified language
        translated = translator.translate('{}'.format(' '.join(context.args[1:len(args)])), dest=lang)
        result = translated.text
        # If pronunciation is in English, so as to not reiterate twice
        if(translated.dest == "en"):
            await context.send(result)
        else:
            await context.send(result + "\n" + translated.pronunciation)

# Initalize identify command
@bot.command(name='identify',
             pass_context=True)
async def identify(context, *args):
    text = translator.translate('{}'.format(' '.join(context.args[1:])))
    language = id(text.src)
    await context.send("This language is " + language.capitalize() + "!")
    
# Initialize help command
bot.remove_command('help')
@bot.command(name='help',
             pass_context=True)
async def help(context):
    # Opens help file and reads from input
    with open("help.txt", 'r') as h:
        await context.send(h.read())
        # Closes right after
    h.close()
bot.run(TOKEN)
