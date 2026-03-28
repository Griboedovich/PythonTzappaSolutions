def main(bites):
	fields_dict = {}
	
	bite_row = int(bites, 16)
	
	fields_dict = {
		'C1': hex(bite_row & 15),
		'C2': hex((bite_row >> 4) & 0b11111),
		'C3': hex((bite_row >> 9) & 0b11),
		'C4': hex((bite_row >> 11) & 0b1),
		'C5': hex((bite_row >> 12) & 0b11),
		'C6': hex(bite_row >> 14)
	}

	return fields_dict

