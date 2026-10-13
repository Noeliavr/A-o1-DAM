public class Coche extends Vehiculo {
    private Motor motor;

    public Coche(String matricula, int caballos) {
        super(matricula);
        this.motor = new Motor(caballos); // Composición fuerte
    }

    @Override
    public void arrancar() {
        System.out.println("Girando llave...");
        this.motor.encender();
    }
    
    // Getter del motor (opcional pero común)
    public Motor getMotor() { return motor; }
}