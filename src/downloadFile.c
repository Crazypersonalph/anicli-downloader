#include <stdlib.h>
#include <stdio.h>
#include <curl/curl.h>

void downloadFile(char *url, char *filename)
{
    FILE *fp;
    CURL *curl;
    fp = fopen(filename, "wb");
    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, NULL);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, fp);
        curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, FALSE);
        curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, FALSE);
        curl_easy_perform(curl);
        fclose(fp);
        curl_easy_cleanup(curl);
        curl_global_cleanup();
    }
}