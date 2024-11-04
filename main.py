import subprocess, sys, os
from tqdm import tqdm
import requests

from pathlib import Path
home = Path.home()

urls = ["https://raw.githubusercontent.com/Crazypersonalph/anicli-downloader/refs/heads/main/initiate.ps1",
        "https://raw.githubusercontent.com/Crazypersonalph/anicli-downloader/refs/heads/main/scoop-install.ps1"]

# Download files with progress bar
for i in urls:
    url = i.rsplit('/', 1)[-1]
    response = requests.get(i, stream=True, verify=True)
    with open(url, "wb") as handle:
        for data in tqdm(response.iter_content(chunk_size=1024), desc=f"Downloading {url}"):
            handle.write(data)

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

# Initialize install scoop
p = subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "RemoteSigned", "-File", 
                      os.path.join(get_script_path(), "initiate.ps1")], 
                     stdout=sys.stdout, shell=True)
p.communicate()

# Install ani-cli plus dependencies
p = subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "RemoteSigned", "-File", 
                      os.path.join(get_script_path(), "scoop-install.ps1")], 
                     stdout=sys.stdout, shell=True)
p.communicate()

# Clean up downloaded files
os.remove("initiate.ps1")
os.remove("scoop-install.ps1")

print("You can now run ani-cli by typing 'ani-cli' in the Git Bash profile in the Windows terminal.")

input("Installation complete, by yours truly. Cya. Press Enter to exit.")

p = subprocess.Popen([f"{home}\\scoop\\apps\\git\\current\\git-bash.exe", "ani-cli"], stdout=sys.stdout, shell=True, start_new_session=True)
p.communicate()