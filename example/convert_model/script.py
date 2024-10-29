from pydantic import BaseModel, Field
from typing import Optional, Literal
from textwrap import dedent


class ButtonProps(BaseModel):
    """
    Model Description
    with Multi Lines
    """

    label: str = Field(description="Label Description")
    variant: Literal["primary", "secondary", "danger"] = Field(
        default="primary",
        description=dedent("""
            Variant Description.
            This is multiline.
            It is indented, but covered by `textwrap.detent`
            """)
    )
    disabled: Optional[bool] = None
    clickCount: Optional[int] = None
