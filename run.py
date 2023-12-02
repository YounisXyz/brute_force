import os, sys
os.system("git pull")
try:
    __import__("run").Login()
except Exception as e:
    exit(str(e))
 
