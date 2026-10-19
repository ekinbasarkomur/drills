CXX      ?= g++
CXXFLAGS ?= -std=c++20 -Wall -Wextra -Wno-unused-parameter -O1 -Iinclude

SRCS  := $(wildcard solutions/*.cpp)
BINS  := $(patsubst solutions/%.cpp,build/%,$(SRCS))
NAMES := $(notdir $(BINS))
HDRS  := $(wildcard include/*.hpp)

.PHONY: all test clean compdb $(NAMES)

all: test

build:
	@mkdir -p build

# leetcode.hpp pulls in every standard header; precompiling it keeps one problem at ~0.5s.
build/leetcode.hpp.pch: $(HDRS) | build
	@$(CXX) $(CXXFLAGS) -x c++-header include/leetcode.hpp -o $@

build/%: solutions/%.cpp $(HDRS) build/leetcode.hpp.pch | build
	@$(CXX) $(CXXFLAGS) $(if $(shell grep -l '"leetcode.hpp"' $<),-include-pch build/leetcode.hpp.pch) -o $@ $<

# `make lc0001_two_sum` builds and runs just that problem
$(NAMES): %: build/%
	@./build/$@

# `make` or `make test` builds and runs everything
test: $(BINS)
	@fail=0; for b in $(BINS); do echo "== $$b"; ./$$b || fail=1; done; \
	 if [ $$fail -ne 0 ]; then echo ""; echo "some problems are still failing"; exit 1; fi

# `make compdb` — regenerate compile_commands.json for clangd
compdb:
	bear -- $(MAKE) clean $(BINS); true

clean:
	rm -rf build
