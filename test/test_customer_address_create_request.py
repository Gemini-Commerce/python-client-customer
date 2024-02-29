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

from customer.models.customer_address_create_request import CustomerAddressCreateRequest

class TestCustomerAddressCreateRequest(unittest.TestCase):
    """CustomerAddressCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerAddressCreateRequest:
        """Test CustomerAddressCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerAddressCreateRequest`
        """
        model = CustomerAddressCreateRequest()
        if include_optional:
            return CustomerAddressCreateRequest(
                tenant_id = '',
                customer_id = '',
                em = customer.models.customer_em_fields.customerEMFields(
                    tenant_id = '', 
                    entity_type = '', 
                    entity_code = '', ),
                name = '',
                surname = '',
                street = '',
                number = '',
                zip = '',
                city = '',
                province = '',
                phone_number = '',
                fiscal_code = '',
                vat_number = '',
                kind = 'SHIPPING',
                default = True,
                country = '',
                attributes = {
                    'key' : {
                        'key' : None
                        }
                    }
            )
        else:
            return CustomerAddressCreateRequest(
        )
        """

    def testCustomerAddressCreateRequest(self):
        """Test CustomerAddressCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()