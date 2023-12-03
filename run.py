import os, sys
os.system("git pull")
try:
    __import__("BRUTE").Login()
except Exception as e:
    exit(str(e))
 
