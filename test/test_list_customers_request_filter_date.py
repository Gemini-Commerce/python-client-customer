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

from customer.models.list_customers_request_filter_date import ListCustomersRequestFilterDate

class TestListCustomersRequestFilterDate(unittest.TestCase):
    """ListCustomersRequestFilterDate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListCustomersRequestFilterDate:
        """Test ListCustomersRequestFilterDate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListCustomersRequestFilterDate`
        """
        model = ListCustomersRequestFilterDate()
        if include_optional:
            return ListCustomersRequestFilterDate(
                var_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ListCustomersRequestFilterDate(
        )
        """

    def testListCustomersRequestFilterDate(self):
        """Test ListCustomersRequestFilterDate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
