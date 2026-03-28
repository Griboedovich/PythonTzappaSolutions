from method_1 import *

print(
	main(['GAMS', 'TOML', 1983, 2013]) == 3,
	main(['ORG', 'HTTP', 1978, 2020]) == 8,
	main(['GAMS', 'TOML', 1978, 2020]) == 0,
	main(['ORG', 'TOML', 1983, 2020]) == 11,
	main(['ORG', 'TOML', 2007, 2013]) == 10
)
