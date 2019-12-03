import sys
import os
import pdb
import random
import string
import ntpath

def randomString(stringLength=10):
    up_letters = string.ascii_uppercase
    all_letters = string.ascii_letters
    return random.choice(up_letters) + \
            ''.join(random.choice(all_letters) for i in range(stringLength))

if len(sys.argv) <= 1:
    print("\n[!] Please provide Grunt raw code to obfuscate!")
    print(f"    Usage:\n\tpython {sys.argv[0]} Grunt.cs")
    sys.exit(1)


filename = os.fspath(sys.argv[1])
files = [f for f in os.listdir('.') if os.path.isfile(f)]

if filename not in files:
    try:
        with open(filename,'r') as myfile:
            filecontent = myfile.read()
        #print(filecontent)    
    except Exception as ex:
        print(f"\n[-] Cannot find file: {filename}\n\
    Ensure that file is either in current directory or full path is specified!")
        sys.exit(1)
else:
    with open(filename) as myfile:
        filecontent = myfile.read()
    #print(filecontent)

obf = filecontent.replace('GruntStager',randomString()).replace('ExecuteStager',randomString()).\
        replace('CovenantURI',randomString()).replace('CovenantCertHash',randomString()).\
        replace('gruntAssembly',randomString()).replace('Stage2',randomString())


head,tail = ntpath.split(filename)
obf_filename = tail.split('.')[0]+'_obfuscated.cs'
obf_filepath = os.path.join(os.getcwd(),obf_filename)

with open(obf_filepath,'w') as myfile:
        myfile.write(obf)

print(f"\n[+] Obfuscated code is written to:\n    {obf_filepath}")
