import pytest
from toolcore.parsers.none_parser import NoneParser
from toolcore.func import BrokenSchemaError


@pytest.fixture
def none_parser():
    return NoneParser(argtype=None, rec_parsers=[])  # type: ignore


def test_returns_none_for_none_input(none_parser):
    assert none_parser.parse_value(None) is None


def test_raises_error_on_non_none_input(none_parser):
    non_none_values = [0, "", [], {}, 1.0, False, True, "string"]
    for value in non_none_values:
        with pytest.raises(BrokenSchemaError):
            none_parser.parse_value(value)
