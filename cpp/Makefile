all: main

clean:
	rm main

main: src/main.cpp
	clang++ -std=c++17 -O3 -Wall -Wextra -pedantic-errors -march=native -mtune=native -o main src/main.cpp
