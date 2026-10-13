package com.ejemplo.testing;

public class GestorFacturas {

    private static final double IVA = 1.21;

    public double calcularTotalFactura(ICalculadora calc, double subtotal) {
        return calc.multiplicar(subtotal, IVA);
    }
}

