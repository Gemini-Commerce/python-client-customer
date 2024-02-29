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

from customer.models.customer_update_group_request import CustomerUpdateGroupRequest

class TestCustomerUpdateGroupRequest(unittest.TestCase):
    """CustomerUpdateGroupRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerUpdateGroupRequest:
        """Test CustomerUpdateGroupRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerUpdateGroupRequest`
        """
        model = CustomerUpdateGroupRequest()
        if include_optional:
            return CustomerUpdateGroupRequest(
                tenant_id = '',
                group_id = '',
                payload = customer.models.customer_update_group_request_payload.customerUpdateGroupRequestPayload(
                    name = '', ),
                field_mask = ''
            )
        else:
            return CustomerUpdateGroupRequest(
        )
        """

    def testCustomerUpdateGroupRequest(self):
        """Test CustomerUpdateGroupRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
