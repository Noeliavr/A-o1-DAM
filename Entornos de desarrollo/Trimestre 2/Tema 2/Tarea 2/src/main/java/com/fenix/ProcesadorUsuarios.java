package com.fenix;

import java.util.ArrayList;
import java.util.List;

/**
 * Esta clase procesa listas de usuarios. Contiene 'code smells' intencionados.
 */
public class ProcesadorUsuarios {

    /**
     *
     * Creación de las constantes para los números mágicos
     *
     */
    private static final int ROL_INVITADO = 2;
    private static final int ROL_ADMIN = 1;

    /**
     * Método con 'code smells': largo, números mágicos, malos nombres.
     */
    public String procesarLista(List<String> usuarios) {
        String admins = "";
        String invitados = "";
        /**
         * Procesar una lista de usuarios en formato "nombre:rol" y devolver un
         * resumen de admins e invitados.
         */

        for (String u : usuarios) {
            /**
             * Formato "nombre:rol"
             */
            String[] parts = u.split(":");
            if (parts.length == 2) {
                var nombre = parts[0];
                int rol = Integer.parseInt(parts[1]);
                /**
                 * Número Mágico: 1 es Admin
                 */
                if (rol == ROL_ADMIN) {
                    admins = procesarAdmin(admins, nombre);
                } /**
                 * Número Mágico: 2 es Invitado
                 *
                 */
                else if (rol == ROL_INVITADO) {
                    invitados = procesarInvitado(invitados, nombre);
                }
            }
        }
        return "Admins: " + admins + " | Invitados: " + invitados;
    }

    /**
     * Clases privadas para los identificar un método largo y convertirlos en
     * dos métodos privados
     */

    /**
     * @param admins
     * @param nombre
     * @return String
     */
    private String procesarInvitado(String invitados, String nombre) {
        invitados += nombre + ";";
        return invitados;
    }

    private String procesarAdmin(String admins, String nombre) {
        admins += nombre + ";"; // ✅ lógica propia, NO llamar a invitado
        return admins;
    }
}
