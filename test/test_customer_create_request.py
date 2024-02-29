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

from customer.models.customer_create_request import CustomerCreateRequest

class TestCustomerCreateRequest(unittest.TestCase):
    """CustomerCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerCreateRequest:
        """Test CustomerCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerCreateRequest`
        """
        model = CustomerCreateRequest()
        if include_optional:
            return CustomerCreateRequest(
                tenant_id = '',
                em = customer.models.customer_em_fields.customerEMFields(
                    tenant_id = '', 
                    entity_type = '', 
                    entity_code = '', ),
                name = '',
                surname = '',
                email = '',
                birthdate = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                gender = '',
                enabled = True,
                source = '',
                addresses = [
                    customer.models.customer_address_entity.customerAddressEntity(
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
                            }, )
                    ],
                phone_number = '',
                nationality = '',
                groups = [
                    ''
                    ],
                deleted = True,
                newsletters = [
                    customer.models.customer_newsletter_request.customerNewsletterRequest(
                        newsletter_grn = '', 
                        name = '', 
                        subscribed = True, )
                    ],
                do_not_notify = True,
                attributes = {
                    'key' : {
                        'key' : None
                        }
                    },
                migrated_password = customer.models.customer_password.customerPassword(
                    data = {
                        'key' : ''
                        }, 
                    enabled = True, 
                    type = 'PASSWORD_TYPE_UNKNOWN', ),
                market = '',
                preferred_locale = '',
                tax_code = '',
                certified_email = '',
                sdi_code = '',
                fiscal_code = '',
                company_name = '',
                additional_info = None,
                external_ids = {
                    'key' : ''
                    },
                consent = customer.models.customer_create_consent_request.customerCreateConsentRequest(
                    preferences = {
                        'key' : True
                        }, ),
                aggregation_id = ''
            )
        else:
            return CustomerCreateRequest(
        )
        """

    def testCustomerCreateRequest(self):
        """Test CustomerCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
