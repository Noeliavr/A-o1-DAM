
class GestorBiblioteca:
  def __init__(self, sistemaNotificaciones):
    self.sistemaNotificaciones = sistemaNotificaciones
    self.catalogoLibros = []
    self.usuariosRegistrados = []
  def agregar_libro (self,libro):
    self.catalogoLibros.append(libro)
    print(f"{libro.titulo} agregado")
  def registrar_usuario(self, usuario):
    self.usuariosRegistrados.append(usuario)
    print(f"{usuario.nombre} agragado")

  def prestar_libro (self,libro, usuario):
    if libro in self.catalogoLibros and usuario in self.usuariosRegistrados :
      if libro.disponible:
        libro.disponible = False
        usuario.libros_prestados.append(libro)
        self.sistemaNotificaciones.enviar(
        f"{libro.titulo} prestado con exito",usuario.contacto
        )
      else:
        print(f"{libro.titulo} no disponible")
    else:
      print("libro o usuario no encontrado")
      
  def devolver_libro (self, libro, usuario):
    if libro in usuario.libros_prestados:
      libro.disponible = True
      usuario.libros_prestados.remove(libro)
      self.sistemaNotificaciones.enviar(
        f"{libro.titulo} devuelto con exito", usuario.contacto
      )
    else:
      print("No tienes el libro asignado")