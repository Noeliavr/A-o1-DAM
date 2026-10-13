package com.ejemplo.testing;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import org.junit.jupiter.api.Test;

public class GestorFacturasTest {

    @Test
    public void testCalcularTotalFacturaConMock() {
        // 1️⃣ Creamos el mock de la interfaz ICalculadora
        ICalculadora calcMock = mock(ICalculadora.class);

        // 2️⃣ Configuramos el comportamiento del mock
        // Si se multiplica 100 * 1.21, devolverá 121
        when(calcMock.multiplicar(100.0, 1.21)).thenReturn(121.0);

        // 3️⃣ Creamos el GestorFacturas y llamamos al método usando el mock
        GestorFacturas gestor = new GestorFacturas();
        double total = gestor.calcularTotalFactura(calcMock, 100.0);

        // 4️⃣ Comprobamos que el resultado sea el esperado
        assertEquals(121.0, total, "El total de la factura debe ser 121.0");
    }
}

