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

from customer.models.customer_remove_default_address_request import CustomerRemoveDefaultAddressRequest

class TestCustomerRemoveDefaultAddressRequest(unittest.TestCase):
    """CustomerRemoveDefaultAddressRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerRemoveDefaultAddressRequest:
        """Test CustomerRemoveDefaultAddressRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerRemoveDefaultAddressRequest`
        """
        model = CustomerRemoveDefaultAddressRequest()
        if include_optional:
            return CustomerRemoveDefaultAddressRequest(
                tenant_id = '',
                customer_id = '',
                address_id = ''
            )
        else:
            return CustomerRemoveDefaultAddressRequest(
        )
        """

    def testCustomerRemoveDefaultAddressRequest(self):
        """Test CustomerRemoveDefaultAddressRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()