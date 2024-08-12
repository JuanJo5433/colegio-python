from fecha import Fecha
from estudiante import Estudiante
from aula import Aula


class Asistencia:
	def __init__(self, fecha, aula, codigo):
		self.__codigo = codigo
		self.__fecha = fecha
		self.__aula = aula
		self.__estudiantes = []

	def get_codigo(self):
		return self.__codigo

	def get_fecha(self):
		return self.__fecha

	def get_aula(self):
		return self.__aula

	def get_estudiantes(self):
		return self.__estudiantes

	def buscar_id_estudiante(self, codigo_estudiante):
		for i in range(len(self.__estudiantes)):
			if self.__estudiantes[i].get_codigo() == codigo_estudiante:
				return codigo_estudiante

	def buscar_nombre_estudiante(self, codigo_estudiante):
		for i in range(len(self.__estudiantes)):
			if self.__estudiantes[i].get_codigo() == codigo_estudiante:
				for estudiante in self.__estudiantes:
					nombre = estudiante.get_nombre()
				return nombre

	def buscar_apellido_estudiante(self, codigo_estudiante):
		for i in range(len(self.__estudiantes)):
			if self.__estudiantes[i].get_codigo() == codigo_estudiante:
				for estudiante in self.__estudiantes:
					apellido = estudiante.get_apellido()
				return apellido
	

	def buscar_estudiante(self, estudiante):
		for item_estudiante in self.__estudiantes:
			if item_estudiante.get_codigo() == estudiante.get_codigo():
				return True
		return -1

	def adicionar_estudiante(self, estudiante):
		if self.buscar_estudiante(estudiante) == -1:
			self.__estudiantes.append(estudiante)
			return True
		return False

	def visualizar_asistencia(self):
		print("Codigo asistencia: %s" % (self.__codigo))
		self.__fecha.visualizar_fecha()
		print("Aula: %s" % (self.__aula.nombre_aula))
		
		for estudiante in self.__estudiantes:
			print("_____________________________")
			estudiante.visualizar_estudiante()

	def visualizar_asistencia_estudiante(self):
		print("Codigo asistencia: %s" % (self.__codigo))
		self.__fecha.visualizar_fecha()
		print("Aula: %s" % (self.__aula.nombre_aula))
		
