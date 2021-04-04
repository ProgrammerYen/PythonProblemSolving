def trailing_zeros(n):
	num_count = 0
	num_power = 2
	num_count += n // 5

	while n // 5 ** num_power >= 1:
		num_count += n // 5 ** num_power
		num_power += 1

	return num_count

print(trailing_zeros(9000000))