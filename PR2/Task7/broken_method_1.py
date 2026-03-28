def main(x):
	match x:
		case ['GAMS', x, 1978, 2020]:
			return 0
		case ['GAMS', x, 2007, 2020]:
			return 1
		case ['GAMS', x, 1983, 2020]:
			return 2
		case ['GAMS', 'TOML', y, 2013]:
			return 3
		case ['GAMS', 'MQL5', y, 2013]:
			return 4
		case ['GAMS', 'HTTP', y, 2013]:
			return 5
		case ['ORG', 'TOML', 1978, z]:
			return 6
		case ['ORG', 'MQL5', 1978, z]:
			return 7
		case ['ORG', 'HTTP', 1978, z]:
			return 8
		case ['ORG', x, 2007, 2020]:
			return 9
		case ['ORG', x, 2007, 2013]:
			return 10
		case ['ORG', x, 1983, z]:
			return 11

