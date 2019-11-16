# add API connection packages
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient      # Azure API imports
from msrest.authentication import CognitiveServicesCredentials
import discord


# Azure API information for Text analysis
azure_api_key = "d671436ef9ca42fb9b9205b8b209528c"
credentials = CognitiveServicesCredentials(azure_api_key)
azure_endpoint_url = "https://eastus.api.cognitive.microsoft.com/"
azure_text_analytics = TextAnalyticsClient(endpoint=azure_endpoint_url, credentials=credentials)

# Discord API stuff and globals
