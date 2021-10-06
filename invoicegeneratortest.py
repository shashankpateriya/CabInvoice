import pytest
from invoicegenerator import Ride, User, InvoiceGenerator

invoice_generator = InvoiceGenerator()


def test_case():
    assert (isinstance(invoice_generator, InvoiceGenerator))

# def test_raises():
#     with pytest.raises(TypeError):
#         assert cab.calculate_fare('s', 's')
