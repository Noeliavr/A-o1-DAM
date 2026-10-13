public class Mecanico {
    private String nombre;

    public Mecanico(String nombre) {
        this.nombre = nombre;
    }

    public void reparar(Coche c) {
        System.out.println("Revisando: " + c.getMatricula());
        c.arrancar();
    }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
}