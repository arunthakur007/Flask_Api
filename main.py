import json
from flask import Flask,render_template,request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

app = Flask(__name__)
url = "https://devapi.endato.com/PersonSearch"

scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file']

credentials = ServiceAccountCredentials.from_json_keyfile_name('crud.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('test4')
get_sheet = sheet.worksheet('Sheet1')

def getRecord():
    Google_sheet_value = get_sheet.get_all_values()
    store_record = Google_sheet_value[1:]
    return store_record

def update_gsheet(payloads,sheet_range):
    update_sheet = get_sheet.update(sheet_range,[payloads])
    return update_sheet

@app.route('/', methods=['GET', 'POST'])
def Search():
    sheet_range = 2
    sheet_ranges = 1
    count = 1
    context = {}
    all_data = list()
    try:
        if request.method == 'POST':
            phone = request.form['phone']
            payload = {"Phone": phone}
            headers = {
                "Accept": "application/json",
                "galaxy-ap-name": "f5778850-ab32-401e-bca1-377606919ae0",
                "galaxy-ap-password": "54e01deb091c4df2bef74481b5093453",
                "galaxy-search-type": "Person",
                "Content-Type": "application/json"
            }
            response = requests.post(url, json=payload, headers=headers)
            data = json.loads(response.text)
            get_data = data.get('persons')
            for i in get_data:
                # New.................................
                dummy = i.get('associates')
                for getdummy in dummy:
                    fName = getdummy.get('name').get('firstName')
                    LName = getdummy.get('name').get('lastName')
                    SFullName  = fName+LName

                firstName = i.get('name').get('firstName')
                lastName = i.get('name').get('lastName')
                fullName = firstName + ' ' + lastName
                age = i.get('age')
                dobFirstSeen = i.get('dobFirstSeen')
                addres = i.get('addresses')
                for getAddress in addres:
                    addresses = getAddress.get('fullAddress')
                context = {
                    "Name": fullName,
                    "age": age,
                    "Dob": dobFirstSeen,
                    "addresses": addresses
                }
                all_data.append(context)
            for k in all_data:
                SName = k.get('Name')
                SAge = k.get('age')
                SDob = k.get('Dob')
                Saddress = k.get('addresses')
                Spayload = [SName,SAge,SDob,Saddress]
                GoogleSheetRecords = getRecord()
                for getRcd in GoogleSheetRecords:
                    if SName in getRcd:
                        sheet_ranges = f'Sheet1!A{count}:D{count}'
                        update_gsheet(Spayload,sheet_ranges)
                    else:
                        print(getRcd,"create","=====")
                sheet_ranges +=1
                get_sheet.insert_row(Spayload, sheet_range)
        return render_template('home.html',all_data=all_data)
    except:
        return render_template('home.html')

if __name__ == '__main__':
    app.run()




