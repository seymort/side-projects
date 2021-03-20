import pathlib
import argparse
import zipfile
import tempfile
import subprocess
import os

def validate_user_input(usr_input):
    if usr_input == '':
        while usr_input == '':
            usr_input = input('Invalid input.\nPlease fill the necessary fields: ')
        return usr_input
    else:
        return usr_input


def validate_path_existence(path):
    if not zipfile.is_zipfile(path):
        while not zipfile.is_zipfile(path):
            path = input('Invalid path.\nPlease enter path: ')
        return path
    else:
        return path

def cred_locater(zip_path, domain_name, client_name, alert_id):

    with tempfile.TemporaryDirectory() as tmpdirname:
        zf = zipfile.ZipFile(zip_path)
        zf.extractall(tmpdirname)
        for files in os.listdir(tmpdirname):
            if files == "passwords.txt" or files == "Passwords.txt":
                file = open(tmpdirname + r"\%s" % files, "r")
                rfile = file.read()
                block = []
                if domain_name in rfile:
                    for i in rfile.split("\n" * 2):
                        if domain_name in i:
                            print(i)
                            block.append(i)
                file.close()

            write_path = client_name + alert_id + ".txt"
            wfile = open(pathlib.Path().absolute() / write_path, "w")
            # write the credentials to the file
            for z in block:
                wfile.write(z)
            wfile.close()
            os.system("start " + write_path)


# CLI USAGE:
if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("zip_path", help="put the zip file path")
    parser.add_argument("domain_name", help="put the domain name")
    args = parser.parse_args()

    client = input("Enter Client name: ")
    client = validate_user_input(client)
    alert = str(input("Enter Alert ID: "))
    alert = validate_user_input(alert)

    domain_name = validate_user_input(args.domain_name)
    zip_path = validate_path_existence(args.zip_path)

    cred_locater(zip_path, domain_name, client, alert)
