from flask import Flask, request, jsonify
from APIKeys import GOOGLEAPIKEY
import requests

GOOGLE_END_POINT = 'https://maps.googleapis.com/maps/api/place/autocomplete/json?'

app = Flask(__name__)



@app.route('/locations')
def autocomplete():

    city = request.args['city']

    r = requests.get(GOOGLE_END_POINT, params={'input': city, 'key': GOOGLEAPIKEY, 'types': '(cities)'})

    dic = r.json()

    resp = {'predictions': []}

    if dic['status'] == 'OK':
        for i in range(0, 5):
            # print dic['predictions'][i]['place_id'], dic['predictions'][i]['description']
            resp['predictions'] += [{'place_id': dic['predictions'][i]['place_id'], 'description': dic['predictions'][i]['description']}]
        for pre in resp['predictions']:
            print pre['place_id'], pre['description']
        return jsonify(resp)
    return "No cities found"


if __name__ == '__main__':
    app.run()
