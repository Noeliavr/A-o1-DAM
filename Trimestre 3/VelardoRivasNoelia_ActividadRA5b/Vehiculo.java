public abstract class Vehiculo {
    protected String matricula;

    public Vehiculo(String matricula) {
        this.matricula = matricula;
    }

    public abstract void arrancar();

    public String getMatricula() { return matricula; }
    public void setMatricula(String matricula) { this.matricula = matricula; }
}