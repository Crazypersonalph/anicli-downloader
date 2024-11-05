#include <curl/curl.h>
#include "downloadFile.h"
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>



int main(void)
{
    // Retrieve environment variables
    const char *homedrive = getenv("HOMEDRIVE");
    const char *homepath = getenv("HOMEPATH");
    const char *location = "\\scoop\\apps\\git\\current\\bin\\bash.exe";

    // Check if environment variables are available
    if (homedrive == NULL || homepath == NULL) {
        fprintf(stderr, "Error: HOMEDRIVE or HOMEPATH not set.\n");
        return 1;
    }

    // Allocate memory for the combined path
    char env[1024];  // Adjust size if necessary
    snprintf(env, sizeof(env), "%s%s%s", homedrive, homepath, location);


    downloadFile("https://github.com/Crazypersonalph/anicli-downloader/raw/refs/heads/main/initiate.ps1", "initiate.ps1");
    downloadFile("https://raw.githubusercontent.com/Crazypersonalph/anicli-downloader/refs/heads/main/scoop-install.ps1", "scoop-install.ps1");
    
    system("powershell.exe Set-ExecutionPolicy RemoteSigned -Scope CurrentUser\n");
    system("powershell.exe -File initiate.ps1\n");
    system("powershell.exe -File scoop-install.ps1\n");

    remove("initiate.ps1");
    remove("scoop-install.ps1");

    printf("You can now run ani-cli by typing 'ani-cli' in the Git Bash profile in the Windows terminal.\n");
    printf("Installation complete, by yours truly. Cya. Press Enter to exit.");
    getchar();

    char final[1024];
    snprintf(final, sizeof(final), "start %s ani-cli", env);
    system(final);
    return 0;
}
