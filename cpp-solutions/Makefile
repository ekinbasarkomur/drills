CXX      ?= g++
CXXFLAGS ?= -std=c++20 -Wall -Wextra -O2 -Iinclude

SRCS := $(wildcard solutions/*.cpp)
BINS := $(patsubst solutions/%.cpp,build/%,$(SRCS))
NAMES := $(notdir $(BINS))

.PHONY: all test clean $(NAMES)

all: test

build:
	@mkdir -p build

build/%: solutions/%.cpp include/test.hpp | build
	$(CXX) $(CXXFLAGS) -o $@ $<

# `make two_sum` builds and runs just that problem
$(NAMES): %: build/%
	@./build/$@

# `make` or `make test` builds and runs everything
test: $(BINS)
	@fail=0; for b in $(BINS); do echo "== $$b"; ./$$b || fail=1; done; \
	 if [ $$fail -ne 0 ]; then echo ""; echo "some problems are still failing"; exit 1; fi

clean:
	rm -rf build
