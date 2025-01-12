'''
Module for using IBM ai translation
api for translating english to french
and from french to english
'''
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey=apikey)
translator_instance = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
translator_instance.set_service_url(url)

def englishToFrench(english_text):
    '''
    function for translating english to french
    '''
    if english_text is not None:
        french_text = translator_instance.translate(text=english_text, model_id="en-fr").get_result()
        return [line['translation'] for line in french_text["translations"][:]]
    return None

def frenchToEnglish(french_text):
    '''
    function for translating french to english
    '''
    if french_text is not None:
        english_text = translator_instance.translate(text=french_text, model_id="fr-en").get_result()
        return [line['translation'] for line in english_text["translations"][:]]
    return None

if __name__ == "__main__":
    frenchText = translator_instance.translate(text="Hello", model_id="en-fr").get_result()
    print(*[line["translation"] for line in frenchText["translations"][:]])