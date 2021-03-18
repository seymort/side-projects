import pathlib
import argparse


def cred_locater(file_path, domain_name):
    file = open(file_path, "r")
    rfile = file.read()
    block = []
    if domain_name in rfile:
        for i in rfile.split("\n" * 2):
            if domain_name in i:
                print(i)
                block.append(i)
        client = input("Enter Client name: ")
        alert = str(input("Enter Alert ID: "))
        write_path = client + alert + ".txt"
        wfile = open(pathlib.Path().absolute() / write_path, "w")
        # write the credentials to the file
        for z in block:
            wfile.write(z)

    else:
        print("False")


# CLI USAGE:

parser = argparse.ArgumentParser()

parser.add_argument("file_path", help="put the txt file path")
parser.add_argument("domain_name", help="put the domain name")
args = parser.parse_args()
cred_locater(args.file_path, args.domain_name)
