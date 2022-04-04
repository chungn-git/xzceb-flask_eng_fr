"""Translale English to French and vise visa using IBM Watson Language Translator API
Requirement:
    1) Create an IBM Cloud Account if not already have one
    2) Create a Language Translator service.
       This module will use OS envoronment variables for apiley and url

Structure of the Module:
    1) Create an instance of the IBM Watson Language translator
    2) Function to translate English to French:
        - Functin name: englishToFrench
        - Input (1 argument): English text
        - Output: French text
    3) Function to translate French to English
        - FrenchToEnglish
        - Input (1 argument): French text
        - Output: English text

This module will use os environment for IBM api key and url
"""
import os
# import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Authentication
authenticator = IAMAuthenticator(apikey)

# Create instance
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Function to translate English to French
def english_to_french(english_text):
    """Function translate Enlish to French
       english_text is a string argument
    """
    if english_text is not None:
        raw_translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        translation = list(raw_translation.values())[0][0]['translation']
        # print(translation)
        return translation
    print("Input is null for English, no translation")
    return None

# Function to translate French to English
def french_to_english(french_text):
    """Function to translate French to English
       french_text is a string argument
    """
    if french_text is not None:
        raw_translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        translation = list(raw_translation.values())[0][0]['translation']
        return translation
    print("Input is null for French, no translation")
    return None


if __name__ == "__main__":
    output = english_to_french('Hello')
    print(output)
    output = french_to_english('Comment ca va?')
    print(output)
