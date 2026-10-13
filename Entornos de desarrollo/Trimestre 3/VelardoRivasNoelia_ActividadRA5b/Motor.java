public class Motor {
    private int caballos;
    private boolean encendido;

    public Motor(int caballos) {
        this.caballos = caballos;
        this.encendido = false;
    }

    public void encender() { 
        this.encendido = true;
        System.out.println("Motor arrancado.");
    }

    public int getCaballos() { return caballos; }
    public void setCaballos(int caballos) { this.caballos = caballos; }
    public boolean isEncendido() { return encendido; } // Getter booleano
}