def main(x):
	return func_zero(x)


def func_zero(x):
	if x[0] == 'GAMS':
		return func_z_f_1(x)
	if x[0] == 'ORG':
		return func_z_f_2(x)


def func_z_f_1(x):
	if x[3] == 2020:
		return func_z_f_1_s_1(x)
	if x[3] == 2013:
		return func_z_f_1_s_2(x)


def func_z_f_1_s_1(x):
	if x[2] == 1978:
		return 0
	if x[2] == 2007:
		return 1
	if x[2] == 1983:
		return 2


def func_z_f_1_s_2(x):
	if x[1] == 'TOML':
		return 3
	if x[1] == 'MQL5':
		return 4
	if x[1] == 'HTTP':
		return 5


def func_z_f_2(x):
	if x[2] == 1978:
		return func_z_f_2_s_1(x)
	if x[2] == 2007:
		return func_z_f_2_s_2(x)
	if x[2] == 1983:
		return 11


def func_z_f_2_s_1(x):
	if x[1] == 'TOML':
		return 6
	if x[1] == 'MQL5':
		return 7
	if x[1] == 'HTTP':
		return 8


def func_z_f_2_s_2(x):
	if x[3] == 2020:
		return 9
	if x[3] == 2013:
		return 10

