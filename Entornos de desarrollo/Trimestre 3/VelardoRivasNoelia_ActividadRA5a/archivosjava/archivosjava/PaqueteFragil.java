package archivosjava;

public class PaqueteFragil extends Paquete {

    private double seguro;

    public PaqueteFragil(String id, double peso, String destino, double seguro) {
        super(id, destino, peso);
        this.seguro = seguro;
    }

    public double getSeguro() {
        return seguro;
    }

    public void setSeguro(double seguro) {
        this.seguro = seguro;
    }
}
