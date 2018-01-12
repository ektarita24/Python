from salaried_individual import SalariedIndividual

class SalaryCalculator:
	
	def calc_salary(salaried_individual):
		if isinstance(salaried_individual,SalariedIndividual):
			n = salaried_individual.get_no_of_days()
			c = salaried_individual.get_cost_per_day()
			tax = salaried_individual.get_tax()
			return (n*c)-tax
		else:
			print("Cannot calculate salary")

