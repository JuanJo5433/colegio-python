class Aula:
	def __init__(self, codigo_aula, nombre_aula, capacidad_aula):
		self.codigo_aula = codigo_aula
		self.nombre_aula = nombre_aula
		self.capacidad_aula = capacidad_aula

	def get_codigo_aula(self):
		return self.codigo_aula