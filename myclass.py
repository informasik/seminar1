class Hello:
	def __init__(self):
		print("Today.")	
	
	def ask(self):
		print("How are you?")

	def ans(self):
		print("Fine.")


def main():
	say=Hello()
	say.ask()
	say.ans()

if __name__ == "__main__":
	main()


