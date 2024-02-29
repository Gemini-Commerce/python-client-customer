# coding: utf-8

"""
    CDP Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from customer.models.customer_address_entity_kind import CustomerAddressEntityKind
from customer.models.customer_em_fields import CustomerEMFields
from customer.models.protobuf_any import ProtobufAny
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomerAddressEntity(BaseModel):
    """
    CustomerAddressEntity
    """ # noqa: E501
    em: Optional[CustomerEMFields] = None
    name: Optional[StrictStr] = None
    surname: Optional[StrictStr] = None
    street: Optional[StrictStr] = None
    number: Optional[StrictStr] = None
    zip: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    province: Optional[StrictStr] = None
    phone_number: Optional[StrictStr] = Field(default=None, alias="phoneNumber")
    fiscal_code: Optional[StrictStr] = Field(default=None, alias="fiscalCode")
    vat_number: Optional[StrictStr] = Field(default=None, alias="vatNumber")
    kind: Optional[CustomerAddressEntityKind] = None
    default: Optional[StrictBool] = None
    country: Optional[StrictStr] = None
    attributes: Optional[Dict[str, ProtobufAny]] = None
    __properties: ClassVar[List[str]] = ["em", "name", "surname", "street", "number", "zip", "city", "province", "phoneNumber", "fiscalCode", "vatNumber", "kind", "default", "country", "attributes"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CustomerAddressEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of em
        if self.em:
            _dict['em'] = self.em.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in attributes (dict)
        _field_dict = {}
        if self.attributes:
            for _key in self.attributes:
                if self.attributes[_key]:
                    _field_dict[_key] = self.attributes[_key].to_dict()
            _dict['attributes'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CustomerAddressEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "em": CustomerEMFields.from_dict(obj.get("em")) if obj.get("em") is not None else None,
            "name": obj.get("name"),
            "surname": obj.get("surname"),
            "street": obj.get("street"),
            "number": obj.get("number"),
            "zip": obj.get("zip"),
            "city": obj.get("city"),
            "province": obj.get("province"),
            "phoneNumber": obj.get("phoneNumber"),
            "fiscalCode": obj.get("fiscalCode"),
            "vatNumber": obj.get("vatNumber"),
            "kind": obj.get("kind"),
            "default": obj.get("default"),
            "country": obj.get("country"),
            "attributes": dict(
                (_k, ProtobufAny.from_dict(_v))
                for _k, _v in obj.get("attributes").items()
            )
            if obj.get("attributes") is not None
            else None
        })
        return _obj


