package archivosjava;

public class PaqueteUrgente extends Paquete {

    private int prioridad;

    public PaqueteUrgente(String id, double peso, String destino, int prioridad) {
        super(id, destino, peso);
        this.prioridad = prioridad;
    }

    public int getPrioridad() {
        return prioridad;
    }

    public void setPrioridad(int prioridad) {
        this.prioridad = prioridad;
    }
}
