import re


def main(data):

	key_val_pattern = re.compile(
		r"let[ ]*\n*[0-9\-]*[ ]*\n*==>[ ]*\n*'[a-z0-9\_]*';"
	)
	val_pattern = re.compile(r"let[ ]*\n*[0-9\-]*[ ]*\n*==>")
	key_pattern = re.compile(r"'[a-z0-9\_]*'")

	key_val = key_val_pattern.findall(data)

	result_dict = {
		key_pattern.search(row).group()[1:-1]:
		int(val_pattern.search(row).group()[3:-3].strip())
		for row in key_val
	}

	return result_dict

