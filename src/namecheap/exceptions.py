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

NC_SYSTEM_TEXT = {
    '10': 'Authentication System',
    '20': 'Validation Error',
    '25': 'Payment Error / Order creation Error',
    '30': 'Provider Error',
    '35': 'Policy Error',
    '40': 'System Error',
    '50': 'Unknown Exceptions',
}

NC_ERROR_TEXT = {
    '10': 'Missing',
    '11': 'Invalid',
    '12': 'Type Mismatch',
    '13': 'Out of Range',
    '14': 'Duplicate',
    '15': 'Policy Violation',
    '16': 'Unauthorized',
    '17': 'Disabled / Locked',
    '18': 'Declined',
    '19': 'Not available / Not Found',
    '20': 'Expired',
    '21': 'Connection Failed',
    '22': 'Failed to retrieve',
    '23': 'Failed to add',
    '24': 'Failed to update / change',
    '25': 'Failed to delete',
    '26': 'Failed to deduct',
    '27': 'Failed to send',
    '28': 'Failed to Purchase/Extend/Reactivate',
    '29': 'Failed',
    '30': 'Unsupported',
    '31': 'Error Response From Provider',
    '32': 'Logical Error',
    '33': 'Conflict',
    '34': 'Down for Maintenance',
    '35': 'Database Error',
    '50': 'Unknown',
    '80': 'Warning ( generic)',
}

