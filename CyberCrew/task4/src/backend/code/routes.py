from flask import request, jsonify
import requests as req

from code import app
import re
from sys import stdout, stderr

@app.route('/resolve', methods=['GET', 'POST'])
def resolve():
    domain = request.args.get('domain')
    get_flag = request.args.get('get_flag')

    if not domain:
        return jsonify({'error': 'Check fields and try again.'})

    if '://' in domain:
        return jsonify({'error': 'The "domain"" field expected a domain, but received a URL'})

    headers = {'FLAG': 'FLAG{7bdaf9e80649ba47499e3fc}'}

    try:
        req.head(f'http://{domain}', headers=headers)
    except req.exceptions.ConnectionError:
        return {'status': 'fail'}

    headers = {
        'domainName': domain,
        'search': domain,
        'web-lookup-search': 'true',
    }

    response = req.post(f'http://ip-api.com/json/{domain}', headers=headers).json()
    return jsonify(response)
