# -*- coding: utf-8 -*-
#
#    bitcoinlib - Compact Python Bitcoin Library
#    blockchain_info client
#    © 2016 November - 1200 Web Development <http://1200wd.com/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import requests
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
import json
from bitcoinlib.config.services import serviceproviders


class BlockchainInfoClient:

    def __init__(self, network):
        try:
            self.url = serviceproviders[network]['blockchaininfo'][1]
        except:
            raise Warning("This Network is not supported by BlockchainInfoClient")

    def request(self, method, parameter, parlist):
        if parameter:
            parameter += '/'
        url = self.url + method + parameter
        if parlist:
            url += '?' + urlencode(parlist)
        resp = requests.get(url)
        data = json.loads(resp.text)
        return data

    def getbalance(self, addresslist):
        parlist = [('active', '|'.join(addresslist))]
        res = self.request('multiaddr', '', parlist)
        balance = 0
        for address in res['addresses']:
            balance += address['final_balance']

        return balance
