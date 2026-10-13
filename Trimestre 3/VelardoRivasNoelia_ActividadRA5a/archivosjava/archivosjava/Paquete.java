package archivosjava;

public class Paquete {

    private String id;
    private String destino;
    private double peso;

    public Paquete(String id, String destino, double peso) {
        this.id = id;
        this.destino = destino;
        this.peso = peso;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getDestino() {
        return destino;
    }

    public void setDestino(String destino) {
        this.destino = destino;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

}
