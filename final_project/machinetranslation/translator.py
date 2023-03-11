"""
This module provides functions to translate text from English to French and from French to English
using the IBM Watson Language Translator service.
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Authenticate using IAMAuthenticator
authenticator = IAMAuthenticator(apikey)

# Create an instance of LanguageTranslatorV3
translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)

# Set the service URL
translator.set_service_url(url)

def englishToFrench(english_text):
    """
    Translates English text to French using the IBM Watson Language Translator
    """
    translation = translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    french_text = translation['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    """
    Translates French text to English using the IBM Watson Language Translator
    """
    translation = translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()

    english_text = translation['translations'][0]['translation']
    return english_text
