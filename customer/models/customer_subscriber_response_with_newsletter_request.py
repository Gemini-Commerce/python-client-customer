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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from customer.models.customer_create_consent_request import CustomerCreateConsentRequest
from customer.models.customer_em_fields import CustomerEMFields
from customer.models.customer_newsletter_request import CustomerNewsletterRequest
from typing import Optional, Set
from typing_extensions import Self

class CustomerSubscriberResponseWithNewsletterRequest(BaseModel):
    """
    CustomerSubscriberResponseWithNewsletterRequest
    """ # noqa: E501
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    lastname: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    gender: Optional[StrictStr] = None
    birthdate: Optional[datetime] = None
    nationality: Optional[StrictStr] = None
    em: Optional[CustomerEMFields] = None
    preferred_locale: Optional[StrictStr] = Field(default=None, alias="preferredLocale")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    newsletters: Optional[List[CustomerNewsletterRequest]] = None
    consent: Optional[CustomerCreateConsentRequest] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "name", "lastname", "email", "country", "gender", "birthdate", "nationality", "em", "preferredLocale", "createdAt", "updatedAt", "newsletters", "consent"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CustomerSubscriberResponseWithNewsletterRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of em
        if self.em:
            _dict['em'] = self.em.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in newsletters (list)
        _items = []
        if self.newsletters:
            for _item_newsletters in self.newsletters:
                if _item_newsletters:
                    _items.append(_item_newsletters.to_dict())
            _dict['newsletters'] = _items
        # override the default output from pydantic by calling `to_dict()` of consent
        if self.consent:
            _dict['consent'] = self.consent.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomerSubscriberResponseWithNewsletterRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "lastname": obj.get("lastname"),
            "email": obj.get("email"),
            "country": obj.get("country"),
            "gender": obj.get("gender"),
            "birthdate": obj.get("birthdate"),
            "nationality": obj.get("nationality"),
            "em": CustomerEMFields.from_dict(obj["em"]) if obj.get("em") is not None else None,
            "preferredLocale": obj.get("preferredLocale"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "newsletters": [CustomerNewsletterRequest.from_dict(_item) for _item in obj["newsletters"]] if obj.get("newsletters") is not None else None,
            "consent": CustomerCreateConsentRequest.from_dict(obj["consent"]) if obj.get("consent") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


