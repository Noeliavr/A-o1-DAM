from biblioteca.interfaces.Notificacion import EmailNotificacion, SMSNotificacion
from biblioteca.modelos.Libro import Libro
from biblioteca.modelos.Usuario import Usuario
from biblioteca.servicios.GestorBiblioteca import GestorBiblioteca

if __name__ == "__main__":

  print("=== Sistema de Biblioteca ===")

  notificacion = SMSNotificacion()
  gestor = GestorBiblioteca(notificacion)


  libro1 = Libro("Te","Amo", "mi vida")
  libro2 = Libro("Te", "Amo", "bebe")

  usuario1 = Usuario("U001", "Alfon", "Alfonsemar12@gmail.com")

  gestor.agregar_libro(libro1)
  gestor.agregar_libro(libro2)
  gestor.registrar_usuario(usuario1)

  gestor.prestar_libro(libro1, usuario1)
  gestor.prestar_libro(libro2, usuario1)
  gestor.devolver_libro(libro1, usuario1)
