class IllegalArgumentError(Exception):
	def __init__(self,msg=None):
		if msg is not None:
			super().__init__(msg)
