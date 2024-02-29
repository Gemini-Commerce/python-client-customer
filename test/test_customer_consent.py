# coding: utf-8

"""
    CDP Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from customer.models.customer_consent import CustomerConsent

class TestCustomerConsent(unittest.TestCase):
    """CustomerConsent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerConsent:
        """Test CustomerConsent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerConsent`
        """
        model = CustomerConsent()
        if include_optional:
            return CustomerConsent(
                id = '',
                grn = '',
                preferences = {
                    'key' : True
                    },
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                source = 'CONSENT_SOURCE_UNKNOWN',
                author = '',
                subject_id = ''
            )
        else:
            return CustomerConsent(
        )
        """

    def testCustomerConsent(self):
        """Test CustomerConsent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
