from io import IOBase
from typing import Any, Dict, Type, Union, get_args, get_origin

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict, FieldValidationInfo, field_validator

from .scalars import SCALARS_PARSE_FUNCTIONS, SCALARS_SERIALIZE_FUNCTIONS


class UnsetType:
    def __bool__(self) -> bool:
        return False


UNSET = UnsetType()


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        arbitrary_types_allowed=True,
    )

    # pylint: disable=no-self-argument
    @field_validator("*", mode="before")
    def parse_custom_scalars(cls, value: Any, info: FieldValidationInfo) -> Any:
        annotation = cls.model_fields[info.field_name].annotation
        if not annotation:
            return value
        return cls._parse_custom_scalar_value(value, annotation)

    @classmethod
    def _parse_custom_scalar_value(cls, value: Any, type_: Type[Any]) -> Any:
        origin = get_origin(type_)
        args = get_args(type_)
        if origin is list and isinstance(value, list):
            return [cls._parse_custom_scalar_value(item, args[0]) for item in value]

        if origin is Union and type(None) in args:
            sub_type: Any = list(filter(None, args))[0]
            return cls._parse_custom_scalar_value(value, sub_type)

        decode = SCALARS_PARSE_FUNCTIONS.get(type_)
        if value and decode and callable(decode):
            return decode(value)

        return value

    def model_dump(self, **kwargs: Any) -> Dict[str, Any]:
        dict_ = super().model_dump(**kwargs)
        return {key: self._serialize_value(value) for key, value in dict_.items()}

    def _serialize_value(self, value: Any) -> Any:
        serialize = SCALARS_SERIALIZE_FUNCTIONS.get(type(value))
        if serialize and callable(serialize):
            return serialize(value)

        if isinstance(value, list):
            return [self._serialize_value(item) for item in value]

        if isinstance(value, dict):
            return {key: self._serialize_value(val) for key, val in value.items()}

        return value


class Upload:
    def __init__(self, filename: str, content: IOBase, content_type: str):
        self.filename = filename
        self.content = content
        self.content_type = content_type
