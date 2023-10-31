from funciones_tp_5 import num_dni, long_word
import pytest

@pytest.mark.parametrize("input_dni, resul",
    [
        ("45140981",True),
        ("1234567",True),
        ("123",False) 
])
def test_num_dni(input_dni,resul):
    assert num_dni(input_dni)==resul

@pytest.mark.parametrize(
        "input_word, result",
        [
            ("hola",4),
            ("caballero",9),
            ("fisio",5)

])
def test_long_word(input_word,result):
    assert long_word(input_word)==result

