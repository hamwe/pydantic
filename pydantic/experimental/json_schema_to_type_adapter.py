"""Experimental support for building a `TypeAdapter` from a JSON Schema."""

from typing import Any

from pydantic import TypeAdapter


def type_adapter(schema: dict[str, Any]) -> TypeAdapter:
    """Build a `TypeAdapter` from a JSON Schema."""
    if schema == {'type': 'integer'}:
        return TypeAdapter(int)
    raise NotImplementedError(f'Unsupported JSON schema: {schema!r}')
