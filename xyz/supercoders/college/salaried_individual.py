from abc import ABC,abstractmethod

class SalariedIndividual(ABC):
	
	@abstractmethod	
	def get_no_of_days(self):
		pass
	
	@abstractmethod	
	def get_cost_per_day(self):
		pass
	
	@abstractmethod	
	def get_tax(self):
		pass
