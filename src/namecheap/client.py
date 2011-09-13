# -*- coding: utf-8 -*-
#
# Copyright (c) 2011, Martín Raúl Villalba
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import urllib2
from decimal import Decimal
from xml.etree import ElementTree

from namecheap.api import NCDomain, NCDomainDNS, NCDomainNS, NCDomainTransfer
from namecheap.api import NCSSL, NCUser, NCUserAddress

NC_SANDBOX = "https://api.sandbox.namecheap.com/xml.response"
NC_PRODUCTION = "https://api.namecheap.com/xml.response"
NC_NAMESPACE = "http://api.namecheap.com/xml.response"

class NCClient(object):
    def __init__(
            self, apikey, apiuser, username,
            client_ip, env=NC_PRODUCTION):
        self.environment = env
        self.apikey = apikey
        self.apiuser = apiuser
        self.username = username
        self.client_ip = client_ip

        self.domain = NCDomain(self)
        self.dns = NCDomainDNS(self)
        self.ns = NCDomainNS(self)
        self.transfer = NCDomainTransfer(self)
        self.ssl = NCSSL(self)
        self.user = NCUser(self)
        self.address = NCUserAddress(self)

    def _make_url(self, command, args):
        flat_args = ""

        for k, v in args.items():
            flat_args += "&{0}={1}".format(k, v)

        url = "{0}?ApiUser={1}&ApiKey={2}&UserName={3}&ClientIP={4}" \
              "&Command={5}{6}".format(
                  self.environment,
                  self.apiuser,
                  self.apikey,
                  self.username,
                  self.client_ip,
                  command,
                  flat_args,
              )

        return url

    def _name(self, tag):
        return '{' + NC_NAMESPACE + '}' + tag

    def _process_response(self, response):
        doc = {
            'Status': None,
            'Errors': None,
            'Warnings': None,
            'RequestedCommand': None,
            'CommandResponse': None,
            'Server': None,
            'GMTTimeDifference': None,
            'ExecutionTime': None,
        }

        root = ElementTree.fromstring(response)

        doc['Status'] = root.attrib['Status']

        errors = root.findall(self._name('Errors'))
        if len(errors) > 0 and len(errors[0]) > 0:
            doc['Errors'] = {
                'Number': errors[0][0].attrib['Number'],
                'Text': errors[0][0].text
            }

        warnings = root.findall(self._name('Warnings'))
        if len(warnings) > 0 and len(warnings[0]) > 0:
            doc['Warnings'] = {
                'Number': warning[0][0].attrib['Number'],
                'Text': warning[0][0].text
            }

        command = root.findall(self._name('RequestedCommand'))
        if len(command) > 0:
            doc['RequestedCommand'] = command[0].text

        cmdres = root.findall(self._name('CommandResponse'))
        if len(cmdres) > 0:
            doc['CommandResponse'] = cmdres[0]

        server = root.findall(self._name('Server'))
        if len(server) > 0:
            doc['Server'] = server[0].text

        gmttime = root.findall(self._name('GMTTimeDifference'))
        if len(gmttime) > 0:
            doc['GMTTimeDifference'] = gmttime[0].text

        exectime = root.findall(self._name('ExecutionTime'))
        if len(exectime) > 0:
            doc['ExecutionTime'] = Decimal(exectime[0].text)

        return doc

    def _call(self, command, args={}):
        url = self._make_url(command, args)
        response = urllib2.urlopen(url)
        doc = self._process_response(response.read())

        return doc

