from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    """Clase UsuarioManager para sobre escribir los metodos necesarios para la creacion de usuarios nuevos y sus
    permisos"""
    def _create_user(self, email, username, nombres, apellidos, rut, contacto, is_staff, is_superuser, password = None):
        """Retornar un usuario nuevo de la clase Usuario


        Argumentos:
            Todos los argumentos son enviados desde el navegador mediante un formulario.


        Returns:
            Retorna un usuario nuevo.
        """


        if not email:
            raise ValueError('Debe ingresar un correo electrónico')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            rut = rut,
            contacto = contacto,
            password = password,
            is_staff = is_staff,
            is_superuser = is_superuser,
        )

        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, username, nombres, apellidos, rut, contacto, password = None):
        return self._create_user(email, username, nombres, apellidos, rut, contacto, False, False, password)

    def create_staffuser(self, email, username, nombres, apellidos, rut, contacto, password = None):
        return self._create_user(email, username, nombres, apellidos, rut, contacto, True, False, password)

    def create_superuser(self, email, username, nombres, apellidos, rut, contacto, password = None):
        return self._create_user(email, username, nombres, apellidos, rut, contacto, True, True, password)


class Usuario(AbstractBaseUser, PermissionsMixin):
    """Clase para modelar a los usuarios, hereda de AbstractBasaUser para abstraer el model user de django"""
    id = models.AutoField(primary_key = True)
    username = models.CharField('Usuario', max_length = 50, unique = True, blank = False, null = False)
    email = models.EmailField('Correo electrónico', max_length = 100, unique = True, blank = False, null = False)
    nombres = models.CharField('Nombres del usuario', max_length = 100, blank = False, null = False)
    apellidos = models.CharField('Apellidos del usuario', max_length = 100, blank = False, null = False)
    rut = models.CharField('Rut del usuario', max_length = 10, unique = True, blank = False, null = False)
    contacto = models.IntegerField('Contacto del usuario', blank = False, null = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    objects = UsuarioManager()  #   Para usar este manager

    USERNAME_FIELD = 'username' #   o email -> campo representativo del usuario
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos', 'rut', 'contacto']
    

    class Meta:
        verbose_name = 'Usuario'
        # verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
