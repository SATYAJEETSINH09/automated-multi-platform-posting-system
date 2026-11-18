
import re
from pydantic import BaseModel, Field, field_validator
from urllib.parse import urlparse


class PostingRequest(BaseModel):

    message: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Message must not exceed 200 characters"
    )

    @field_validator("message")
    @classmethod
    def validate_message(cls, value):

        # Find URLs in message
        urls = re.findall(
            r'https?://[^\s]+',
            value
        )

        # Exactly one URL required
        if len(urls) != 1:
            raise ValueError(
                "Message must contain exactly one CTA link"
            )

        # Validate URL
        parsed_url = urlparse(urls[0])

        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError("Invalid URL")

        if "." not in parsed_url.netloc:
            raise ValueError("Invalid URL domain")

        return value
