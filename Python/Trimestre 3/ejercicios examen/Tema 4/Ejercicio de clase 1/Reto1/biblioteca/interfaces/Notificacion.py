from abc import ABC, abstractmethod

class notificacion (ABC):
  @abstractmethod
  def enviar(mensaje, destinatario):
    pass

class EmailNotificacion(notificacion):
  def enviar(self, mensaje, destinatario):
    print(f"Enviando mensaje {mensaje} a {destinatario}")
class SMSNotificacion(notificacion):
  def enviar(self,mensaje, destinatario):
    print(f"Enviando SMS {mensaje} a {destinatario}")