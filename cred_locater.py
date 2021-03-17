import pathlib


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
        alert = str(input("Enter Alert ID"))
        write_path = client + alert + ".txt"
        wfile = open(pathlib.Path().absolute() / write_path, "w")
        # write the credentials to the file
        for z in block:
            wfile.write(z)

    else:
        print("False")

