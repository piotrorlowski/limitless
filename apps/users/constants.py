from typing import Mapping

REQUIRED_FIELD_ERRORS: Mapping[str, str] = {
    "required": "This field is required.",
    "blank": "This field is required.",
    "null": "This field is required.",
}

INVALID_IMAGE_FORMAT: Mapping[str, str] = {
    "invalid_image": "Invalid file extension.",
}
