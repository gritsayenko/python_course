def  mul_seq(seq, n):
	seq = map(lambda x: x * n, seq)
	return seq


mul_seq(range(3), 4)
mul_seq([0, 1, 2], 4)
mul_seq((1, 2, 3), 4)



