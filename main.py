import subprocess, sys, os
from tqdm import tqdm
import requests

urls = ["https://raw.githubusercontent.com/Crazypersonalph/anicli-downloader/refs/heads/main/initiate.ps1",
        "https://raw.githubusercontent.com/Crazypersonalph/anicli-downloader/refs/heads/main/scoop-install.ps1"]

for i in urls:
    url = i.rsplit('/', 1)[-1]
    response = requests.get(i, stream=True, verify=True)
    with open(url, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

# Initialise install scoop
p = subprocess.Popen(["powershell.exe -ExecutionPolicy RemoteSigned -file", 
              f"{get_script_path()}\\initiate.ps1"], 
              stdout=sys.stdout)
p.communicate()


# Install ani-cli plus deps
p = subprocess.Popen(["powershell.exe -ExecutionPolicy RemoteSigned -file", 
                      f"{get_script_path()}\\scoop-install.ps1"], 
                      stdout=sys.stdout)
p.communicate()

os.remove("initiate.ps1")
os.remove("scoop-install.ps1")

input("Installation complete, by yours truly. Cyah! Press Enter to exit.")