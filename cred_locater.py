yotam haia po
import pathlib
import argparse
import zipfile
import tempfile
import subprocess
import os
from gooey import Gooey, GooeyParser

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

    file_exists = False
    with tempfile.TemporaryDirectory() as tmpdirname:
        block = []
        zf = zipfile.ZipFile(zip_path)
        zf.extractall(tmpdirname)
        for files in os.listdir(tmpdirname):
            if files == "passwords.txt" or files == "Passwords.txt" or files == "PasswordsList.txt":
                file_exists = True
                file = open(tmpdirname + r"\%s" % files, "r")
                rfile = file.read()
                if domain_name in rfile:
                    for i in rfile.split("\n" * 2):
                        if domain_name in i:
                            print(i)
                            block.append(i + '\n' * 2)
                file.close()
                break

        if file_exists == False:
            print("Did not find password file in the ZIP folder, please check the ZIP manually")
            return "Did not find password file in the ZIP folder, please check the ZIP manually"

        write_path = client_name + alert_id + ".txt"
        wfile = open(pathlib.Path().absolute() / write_path, "w")
            # write the credentials to the file
        for z in block:
            wfile.write(z)
        wfile.close()
        os.system("start " + write_path)




@Gooey()
def main():
    parser = GooeyParser(description="A Tool That Was Created Specially For the Tier1 Team To Locate Stolen Credentials in Zip Files")

    parser.add_argument("zip_path", help="put the zip file path", widget= 'FileChooser')
    parser.add_argument("domain_name", help="put the domain name")
    parser.add_argument("client", help="Enter Client name")
    parser.add_argument("alert", help="Enter Alert ID")
    args = parser.parse_args()


    domain_name = validate_user_input(args.domain_name)
    zip_path = validate_path_existence(args.zip_path)
    client = args.client
    alert = args.alert

    cred_locater(zip_path, domain_name, client, alert)

if __name__ == '__main__':
    main()

