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

from customer.models.customer_create_subscriber_request import CustomerCreateSubscriberRequest

class TestCustomerCreateSubscriberRequest(unittest.TestCase):
    """CustomerCreateSubscriberRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerCreateSubscriberRequest:
        """Test CustomerCreateSubscriberRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerCreateSubscriberRequest`
        """
        model = CustomerCreateSubscriberRequest()
        if include_optional:
            return CustomerCreateSubscriberRequest(
                tenant_id = '',
                subscriber = customer.models.customer_subscriber_request.customerSubscriberRequest(
                    name = '', 
                    lastname = '', 
                    email = '', 
                    country = '', 
                    gender = '', 
                    birthdate = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    nationality = '', 
                    em = customer.models.customer_em_fields.customerEMFields(
                        tenant_id = '', 
                        entity_type = '', 
                        entity_code = '', ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    newsletters = [
                        customer.models.customer_newsletter_request.customerNewsletterRequest(
                            newsletter_grn = '', 
                            name = '', 
                            subscribed = True, )
                        ], 
                    market = '', 
                    preferred_locale = '', 
                    consent = customer.models.customer_create_consent_request.customerCreateConsentRequest(
                        preferences = {
                            'key' : True
                            }, ), )
            )
        else:
            return CustomerCreateSubscriberRequest(
        )
        """

    def testCustomerCreateSubscriberRequest(self):
        """Test CustomerCreateSubscriberRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()