def multiply(n):
	def decorator(ref_func):
		def wrapper(num):
			result = ref_func(num)
			return result * n
		return wrapper
	return decorator

