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

from customer.models.list_consents_request_filters import ListConsentsRequestFilters

class TestListConsentsRequestFilters(unittest.TestCase):
    """ListConsentsRequestFilters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListConsentsRequestFilters:
        """Test ListConsentsRequestFilters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConsentsRequestFilters`
        """
        model = ListConsentsRequestFilters()
        if include_optional:
            return ListConsentsRequestFilters(
                subject_ids = [
                    ''
                    ]
            )
        else:
            return ListConsentsRequestFilters(
        )
        """

    def testListConsentsRequestFilters(self):
        """Test ListConsentsRequestFilters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
