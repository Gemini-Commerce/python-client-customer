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

from customer.models.customer_list_groups_request import CustomerListGroupsRequest

class TestCustomerListGroupsRequest(unittest.TestCase):
    """CustomerListGroupsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerListGroupsRequest:
        """Test CustomerListGroupsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerListGroupsRequest`
        """
        model = CustomerListGroupsRequest()
        if include_optional:
            return CustomerListGroupsRequest(
                tenant_id = '',
                page_size = 56,
                page_token = '',
                filter = customer.models.customer_list_groups_request_filter.customerListGroupsRequestFilter(
                    search_term = '', ),
                filters_mask = ''
            )
        else:
            return CustomerListGroupsRequest(
        )
        """

    def testCustomerListGroupsRequest(self):
        """Test CustomerListGroupsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
