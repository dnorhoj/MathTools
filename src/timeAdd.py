from termcolor import colored, cprint
import sys, re

def wrong_format(info=""):
	cprint("\nWrong format!", "red", attrs=["bold"])
	if not info == "":
		cprint(info, "red", attrs=["bold"])
	sys.exit(1)

if __name__ == "__main__":
	inputstr = colored(f"First timestamp", "magenta")+colored("(hh:mm)", "blue")+colored("> ", "green")

	uip = input(inputstr)
	match = re.match(r"([0-9]{1,2}):([0-9]{1,2})$", uip)

	if match:
		cprint("true", "green")
	else:
		wrong_format()