from translate import Translator
from textblob import TextBlob


class Translation:

    def __init__(self, text):
        self.text = text

    def translate_word(self):

        lang = TextBlob(self.text)
        if lang.detect_language() == 'en':

            translator = Translator(from_lang='en', to_lang='hi')
            translation = translator.translate(self.text)
            return translation
        else:
            translator = Translator(from_lang='hi', to_lang='en')
            translation = translator.translate(self.text)
            return translation
