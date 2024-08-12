from os import system
from estudiante import Estudiante
from colegio import Colegio
from aula import Aula
from fecha import Fecha
from asistencia import Asistencia

class Menu:
		
	def __init__(self):
		self.colegio = Colegio()

	def listar_estudiantes(self):
		system("cls")
		self.colegio.cuadro_para_mensaje("LISTAR ESTUDIANTES")
		for estudiante in self.colegio.get_estudiantes():
			print("codigo: %s" %(estudiante.get_codigo()))
			print("nombre: %s" %(estudiante.get_nombre()))
			print("apellido: %s" %(estudiante.get_apellido()))
			print("____________________________________________")
		input("Presiona Enter para continuar...")
			

	def listar_aulas(self):
		system("cls")
		self.colegio.cuadro_para_mensaje("LISTAR AULAS")
		for aula in self.colegio.get_aulas():
			print("codigo: %s" %(aula.codigo_aula))
			print("nombre: %s" %(aula.nombre_aula))
			print("Capacidad: %s" %(aula.capacidad_aula))
			print("____________________________________________")
		input("Presiona Enter para continuar...")

	def listar_asistencias(self):
		system("cls")
		self.colegio.cuadro_para_mensaje("LISTAR ASISTENCIAS")
		for asistencia in self.colegio.get_asistencias():
			print("____________________________________________")
			asistencia.visualizar_asistencia()
			print("____________________________________________")
		input("Presiona ENTER para continuar...")

	def listar_asistencia_aula(self):
		system("cls")
		self.colegio.cuadro_para_mensaje("LISTAR ASISTENCIAS DE LA AULA")

		codigo_aula = input("Ingrese el codigo del aula: ")
		pos_aula = self.colegio.buscar_aula(codigo_aula)

		if pos_aula != -1:
			for asistencia in self.colegio.get_asistencia_aula(codigo_aula):
				print("____________________________________________")
				asistencia.visualizar_asistencia()
				print("____________________________________________")
			input("Presiona ENTER para continuar...")

	def listar_asistencia_aula_estudiante(self):
		system("cls")
		self.colegio.cuadro_para_mensaje("LISTA ASISTENCIAS DEL ESTUDIANTE")

		codigo_estudiante = input("Ingrese el codigo del estudiante: ")
		pos_estudiante = self.colegio.buscar_estudiante(codigo_estudiante)

		if pos_estudiante != -1:
			cont = 0
			for asistencia in self.colegio.get_asistencia_estudiante(codigo_estudiante):
				if cont == 0:
					print("Estudiante:", asistencia.buscar_nombre_estudiante(codigo_estudiante), asistencia.buscar_apellido_estudiante(codigo_estudiante))
					cont += 1
				print("____________________________________________")
				asistencia.visualizar_asistencia_estudiante()
				print("____________________________________________")
			input("Presiona ENTER para continuar...")				


	def crear_estudiante(self):
		system("cls")
		self.colegio.cuadro_para_mensaje("CREAR ESTUDIANTE")
		codigo = input("Ingrese el codigo del estudiante: ")
		nombre = input("Ingrese el nombre completo del estudiante: ")
		apellido = input("Ingrese el apellido completo del estudiante: ")

		estudiante = Estudiante(codigo, nombre, apellido)
		
		if self.colegio.adicionar_estudiante(estudiante):
			self.colegio.cuadro_para_alerta(" Info - El estudiante se creó correctamente ", "info")
	
		else:
			print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("   Error - El estudiante ya existe en el sistema   ")
			print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
			input("Presiona ENTER para continuar...")
			self.colegio.cuadro_para_alerta(" Error - El estudiante ya existe en el sistema  ", "error")
			

	def crear_aula(self):
		system("cls")
		self.colegio.cuadro_para_mensaje("CREAR AULA")
		capacidad_aula = input("Ingrese la capacidad del aula: ")
		nombre_aula = input("Ingrese el nombre del aula: ")
		codigo_aula = input("Ingrese el codigo del aula: ")
		aula = Aula(codigo_aula, nombre_aula, capacidad_aula)

		if self.colegio.adicionar_aula(aula):
			print("++++++++++++++++++++++++++++++++++++++++++")
			print("   Info - La aula se creó correctamente   ")
			print("++++++++++++++++++++++++++++++++++++++++++")
			input("Presiona ENTER para continuar...")
		else:
			print("+++++++++++++++++++++++++++++++++++++++++++++")
			print("   Error - La aula ya existe en el sistema   ")
			print("+++++++++++++++++++++++++++++++++++++++++++++")
			input("Presiona ENTER para continuar...")

	def crer_asistencia_aula(self):
		system("cls")
		self.colegio.cuadro_para_mensaje("CREAR ASISTENCIA AULA")
		codigo_aula = input("Ingrese el codigo del aula: ")
		pos_aula  = self.colegio.buscar_aula(codigo_aula)

		if pos_aula != -1:
			dia = int(input("Ingrese el dia: "))
			mes = int(input("Ingrese el mes: "))
			anio = int(input("Ingrese el año: "))
			fecha = Fecha(anio, mes, dia)

			codigo_asistencia = int(input("Ingrese el codigo de la asistencia: "))

			asistencia_aula = Asistencia(fecha, self.colegio.get_aula(pos_aula), codigo_asistencia)

			while True:
				print("|-----------------------------------------|")
				print("|           ASISTENCIA ESTUDIANTE         |")
				print("|-----------------------------------------|")
				print("|1 = Ingresar la asistencia del estudiante|")
				print("|2 = Salir                                |")
				print("|-----------------------------------------|")
				op = int(input("Ingrese una opcion: "))
				print("-------------------------------------------")

				if op == 1:
					codigo_estudiante = input("Ingrese el codigo del estudiante: ")
					pos_estudiante = self.colegio.buscar_estudiante(codigo_estudiante)

					if pos_estudiante != -1:
						asistencia_aula.adicionar_estudiante(self.colegio.get_estudiante(pos_estudiante))

					else:
						print("+++++++++++++++++++++++++++++++++++++")
						print("   Error - El estudiante no existe   ")
						print("+++++++++++++++++++++++++++++++++++++")
						input("Presiona ENTER para continuar...")
				elif op == 2:
					break
				else:
					print("+++++++++++++++++++++++++++++++")
					print("   Error - Opcion no valida.   ")
					print("+++++++++++++++++++++++++++++++")
					input("Presiona ENTER para continuar...")

			self.colegio.adicionar_asistencia(asistencia_aula)

		else:
			print("+++++++++++++++++++++++++++++++")
			print("   Error - El aula no existe   ")
			print("+++++++++++++++++++++++++++++++")
			input("Presiona ENTER para continuar...")




	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("|----------------------------------------------|")
			print("|                    COLEGIO                   |")
			print("|----------------------------------------------|")
			print("|                 MENU PRINCIPAL               |")
			print("|----------------------------------------------|")
			print("|Opciones                                      |")
			print("|1 = Crear Estudiante                          |")
			print("|2 = Crear Aula                                |")
			print("|3 = Crear Asistencia Aula                     |")
			print("|4 = Listar Estudiantes                        |")
			print("|5 = Listar Aulas                              |")
			print("|6 = Listar Asistencias                        |")
			print("|7 = Listar Asistencias por Aula               |")
			print("|8 = Listar Asistencias al Aula del Estudiante |")
			print("|0 = Salir del sistema                         |")
			print("|----------------------------------------------|")

			try:
				op = int(input("Ingrese una opcion: "))

				if op == 0:
					print("Has salido del sistema")
					break
				elif op == 1:
					self.crear_estudiante()
				elif op == 2:
					self.crear_aula()
				elif op == 3:
					self.crer_asistencia_aula()
				elif op == 4:
					self.listar_estudiantes()
				elif op == 5:
					self.listar_aulas()
				elif op == 6:
					self.listar_asistencias()
				elif op == 7:
					self.listar_asistencia_aula()
				elif op == 8:
					self.listar_asistencia_aula_estudiante()

				else:
					print("+++++++++++++++++++++++++++++++")
					print("   Error - Opcion no valida.   ")
					print("+++++++++++++++++++++++++++++++")
					input("Presiona ENTER para continuar...")

				
			except ValueError:
				print("+++++++++++++++++++++++++++++++++++++")
				print("   Error - El dato debe ser entero   ")
				print("+++++++++++++++++++++++++++++++++++++")
				input("Presiona ENTER para continuar...")

if __name__ == '__main__':
	menu = Menu()
	menu.mostrar_menu_principal()
