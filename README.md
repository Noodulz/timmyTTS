# TimmyTTS
![toad](toad.png)
TimmyTTS is a text-to-speech bot that can generate and send audio files of speech synthesis in multiple languages. In addition, TimmyTTS can also translate text, and identify the language of a piece of text. 

## Supported Languages
Languages supported include Arabic, Chinese, Cantonese, Traditional Chinese, English, French, German, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Malay, Portuguese, Russian, Spanish, Swedish, Tagalog, Tamil, Thai and Vietnamese.

## How to use
The available commands are `t/speak`, `t/translate`, `t/identify`, and `t/help`. 

To request a TTS message, use `t/speak`, specify your target language, and then your text.
```
t/speak french oui oui baguette
```

To translate text, use `t/translate`, enter your text, and then specify the target language at the end.
```
t/translate hola japanese
```

To identify the language of a text, use `t/identify` and then the text you want to identify.
```
t/identify ハイププ
```

For more help, trigger `t/help`

## Requirements
This bot was specifically developed using Python 3.6, as there are difficult constraints with integrating the Discord API with the latest Python 3.x, so it will only work under 3.6 if intending to host. The modules used were discord.py, urllib, asyncio, wget, os, requests, and googletrans. 

```
python3.6 -m pip install -r requirements.txt
```

This bot uses the Google Translate API and the VoiceRSS API for TTS messages. 

## Demo
TBA

## Invite Link
https://shorturl.at/rSTZ2