NC_PARAM_TEXT = {
    '101': 'ApiUser',
    '251': 'CiraRegistrantDesc',
    '102': 'ApiKey',
    '252': 'CiraTrademarkNo',
    '103': 'UserName',
    '253': 'CiraOrgRegisteredIn',
    '104': 'Command',
    '254': 'COUKLegalType',
    '105': 'ClientIp',
    '255': 'COUKCompanyID',
    '150': 'RequestIP',
    '256': 'COUKRegisteredfor',
    '151': 'FirstName',
    '257': 'COUKRegOptOut',
    '152': 'LastName',
    '258': 'ORGUKLegalType',
    '153': 'EmailAddress',
    '259': 'ORGUKCompanyID',
    '154': 'JobTitle',
    '260': 'ORGUKRegisteredfor',
    '155': 'Organization',
    '261': 'ORGUKRegOptOut',
    '156': 'Address1',
    '262': 'MEUKLegalType',
    '157': 'Address2',
    '263': 'MEUKCompanyID',
    '158': 'City',
    '264': 'MEUKRegisteredfor',
    '159': 'StateProvince',
    '265': 'MEUKRegOptOut',
    '160': 'StateProvinceChoice',
    '266': 'EUWhoisPolicy',
    '161': 'Zip',
    '267': 'EUAgreeDelete',
    '162': 'Country',
    '268': 'EUAdrLang',
    '163': 'Phone',
    '269': 'AddFreeWhoisguard',
    '164': 'PhoneExt',
    '270': 'WGEnabled',
    '165': 'Fax',
    '271': 'AddFreePositiveSSL',
    '166': 'DomainName',
    '272': 'ListType',
    '167': 'Years',
    '273': 'SearchTerm',
    '168': 'NameServers',
    '274': 'Page',
    '169': 'DomainList',
    '275': 'PageSize',
    '170': 'PromotionCode',
    '276': 'SortBy',
    '171': 'RegistrantOrganizationName',
    '277': 'AddressId',
    '172': 'RegistrantJobTitle',
    '278': 'LockAction',
    '173': 'RegistrantFirstName',
    '279': 'Sld',
    '174': 'RegistrantLastName',
    '280': 'Tld',
    '175': 'RegistrantAddress1',
    '281': 'Host_MailBox',
    '176': 'RegistrantAddress2',
    '282': 'Host_ForwardTo',
    '177': 'RegistrantCity',
    '283': 'Host_HostName',
    '178': 'RegistrantStateProvince',
    '284': 'Host_RecordType',
    '179': 'RegistrantStateProvinceChoice',
    '285': 'Host_Address',
    '180': 'RegistrantPostalCode',
    '286': 'Host_MXPref',
    '181': 'RegistrantCountry',
    '287': 'EmailType',
    '182': 'RegistrantPhone',
    '288': 'Nameserver',
    '183': 'RegistrantFax',
    '289': 'IP',
    '184': 'RegistrantEmailAddress',
    '290': 'OldIP',
    '185': 'RegistrantPhoneExt',
    '291': 'EPPCode',
    '186': 'TechOrganizationName',
    '292': 'TransferID',
    '187': 'TechJobTitle',
    '293': 'Resubmit',
    '188': 'TechFirstName',
    '294': 'CertificateID',
    '189': 'TechLastName',
    '295': 'ApproverEmail',
    '190': 'TechAddress1',
    '296': 'CSR',
    '191': 'TechAddress2',
    '297': 'WebServerType',
    '192': 'TechCity',
    '298': 'Type',
    '193': 'TechStateProvince',
    '299': 'PurchaseValidateId',
    '194': 'TechStateProvinceChoice',
    '300': 'CertificateType',
    '195': 'TechPostalCode',
    '301': 'SSLType',
    '196': 'TechCountry',
    '302': 'OldPassword',
    '197': 'TechPhone',
    '303': 'ResetCode',
    '198': 'TechFax',
    '304': 'NewPassword',
    '199': 'TechEmailAddress',
    '305': 'NewUserPassword',
    '200': 'TechPhoneExt',
    '306': 'NewUserName',
    '201': 'AdminOrganizationName',
    '307': 'AcceptTerms',
    '202': 'AdminJobTitle',
    '308': 'AcceptNews',
    '203': 'AdminFirstName',
    '309': 'IgnoreDuplicateEmailAddress',
    '204': 'AdminLastName',
    '310': 'InvoiceId',
    '205': 'AdminAddress1',
    '311': 'InvoiceSource',
    '206': 'AdminAddress2',
    '312': 'Amount',
    '207': 'AdminCity',
    '313': 'Currency',
    '208': 'AdminStateProvince',
    '314': 'Comments',
    '209': 'AdminStateProvinceChoice',
    '315': 'FindBy',
    '210': 'AdminPostalCode',
    '316': 'FindByValue',
    '211': 'AdminCountry',
    '317': 'EmailFromName',
    '212': 'AdminPhone',
    '318': 'EmailFrom',
    '213': 'AdminFax',
    '319': 'URLPattern',
    '214': 'AdminEmailAddress',
    '320': 'AddressName',
    '215': 'AdminPhoneExt',
    '321': 'DefaultYN',
    '216': 'AuxBillingOrganizationName',
    '322': 'ExtendedAttributes',
    '217': 'AuxBillingJobTitle',
    '323': 'DomainContacts',
    '218': 'AuxBillingFirstName',
    '324': 'RegistrantContacts',
    '219': 'AuxBillingLastName',
    '325': 'TechContacts',
    '220': 'AuxBillingAddress1',
    '326': 'AdminContacts',
    '221': 'AuxBillingAddress2',
    '327': 'AuxbillingContacts',
    '222': 'AuxBillingCity',
    '328': 'EmailForwardingRecords',
    '223': 'AuxBillingStateProvince',
    '329': 'TransferStatus',
    '224': 'AuxBillingStateProvinceChoice',
    '330': 'HostRecords',
    '225': 'AuxBillingPostalCode',
    '331': 'Status',
    '226': 'AuxBillingCountry',
    '332': 'ConfigFile',
    '227': 'AuxBillingPhone',
    '333': 'XmlFile',
    '228': 'AuxBillingFax',
    '334': 'Fullfillmentemail',
    '229': 'AuxBillingEmailAddress',
    '335': 'Password',
    '230': 'AuxBillingPhoneExt',
    '336': 'UserAddress',
    '231': 'BillingOrganizationName',
    '900': 'Unknown',
    '232': 'BillingJobTitle',
    '401': 'Expiration',
    '233': 'BillingFirstName',
    '402': 'Creation',
    '234': 'BillingLastName',
    '403': 'Registration',
    '235': 'BillingAddress1',
    '404': 'Auto',
    '236': 'BillingAddress2',
    '405': 'Account',
    '237': 'BillingCity',
    '406': 'Available',
    '238': 'BillingStateProvince',
    '407': 'WhoisGuard',
    '239': 'BillingStateProvinceChoice',
    '408': 'Authentication',
    '240': 'BillingPostalCode',
    '409': 'Order',
    '241': 'BillingCountry',
    '410': 'Too',
    '242': 'BillingPhone',
    '411': 'Too',
    '243': 'BillingFax',
    '412': 'Authentication',
    '244': 'BillingEmailAddress',
    '413': 'Authorization',
    '245': 'BillingPhoneExt',
    '510': 'Provider',
    '246': 'RegistrantNexus',
    '511': 'Provider',
    '247': 'RegistrantNexusCountry',
    '512': 'Cryptography',
    '248': 'RegistrantPurpose',
    '513': 'Encryption',
    '249': 'CIRAType',
    '514': 'Decryption',
    '250': 'CiraRegistrant',
}

class NCException(Exception):
    def __init__(self, doc):
        self.doc = doc
        self.number = doc['Errors']['Number']
        self.system = self.number[0:2]
        self.error = self.number[2:4]
        self.param = self.number[4:7]
        self.text = doc['Errors']['Text']

        self.system_text = NC_SYSTEM_TEXT[self.system]
        self.error_text = NC_ERROR_TEXT[self.error]
        self.param_text = NC_PARAM_TEXT[self.param]

        Exception.__init__(
            self,
            '[{0}-{1}-{2}] {3}'.format(
                self.system, self.error,
                self.param, self.text)
        )

class NCAuthenticationError(NCException):
    pass

class NCValidationError(NCException):
    pass

class NCPaymentError(NCException):
    pass

class NCProviderError(NCException):
    pass

class NCPolicyError(NCException):
    pass

class NCSystemError(NCException):
    pass

class NCUnknownError(NCException):
    pass

