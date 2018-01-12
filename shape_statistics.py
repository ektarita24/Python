from xyz.supercoders.Shapes.shape import Shape

class ShapeStatistics:
	
	def print_statistics(shape):
		if isinstance(shape,Shape):
			print(shape.area())
			print(shape.perimeter())
		else:
			print("Invalid")
