import pytest
from invoicegenerator import CabInvoice


def test_method():
    expected_total_fare = 25
    assert expected_total_fare == CabInvoice().calculate_fare(2, 5)


@pytest.mark.xfail
def test_method1():
    expected_total_fare = 35
    assert expected_total_fare == CabInvoice().calculate_fare(2, 5)
