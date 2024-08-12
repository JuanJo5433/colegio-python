class Estudiante:
	def __init__(self, codigo, nombre, apellido):
		self.__codigo = codigo
		self.__nombre = nombre
		self.__apellido = apellido

	def get_codigo(self):
		return self.__codigo

	def get_nombre(self):
		return self.__nombre

	def get_apellido(self):
		return self.__apellido

	def visualizar_estudiante(self):
		print("Nombre: %s" %(self.__nombre))
		print("Apellidos: %s" %(self.__apellido))
		print("Codigo del estudiante: %s" %(self.__codigo))