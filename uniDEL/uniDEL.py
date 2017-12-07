import os, time, sys, random
# Set up
os.system('clear')
source = open("source.txt", "r").read()
target = open("target.txt", "r").read()
filename = open("filename.txt", "r").read()
# End of setup

os.system('clear')
action = raw_input('[!]>>')

def remove_chars(data, chars):
    new_data = data
    for ch in chars:
        new_data = new_data.replace(ch, '')
    return new_data
def random_list():
    for i in range(5, 12):
        random.randint(111, 1666)


sourcer = source.replace("\n", "")
targetr = target.replace("\n", "")
filenamer = filename.replace("\n", "")
if action=='del -p':
    os.system('clear')
    print('Are you sure you want to delete your file?')
    print('Filename: ', filenamer )
    print('Source: ', sourcer )
    print('Target: ', targetr )
    confirm = raw_input('[y/n]')
else:
    print('\330[1;31;40m Syntax Error: Does nor exist\n')
    print('Type [-h] for help')
    print('Reseting...')
    exit()

if confirm=='y':
    print('Working...')
    os.listdir(sourcer)
    os.chdir(sourcer)
    random_list()
    os.remove(filenamer)
    time.sleep(1)
    print('Done!')
    os.listdir(sourcer)
    time.sleep(3)
if action=='edit -s':
    os.system('clear')
