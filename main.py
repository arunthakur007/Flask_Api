import json
from number_check import number_checker
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


@app.route('/', methods=['GET', 'POST'])
def Search():
    all_datas = []
    content = ''
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
            emp = []
            for i in get_data:
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

                for key,value in context.items():
                    all_datas.append((value))
                sheet_range = 2
                payload = [
                    all_datas[0],
                    all_datas[1],
                    all_datas[2],
                    all_datas[3]
                ]
                get_sheet.insert_row(payload, sheet_range)
        return render_template('home.html',all_data=all_data)
    except:
        return render_template('home.html')

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':

        phone = request.args['phone']
        data = number_checker(phone)
        print(data,"===")
        # abc()
        return data

if __name__ == '__main__':
    app.run()


