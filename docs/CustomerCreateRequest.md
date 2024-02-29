# # CustomerCreateRequest


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id**| **str** |   | [optional]
**em**| [**CustomerEMFields**](CustomerEMFields.md) |   | [optional]
**name**| **str** |   | [optional]
**surname**| **str** |   | [optional]
**email**| **str** |   | [optional]
**birthdate**| **datetime** |   | [optional]
**gender**| **str** |   | [optional]
**enabled**| **bool** |   | [optional]
**source**| **str** |   | [optional]
**addresses**| [**List[CustomerAddressEntity]**](CustomerAddressEntity.md) |   | [optional]
**phone_number**| **str** |   | [optional]
**nationality**| **str** |   | [optional]
**groups**| **List[str]** |   | [optional]
**deleted**| **bool** |   | [optional]
**newsletters**| [**List[CustomerNewsletterRequest]**](CustomerNewsletterRequest.md) |   | [optional]
**do_not_notify**| **bool** |   | [optional]
**attributes**| [**Dict[str, ProtobufAny]**](ProtobufAny.md) |   | [optional]
**migrated_password**| [**CustomerPassword**](CustomerPassword.md) |   | [optional]
**market**| **str** |   | [optional]
**preferred_locale**| **str** |   | [optional]
**tax_code**| **str** |   | [optional]
**certified_email**| **str** |   | [optional]
**sdi_code**| **str** |   | [optional]
**fiscal_code**| **str** |   | [optional]
**company_name**| **str** |   | [optional]
**additional_info**| **object** |   | [optional]
**external_ids**| **Dict[str, str]** |   | [optional]
**consent**| [**CustomerCreateConsentRequest**](CustomerCreateConsentRequest.md) |   | [optional]
**aggregation_id**| **str** |   | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

