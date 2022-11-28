import os

# shadow file
# change the current directory
os.chdir('/etc')
# print("Current working directory: {0}".format(os.getcwd()))

if os.geteuid() != 0:
    print("Err. You are not root.")

with open("shadow", "r") as f:
    f.seek(0)  # from the begining of the file
    print("*******************")
    print("SHADOW FILE")
    print("*******************")
    print(f.read())

# other information we want:
cmd = ['ifconfig', 'hostnamectl', 'locale']  # ip, os information, language
for c in cmd:
    os.popen(c,'w')  # write throwgh cmd
    data = os.popen(c).read()  # read from cmd
    print("*******************")
    print(c)
    print("*******************")
    print(data)