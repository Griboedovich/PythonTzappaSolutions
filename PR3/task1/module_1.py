import re


def main(table):
	name = ""
	email = ""
	number = ""
	digit = 0

	new_table = []

	for column in table:
		phone = column[1]
		name, email = column[0].split(";")
		number = column[3]

		number = number_processing(number)
		phone = phone_processing(phone)
		name = name_processing(name)
		email = email_processing(email)
		
		new_table.append([
			name,
			email,
			phone,
			number
		])
	new_table.sort(key=lambda p: p[0][0])
	transposed_table = transpose_table(new_table)
	return transposed_table


def number_processing(number):
	number = round(float(number), 3)
	number_str = str(number)
	if len(number_str) < 5:
		number_str += "0"*(5-len(number_str))
	return number_str


def phone_processing(phone_number):
	phone_number = phone_number.replace("(", "-")
	phone_number = phone_number.replace(")", "-")
	phone_number = phone_number.replace(" ", "-")

	phone_part = phone_number.split("-")
	phone_number = ""
	phone_number += "("
	phone_number += phone_part[1]
	phone_number += ") "
	phone_number += phone_part[2]
	phone_number += "-"
	phone_number += phone_part[3]
	phone_number += phone_part[4]
	return phone_number


def name_processing(name):
	name_parts = name.split(" ")
	return name_parts[1] + " " + name_parts[0]


def email_processing(email):
	email_parts = email.split("@")
	return email_parts[1]


def transpose_table(table):

	transposed_table = []

	for i in range(len(table[0])):
		transposed_table.append([])
		for j in range(len(table)):
			transposed_table[i].append(table[j][i])
	return transposed_table

