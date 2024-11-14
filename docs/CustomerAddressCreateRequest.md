# # CustomerAddressCreateRequest


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id**| **str** |   | [optional]
**customer_id**| **str** |   | [optional]
**em**| [**CustomerEMFields**](CustomerEMFields.md) |   | [optional]
**name**| **str** |   | [optional]
**surname**| **str** |   | [optional]
**street**| **str** |   | [optional]
**number**| **str** |   | [optional]
**zip**| **str** |   | [optional]
**city**| **str** |   | [optional]
**province**| **str** |   | [optional]
**phone_number**| **str** |   | [optional]
**fiscal_code**| **str** |   | [optional]
**vat_number**| **str** |   | [optional]
**kind**| [**CustomerAddressCreateRequestKind**](CustomerAddressCreateRequestKind.md) |  for more information please, see Model/CustomerAddressCreateRequestKind.php  | [optional] [default to CustomerAddressCreateRequestKind.SHIPPING]
**default**| **bool** |   | [optional]
**country**| **str** |   | [optional]
**attributes**| [**Dict[str, ProtobufAny]**](ProtobufAny.md) |   | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

