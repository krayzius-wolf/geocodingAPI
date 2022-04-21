import parts
import json
from flask import Flask, request, Response
app = Flask(__name__)


@app.route('/getAddressDetails', methods=['POST'])
def geocoder():
    if request.json['output_format'] == 'json':
        s = parts.getinfojson(request.json)
        return s
    else:
        s = parts.getinfoxml(request.json)
        return Response(s, mimetype='text/xml')

app.run()
