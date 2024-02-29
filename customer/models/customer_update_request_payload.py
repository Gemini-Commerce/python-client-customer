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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from customer.models.customer_address_entity import CustomerAddressEntity
from customer.models.customer_create_consent_request import CustomerCreateConsentRequest
from customer.models.customer_em_fields import CustomerEMFields
from customer.models.customer_newsletter_request import CustomerNewsletterRequest
from customer.models.customer_password import CustomerPassword
from customer.models.protobuf_any import ProtobufAny
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomerUpdateRequestPayload(BaseModel):
    """
    CustomerUpdateRequestPayload
    """ # noqa: E501
    em: Optional[CustomerEMFields] = None
    name: Optional[StrictStr] = None
    surname: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    birthdate: Optional[datetime] = None
    gender: Optional[StrictStr] = None
    enabled: Optional[StrictBool] = None
    source: Optional[StrictStr] = None
    addresses: Optional[List[CustomerAddressEntity]] = None
    default_billing_address_id: Optional[StrictStr] = Field(default=None, alias="defaultBillingAddressId")
    default_shipping_address_id: Optional[StrictStr] = Field(default=None, alias="defaultShippingAddressId")
    phone_number: Optional[StrictStr] = Field(default=None, alias="phoneNumber")
    nationality: Optional[StrictStr] = None
    groups: Optional[List[StrictStr]] = None
    deleted: Optional[StrictBool] = None
    newsletters: Optional[List[CustomerNewsletterRequest]] = None
    attributes: Optional[Dict[str, ProtobufAny]] = None
    migrated_password: Optional[CustomerPassword] = Field(default=None, alias="migratedPassword")
    preferred_locale: Optional[StrictStr] = Field(default=None, alias="preferredLocale")
    tax_code: Optional[StrictStr] = Field(default=None, alias="taxCode")
    certified_email: Optional[StrictStr] = Field(default=None, alias="certifiedEmail")
    sdi_code: Optional[StrictStr] = Field(default=None, alias="sdiCode")
    fiscal_code: Optional[StrictStr] = Field(default=None, alias="fiscalCode")
    company_name: Optional[StrictStr] = Field(default=None, alias="companyName")
    additional_info: Optional[Dict[str, Any]] = Field(default=None, alias="additionalInfo")
    market: Optional[StrictStr] = None
    external_ids: Optional[Dict[str, StrictStr]] = Field(default=None, alias="externalIds")
    consent: Optional[CustomerCreateConsentRequest] = None
    __properties: ClassVar[List[str]] = ["em", "name", "surname", "email", "birthdate", "gender", "enabled", "source", "addresses", "defaultBillingAddressId", "defaultShippingAddressId", "phoneNumber", "nationality", "groups", "deleted", "newsletters", "attributes", "migratedPassword", "preferredLocale", "taxCode", "certifiedEmail", "sdiCode", "fiscalCode", "companyName", "additionalInfo", "market", "externalIds", "consent"]

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
        """Create an instance of CustomerUpdateRequestPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in addresses (list)
        _items = []
        if self.addresses:
            for _item in self.addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in newsletters (list)
        _items = []
        if self.newsletters:
            for _item in self.newsletters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['newsletters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in attributes (dict)
        _field_dict = {}
        if self.attributes:
            for _key in self.attributes:
                if self.attributes[_key]:
                    _field_dict[_key] = self.attributes[_key].to_dict()
            _dict['attributes'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of migrated_password
        if self.migrated_password:
            _dict['migratedPassword'] = self.migrated_password.to_dict()
        # override the default output from pydantic by calling `to_dict()` of consent
        if self.consent:
            _dict['consent'] = self.consent.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CustomerUpdateRequestPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "em": CustomerEMFields.from_dict(obj.get("em")) if obj.get("em") is not None else None,
            "name": obj.get("name"),
            "surname": obj.get("surname"),
            "email": obj.get("email"),
            "birthdate": obj.get("birthdate"),
            "gender": obj.get("gender"),
            "enabled": obj.get("enabled"),
            "source": obj.get("source"),
            "addresses": [CustomerAddressEntity.from_dict(_item) for _item in obj.get("addresses")] if obj.get("addresses") is not None else None,
            "defaultBillingAddressId": obj.get("defaultBillingAddressId"),
            "defaultShippingAddressId": obj.get("defaultShippingAddressId"),
            "phoneNumber": obj.get("phoneNumber"),
            "nationality": obj.get("nationality"),
            "groups": obj.get("groups"),
            "deleted": obj.get("deleted"),
            "newsletters": [CustomerNewsletterRequest.from_dict(_item) for _item in obj.get("newsletters")] if obj.get("newsletters") is not None else None,
            "attributes": dict(
                (_k, ProtobufAny.from_dict(_v))
                for _k, _v in obj.get("attributes").items()
            )
            if obj.get("attributes") is not None
            else None,
            "migratedPassword": CustomerPassword.from_dict(obj.get("migratedPassword")) if obj.get("migratedPassword") is not None else None,
            "preferredLocale": obj.get("preferredLocale"),
            "taxCode": obj.get("taxCode"),
            "certifiedEmail": obj.get("certifiedEmail"),
            "sdiCode": obj.get("sdiCode"),
            "fiscalCode": obj.get("fiscalCode"),
            "companyName": obj.get("companyName"),
            "additionalInfo": obj.get("additionalInfo"),
            "market": obj.get("market"),
            "externalIds": obj.get("externalIds"),
            "consent": CustomerCreateConsentRequest.from_dict(obj.get("consent")) if obj.get("consent") is not None else None
        })
        return _obj


