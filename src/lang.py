# Available languages to translate for Google Translate API
def google_lang(language):
    lang = {
        "english": "en",
        "spanish": "es",
        "korean": "ko",
        "chinese": "zh-cn",
        "chineseSP": "zh-cn",
        "chineseTR": "zh-tw",
        "russian": "ru",
        "japanese": "ja",
        "french": "fr",
        "vietnamese": "vi",
        "hindi": "hi",
        "hmong": "hmn",
        "mongolian": "mn",
        "italian": "it",
        "thai": "th",
        "tagalog": "tl",
        "hawaiian": "haw",
        "malay": "ms",
        "german": "de",
        "indonesian": "id",
        "portuguese": "pt",
        "arabic": "ar",
        "hebrew": "iw",
        "tamil": "ta",
        "not found": "not found"
    }

    return lang.get(language, "not found")

# Available languages for VoiceRSS API
def voiceRSS_lang(language):
    lang = {
        "arabic": "ar-sa",
        "chinese": "zh-cn",
        "chineseSP": "zh-cn",
        "chineseHK": "zh-hk",
        "chineseTR": "zh-tw",
        "english": "en-us",
        "englishBR": "en-gb",
        "englishAU": "en-au",
        "french": "fr-fr",
        "frenchCA": "fr-ca",
        "german": "de-de",
        "hebrew": "he-il",
        "hindi": "hi-in",
        "indonesian": "id-id",
        "italian": "it-it",
        "japanese": "ja-jp",
        "korean": "ko-kr",
        "malay": "ms-my",
        "portuguese": "pt-br",
        "portuguesePT": "pt-pt",
        "russian": "ru-ru",
        "spanish": "es-mx",
        "spanishSP": "es-es",
        "swedish": "sv-se",
        "tamil": "ta-in",
        "thai": "th-th",
        "vietnamese": "vi-vn",
        "not found": "not found"
    }

    return lang.get(language, "not found")

def id(language):
    lang = {
        "english": "en",
        "spanish": "es",
        "korean": "kr",
        "chinese": "zh-cn",
        "chineseSP": "zh-cn",
        "chineseTR": "zh-tw",
        "russian": "ru",
        "japanese": "ja",
        "french": "fr",
        "vietnamese": "vi",
        "hindi": "hi",
        "hmong": "hmn",
        "mongolian": "mn",
        "italian": "it",
        "thai": "th",
        "tagalog": "tl",
        "hawaiian": "haw",
        "malay": "ms",
        "german": "de",
        "indonesian": "id",
        "portuguese": "pt",
        "arabic": "ar",
        "hebrew": "iw",
        "tamil": "ta",
        "not found": "not found"
    }
    id = "not found"
    for key in lang:
        if(lang[key] == language):
            id = key
    return id 


