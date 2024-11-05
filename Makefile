

build:
	gcc -o bin/main.exe src/main.c src/downloadFile.c -Iinclude/ -IC:/msys64/ucrt64/bin/../include -DCURL_STATICLIB -DNGHTTP2_STATICLIB -DNGHTTP3_STATICLIB -LC:/msys64/ucrt64/bin/../lib -lcurl -lmingw32 -lgcc -lmingwex -lkernel32 -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -lmingw32 -lgcc -lmingwex -lkernel32 -lws2_32 -lbcrypt -lssl -lcrypto -lwldap32 -ladvapi32 -lcrypt32 -lbrotlidec -lbrotlicommon -lzstd -lnghttp2 -lnghttp3 -lpsl -lunistring -lws2_32 -liconv -lidn2 -liconv -lunistring -lssh2 -lws2_32 -lssl -lcrypto -lws2_32 -lgdi32 -lcrypt32 -lz -static -O3