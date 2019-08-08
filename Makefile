CC=gcc

compile: main.c
				$(CC) `pkg-config --cflags gtk+-3.0` -o EvanBrosTiles main.c `pkg-config --libs gtk+-3.0`
				make run
run: EvanBrosTiles
				./EvanBrosTiles