from __future__ import print_function

import os

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, tools
from django.conf import settings

from config.settings import BASE_DIR
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build

import requests

import google.oauth2.credentials


def retrieve_response(form_id, access_token, refresh_token):

    SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
    API_SERVICE = "forms"
    API_VERSION = "v1"

    credentials = {
        "token": access_token,
        # "refresh_token": refresh_token,
        # "token_uri": token_uri,
        "client_id": settings.GOOGLE_OAUTH2_CLIENT_ID,
        "client_secret": settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        "scopes": SCOPES,
    }

    service = build("forms", "v1", credentials=credentials)
    result = service.forms().responses().list(formId=form_id).execute()
    return result

    # print(str(BASE_DIR) + "/forms/tokens/token.json")
    # store = file.Storage(str(BASE_DIR) + "/forms/tokens/token.json")
    # creds = None
    # if not creds or creds.invalid:
    #     secret = {
    #         "web":{
    #             "client_id": settings.GOOGLE_OAUTH2_CLIENT_ID,
    #             "project_id": "nomado-workflow",
    #             "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #             "token_uri": "https://oauth2.googleapis.com/token",
    #             "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #             "client_secret": settings.GOOGLE_OAUTH2_CLIENT_SECRET,
    #             "redirect_uris":[
    #                 "http://127.0.0.1:8000/api/v1/forms/list/",
    #                 "https://nextjs-todos-e3q3.vercel.app/api/v1/forms/list/"
    #                 ]
    #             }
    #     }
    #     flow = InstalledAppFlow.from_client_config(secret, SCOPES)
    #     creds = tools.run_flow(flow, store)
    # service = discovery.build('forms', 'v1', http=creds.authorize(
    #     Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

    # # Prints the responses of your specified form:
    # result = service.forms().responses().list(formId=form_id).execute()
    # return result

def retrieve_content(form_id, access_token, refresh_token):
    SCOPES = "https://www.googleapis.com/auth/forms.body.readonly"
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

    # REQUEST_URL = "https://forms.googleapis.com/v1/forms/" + form_id

    # headers = {
    #     "Authorization: Barer " + access_token,
    #     "Content-Type: application/json"
    # }

    # response = requests.post(
    #     REQUEST_URL,
    #     params={"token": access_token},
    #     headers={"content-type": "application/x-www-form-urlencoded"})

    dict_credentials = {
        "token": access_token,
        "refresh_token": refresh_token,
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "client_id": settings.GOOGLE_OAUTH2_CLIENT_ID,
        "client_secret": settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        "scopes": SCOPES,
    }
    credentials = google.oauth2.credentials.Credentials(**dict_credentials)


    service = build("forms", "v1", credentials=credentials)
    result = service.forms().get(formId=form_id).execute()
    return result
