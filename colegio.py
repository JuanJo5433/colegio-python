from estudiante import Estudiante
from aula import Aula
from asistencia import Asistencia


class Colegio:

	def __init__(self):
		self.__estudiantes = []
		self.__aulas = []
		self.__asistencias = []

	def get_aula(self, posicion):
		return self.__aulas[posicion]

	def get_aulas(self):
		return self.__aulas

	def get_estudiante(self, posicion):
		return self.__estudiantes[posicion]

	def get_estudiantes(self):
		return self.__estudiantes

	def get_asistencias(self):
		return self.__asistencias

	def get_asistencia_aula(self, codigo_aula):
		asistencia_aula = []
		for asistencia in self.__asistencias:
			if asistencia.get_aula().codigo_aula == codigo_aula:
				asistencia_aula.append(asistencia)
		return asistencia_aula

	def get_asistencia_estudiante(self, codigo_estudiante):
		asistencia_estudiante = []
		pos = self.buscar_estudiante(codigo_estudiante)
		for asistencia in self.__asistencias:
			if asistencia.buscar_id_estudiante(codigo_estudiante) == codigo_estudiante:
				asistencia_estudiante.append(asistencia)
		return asistencia_estudiante


	def buscar_estudiante(self, codigo_estudiante):
		for i in range(len(self.__estudiantes)):
			if self.__estudiantes[i].get_codigo() == codigo_estudiante:
				return i
		return -1


	def adicionar_estudiante(self, estudiante):
		if self.buscar_estudiante(estudiante.get_codigo()) == -1:
			self.__estudiantes.append(estudiante)
			return True
		return False

	def buscar_aula(self, codigo_aula):
		for i in range(len(self.__aulas)):
			if self.__aulas[i].codigo_aula == codigo_aula:
				return i
		return -1

	def adicionar_aula(self, aula):
		if self.buscar_aula(aula.codigo_aula) == -1:
			self.__aulas.append(aula)
			return True
		return False

	def buscar_asistencia(self, asistencia):
		for item_asistencia in self.__asistencias:
			if item_asistencia.get_codigo() == asistencia.get_codigo():
				return True
		return -1

	def adicionar_asistencia(self, asistencia):
		if self.buscar_asistencia(asistencia) == -1:
			self.__asistencias.append(asistencia)
			return True
		return False

	def cuadro_para_mensaje(self, texto):
		longitud = len(texto)
		borde = '|' + '-' * (longitud + 20) + '|'
		contenido = '|          ' + texto + '          |'

		print(borde)
		print(contenido)
		print(borde)

	def cuadro_para_alerta(self, alerta, tipo):
		reiniciar = '\033[0m'
		rojo = '\033[91m'
		verde = '\033[92m'
		if tipo == 'info':
			longitud = len(alerta)
			borde = '+' * (longitud + 10) + '+'
			contenido = verde + '     ' + alerta + '     ' + reiniciar 

			print(borde)
			print(contenido)
			print(borde)
			input("Presiona ENTER para continuar...")
		if tipo == 'error':
			longitud = len(alerta)
			borde = '+' * (longitud + 10) + '+'
			contenido = rojo + '     ' + alerta + '     ' + reiniciar 

			print(borde)
			print(contenido)
			print(borde)
			input("Presiona ENTER para continuar...")
