import string
import random
import argparse

def generate_password(length, include_special, include_numbers):
	chars = string.ascii_letters
	if include_special:
		chars += string.punctuation
	if include_numbers:
		chars += string.digits

	password = ''.join(random.choice(chars) for i in range(length))
	return password

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Password generator")
	parser.add_argument("-l", "--length", type=int, default=16, help="Password length")
	parser.add_argument("-s", "--special", action="store_true", help="Include special characters")
	parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers")
	args = parser.parse_args()

	password = generate_password(args.length, args.special, args.numbers)
	print(password)
