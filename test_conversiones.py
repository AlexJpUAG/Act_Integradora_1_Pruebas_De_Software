import logging
import pytest

import conversiones


@pytest.fixture
def system():
    return conversiones


# CP1 - Conversión de Celsius a Fahrenheit
@pytest.mark.unit
@pytest.mark.functional
@pytest.mark.temperature
@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0, 32),
        (25, 77),
        (100, 212)
    ]
)
def test_cp1_celsius_a_fahrenheit(system, celsius, expected):

    logging.info(
        f"CP1 - Celsius a Fahrenheit: entrada={celsius}, esperado={expected}"
    )

    resultado = system.celsius_a_fahrenheit(celsius)

    logging.info(f"Resultado obtenido: {resultado}")

    assert resultado == pytest.approx(expected)


# CP2 - Conversión de kilómetros a millas
@pytest.mark.unit
@pytest.mark.functional
@pytest.mark.distance
@pytest.mark.parametrize(
    "kilometros, expected",
    [
        (1, 0.621371),
        (10, 6.21371),
        (100, 62.1371)
    ]
)
def test_cp2_kilometros_a_millas(system, kilometros, expected):

    logging.info(
        f"CP2 - Kilómetros a millas: entrada={kilometros}, esperado={expected}"
    )

    resultado = system.kilometros_a_millas(kilometros)

    logging.info(f"Resultado obtenido: {resultado}")

    assert resultado == pytest.approx(expected)


# CP3 - Conversión de pesos mexicanos a dólares
@pytest.mark.unit
@pytest.mark.functional
@pytest.mark.currency
@pytest.mark.parametrize(
    "pesos, expected",
    [
        (18.50, 1),
        (185, 10),
        (1850, 100)
    ]
)
def test_cp3_pesos_a_dolares(system, pesos, expected):

    logging.info(
        f"CP3 - Pesos a dólares: entrada={pesos}, esperado={expected}"
    )

    resultado = system.pesos_a_dolares(pesos)

    logging.info(f"Resultado obtenido: {resultado}")

    assert resultado == pytest.approx(expected)


# CP4 - Precisión de al menos dos decimales
@pytest.mark.unit
@pytest.mark.nonfunctional
@pytest.mark.precision
@pytest.mark.parametrize(
    "valor",
    [
        25,
        10,
        18.50
    ]
)
def test_cp4_precision_dos_decimales(system, valor):

    resultado = system.celsius_a_fahrenheit(valor)

    resultado_formateado = f"{resultado:.2f}"

    logging.info(
        f"CP4 - Precisión: resultado={resultado_formateado}"
    )

    assert len(resultado_formateado.split(".")[1]) >= 2


# CP5 - La entrada no se modifica durante la conversión
@pytest.mark.unit
@pytest.mark.nonfunctional
@pytest.mark.input_integrity
@pytest.mark.parametrize(
    "valor",
    [
        0,
        25,
        100
    ]
)
def test_cp5_entrada_no_se_modifica(system, valor):

    valor_original = valor

    resultado = system.celsius_a_fahrenheit(valor)

    logging.info(
        f"CP5 - Integridad de entrada: original={valor_original}, "
        f"entrada_despues={valor}"
    )

    assert valor == valor_original
    assert resultado != valor