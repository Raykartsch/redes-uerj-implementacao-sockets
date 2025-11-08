from deep_translator import GoogleTranslator

def translate(word, language):
    return GoogleTranslator(source='pt', target=language).translate(word)