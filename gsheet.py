import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from main import abc

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/drive.file']

credentials = ServiceAccountCredentials.from_json_keyfile_name('crud.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('test4')
get_sheet = sheet.worksheet('Sheet1')

def create_Sheet():
    sheet_range = 4
    payload = [
        "hello",
        "arun" ] #dynamic paload
    store_sheet = get_sheet.insert_row(payload,sheet_range)
    return store_sheet
# create_Sheet()


# print(abc(),"==================================")



import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from main import abc

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/drive.file']

credentials = ServiceAccountCredentials.from_json_keyfile_name('crud.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('test4')
get_sheet = sheet.worksheet('Sheet1')

def create_Sheet():
    sheet_range = 4
    payload = [
        "hello",
        "arun" ] #dynamic paload
    store_sheet = get_sheet.insert_row(payload,sheet_range)
    return store_sheet
# create_Sheet()


