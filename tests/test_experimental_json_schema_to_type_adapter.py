import pytest

from pydantic import TypeAdapter
from pydantic.experimental.json_schema_to_type_adapter import type_adapter


@pytest.mark.parametrize('tp', [int])
def test_round_trip(tp: type) -> None:
    schema = TypeAdapter(tp).json_schema()
    assert type_adapter(schema).json_schema() == schema
