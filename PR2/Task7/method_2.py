def main(x):
	tree_dict = {
		'GAMS': (3, {
			2020: (2, {
				1978: 0,
				2007: 1,
				1983: 2
			}),
			2013: (1, {
				'TOML': 3,
				'MQL5': 4,
				'HTTP': 5
			})
		}),
		'ORG': (2, {
			1978: (1, {
				'TOML': 6,
				'MQL5': 7,
				'HTTP': 8
			}),
			2007: (3, {
				2020: 9,
				2013: 10
			}),
			1983: (2, {
				1983: 11
			})
		})
	}

	index, next_dict = tree_dict[x[0]]
	index, next_dict = next_dict[x[index]]
	return next_dict[x[index]]

