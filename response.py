import requests, json
url = "https://devapi.endato.com/PersonSearch"
response = ''

payload1 = [
    {
        "Phone": "702-808-1141"
        },
        {
          "Phone": "702-808-1140",
        },
          {
        "Phone":"702-808-1149"
        }
    ]

headers = {
    "Accept": "application/json",
    "galaxy-ap-name": "f5778850-ab32-401e-bca1-377606919ae0",
    "galaxy-ap-password": "54e01deb091c4df2bef74481b5093453",
    "galaxy-search-type": "Person",
    "Content-Type": "application/json"
}
for i in payload1:
    response = requests.post(url,json=i, headers=headers)
    res = json.loads(response.text).get('persons')[0].get('name').get('firstName')
    print(res,"====")





# @app.route('/abc', methods=['GET', 'POST'])
# def abc():
#     context = ''
#     if request.method == 'POST':
#         upload_phone = request.files['upload_phone']
#         myfile = upload_phone.read()
#         d = json.loads(myfile)
#         for getPhoneNumber in d:
#
#             headers = {
#                 "Accept": "application/json",
#                 "galaxy-ap-name": "f5778850-ab32-401e-bca1-377606919ae0",
#                 "galaxy-ap-password": "54e01deb091c4df2bef74481b5093453",
#                 "galaxy-search-type": "Person",
#                 "Content-Type": "application/json"
#             }
#             response = requests.post(url, json=getPhoneNumber, headers=headers)
#             data = json.loads(response.text)
#             get_data = data.get('persons')
#
#             for show_data in get_data:
#                 firstName = show_data.get('name').get('firstName')
#                 lastName = show_data.get('name').get('lastName')
#                 fullName = firstName + ' ' + lastName
#                 age = show_data.get('age')
#                 dobFirstSeen = show_data.get('dobFirstSeen')
#                 addresses = show_data.get('addresses')[0]
#                 context = {
#                     "Name":fullName,
#                     "age":age,
#                     "Dob":dobFirstSeen,
#                     "addresses":addresses
#                 }
#         print(context.keys())
#     return render_template('table.html',context=context)
