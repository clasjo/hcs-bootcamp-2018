from chalice import Chalice
import requests
import json
import datetime

app = Chalice(app_name='chalice-starter')
apiKey = "NESSIE_API_KEY"


@app.route('/data', cors=True)
def index():
    # create the URL for the request
    accountsUrl = 'http://api.reimaginebanking.com/accounts?key={}'.format(apiKey)

    # make call to the Nessie Accounts endpoint
    accountsResponse = requests.get(accountsUrl)

    if accountsResponse.status_code == 200:


        return {"data":{"transfers":transfers,"accounts":accountsNoCards}}
    else:
        return {"data":{"transfers":[], "accounts":[]}}


@app.route('/transfer', methods=['POST'], cors=True)
def transfer():
    request = app.current_request
    json_body = request.json_body



    # redirect user to the same page, which should now show there latest transaction in the list
    return {"data": "success"}