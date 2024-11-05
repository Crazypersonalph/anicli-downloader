

build:
	gcc -o bin/main.exe src/main.c src/downloadFile.c -Iinclude/ -DCURL_STATICLIB -lcurl -lmingw32 -lgcc -lmingwex -lkernel32 -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -lmingw32 -lgcc -lmingwex -lkernel32 -lws2_32 -lbcrypt -lwldap32 -ladvapi32 -lcrypt32 -lbrotlidec -lbrotlicommon -lzstd -lpsl -lunistring -lws2_32 -liconv -lidn2 -L/ucrt64/lib -liconv -L/ucrt64/lib -lunistring -lssh2 -lws2_32 -lcrypt32 -L/ucrt64/lib -lbcrypt -lz -static -O3