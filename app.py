from chalice import Chalice
import requests
import json
import datetime

app = Chalice(app_name='chalice-starter')
apiKey = "NESSIE_API_KEY"


####TODO####
"""
This endpoint returns the data required to populate the frontend. you need to get all accounts and transfers from your nessie account
and add them as lists to the transfers and account variables.
"""
############
@app.route('/data', cors=True)
def index():
    # create the URL for the request
    accountsUrl = 'http://api.reimaginebanking.com/accounts?key={}'.format(apiKey)

    # make call to the Nessie Accounts endpoint
    accountsResponse = requests.get(accountsUrl)

    if accountsResponse.status_code == 200:


        return {"data":{"transfers":transfers,"accounts":accounts}}
    else:
        return {"data":{"transfers":[], "accounts":[]}}

####TODO####
"""
This endpoint creates a new transfer. You should get the neccessary account info and transfer amoiunt from the json_body variable
and call the nessie api to create a new transfer. 

json_vars

fromAccount
toAccount
amount
description
"""
############
@app.route('/transfer', methods=['POST'], cors=True)
def transfer():
    request = app.current_request
    json_body = request.json_body



    # redirect user to the same page, which should now show there latest transaction in the list
    return {"data": "success"}
