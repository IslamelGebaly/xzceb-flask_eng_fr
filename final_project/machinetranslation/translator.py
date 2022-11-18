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

def englishToFrench(englishText):
    frenchText = translator_instance.translate(text=englishText, model_id="en-fr").get_result()
    return [line['translation'] for line in frenchText["translations"][:]]

def FrenchToEnglish(frenchText):
    englishText = translator_instance.translate(text=frenchText, model_id="fr-en").get_result()
    return [line['translation'] for line in englishText["translations"][:]]

if __name__ == "__main__":
    frenchText = translator_instance.translate(text="Hello", model_id="en-fr").get_result()
    print(*[line["translation"] for line in frenchText["translations"][:]])