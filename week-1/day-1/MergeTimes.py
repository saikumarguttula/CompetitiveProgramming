def merge_intervals(intervals):
	"""
	A simple algorithm can be used:
	1. Sort the intervals in increasing order
	2. Push the first interval on the stack
	3. Iterate through intervals and for each one compare current interval
	   with the top of the stack and:
	   A. If current interval does not overlap, push on to stack
	   B. If current interval does overlap, merge both intervals in to one
		  and push on to stack
	4. At the end return stack
	"""
	si = sorted(intervals, key=lambda tup: tup[0])
	merged = []

	for tup in si:
		if not merged:
			merged.append(tup)
		else:
			b = merged.pop()
			print(b)
			if b[1] >= tup[0]:
				new_tup = tuple([b[0], tup[1]])
				merged.append(new_tup)
			else:
				merged.append(b)
				merged.append(tup)
	print("========",merged,"========")
	return merged

if __name__ == '__main__':

	l = [(1, 4), (2, 5), (5, 8)]
	print("Original list of ranges: {}".format(l))
	merged_list = merge_intervals(l)
	print("List of ranges after merge_ranges: {}".format(merged_list))
