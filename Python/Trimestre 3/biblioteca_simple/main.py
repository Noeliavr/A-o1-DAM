from abc import ABC, abstractmethod

# ===== MODELOS =====
class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

class Usuario:
    def __init__(self, id_usuario, nombre, contacto):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.contacto = contacto
        self.libros_prestados = []

# ===== INTERFACES =====
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje, destinatario):
        pass

class EmailNotificacion(Notificacion):
    def enviar(self, mensaje, destinatario):
        print(f"Enviando EMAIL a {destinatario}: {mensaje}")

class SMSNotificacion(Notificacion):
    def enviar(self, mensaje, destinatario):
        print(f"Enviando SMS a {destinatario}: {mensaje}")

# ===== SERVICIO =====
class GestorBiblioteca:
    def __init__(self, sistema_notificacion):
        self.notificador = sistema_notificacion
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, libro, usuario):
        if libro.disponible:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            self.notificador.enviar(
                f"Has prestado el libro '{libro.titulo}'",
                usuario.contacto
            )
        else:
            print("El libro no está disponible")

    def devolver_libro(self, libro, usuario):
        if libro in usuario.libros_prestados:
            libro.disponible = True
            usuario.libros_prestados.remove(libro)
            self.notificador.enviar(
                f"Has devuelto el libro '{libro.titulo}'",
                usuario.contacto
            )

# ===== MAIN =====
if __name__ == "__main__":
    #notificacion = EmailNotificacion()
    notificacion = SMSNotificacion()
    gestor = GestorBiblioteca(notificacion)

    libro1 = Libro(1, "1984", "George Orwell")
    usuario1 = Usuario(1, "Juan", "juan@email.com")

    gestor.agregar_libro(libro1)
    gestor.registrar_usuario(usuario1)

    gestor.prestar_libro(libro1, usuario1)
    gestor.prestar_libro(libro1, usuario1)  # falla
    gestor.devolver_libro(libro1, usuario1)
