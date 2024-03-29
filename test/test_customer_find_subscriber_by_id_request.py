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

from customer.models.customer_find_subscriber_by_id_request import CustomerFindSubscriberByIdRequest

class TestCustomerFindSubscriberByIdRequest(unittest.TestCase):
    """CustomerFindSubscriberByIdRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerFindSubscriberByIdRequest:
        """Test CustomerFindSubscriberByIdRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerFindSubscriberByIdRequest`
        """
        model = CustomerFindSubscriberByIdRequest()
        if include_optional:
            return CustomerFindSubscriberByIdRequest(
                tenant_id = '',
                subscriber_id = ''
            )
        else:
            return CustomerFindSubscriberByIdRequest(
        )
        """

    def testCustomerFindSubscriberByIdRequest(self):
        """Test CustomerFindSubscriberByIdRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
