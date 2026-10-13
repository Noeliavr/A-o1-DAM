package com.ejemplo.testing;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class CalculadoraTest {

    Calculadora calc = new Calculadora();

    // Suma correcta: 2 + 3 = 5
    @Test
    public void testSumar() {
        assertEquals(5.0, calc.sumar(2, 3), "2 + 3 debería ser 5");
    }

    @Test
    public void testRestar() {
        assertEquals(5.0, calc.restar(10, 5));
    }

    // CP-DIV-01: división normal 10 / 2 = 5
    @Test
    public void testDividir_CP_DIV01() {
        assertEquals(5.0, calc.dividir(10, 2), "10 / 2 debería ser 5.0");
    }

    // CP-DIV-02: división normal 5 / 2 = 2.5
    @Test
    public void testDividir_CP_DIV02() {
        assertEquals(2.5, calc.dividir(5, 2), "5 / 2 debería ser 2.5");
    }

// CP-DIV-03: división por cero con double -> devuelve Infinity
    @Test
    public void testDividir_CP_DIV03() {
        assertEquals(Double.POSITIVE_INFINITY, calc.dividir(10, 0), "10 / 0 debería devolver Infinity");
    }

    // CP-DIV-04: división límite 0 / 5 = 0.0
    @Test
    public void testDividir_CP_DIV04() {
        assertEquals(0.0, calc.dividir(0, 5), "0 / 5 debería ser 0.0");
    }
}
