package archivosjava;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Camion {

    private String matricula;
    private double capacidad;

    private final GPS gps;

    private final List<Paquete> paquetes;

    private Conductor conductor;

    public Camion(String matricula, double capacidad, String coordenadas) {
        this.matricula = matricula;
        this.capacidad = capacidad;
        this.gps = new GPS(coordenadas);
        this.paquetes = new ArrayList<>();
    }

    public void cargarPaquete(Paquete p) {
        if (p == null) {
            throw new IllegalArgumentException("El paquete no puede ser null");
        }
        if (pesoTotal() + p.getPeso() > capacidad) {
            throw new IllegalStateException("Capacidad superada: no se puede cargar el paquete");
        }
        paquetes.add(p);
    }

    private double pesoTotal() {
        double total = 0;
        for (Paquete p : paquetes) {
            total += p.getPeso();
        }
        return total;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public double getCapacidad() {
        return capacidad;
    }

    public void setCapacidad(double capacidad) {
        this.capacidad = capacidad;
    }

    public GPS getGps() {
        return gps;
    }

    public List<Paquete> getPaquetes() {
        return Collections.unmodifiableList(paquetes);
    }

    public Conductor getConductor() {
        return conductor;
    }

    public void setConductor(Conductor conductor) {
        this.conductor = conductor;
    }
}
