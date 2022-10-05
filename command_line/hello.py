import argparse


parser = argparse.ArgumentParser(description="Process some integers.")

parser.add_argument("fname", type=str, help="Type your name")
parser.add_argument("-o", "--lname", type=str, help="Optional last name")
args = parser.parse_args()
first_name = args.fname
last_name = args.lname if args.lname else ""
print("Hello {0} {1}".format(first_name, last_name))

# convert into executable command
# pyinstaller -F "hello.py"


# it will create 2 folder build and dist


# run
# .\hello "Afsar" -o "Ahmad"

# hello "Afsar"
