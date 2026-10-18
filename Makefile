# Run anything from the repository root.
#
#   make                  every exercise, all three languages
#   make rust             every Rust exercise
#   make two_sum          that one exercise, in all three languages
#   make cpp-two_sum      that one exercise, in C++ only
#   make status           a grid of what is solved in which language
#   make progress         the same, and rewrite the PROGRESS.md tables
#   make list             the exercise names you can pass
#
# Each language project can still be driven from inside its own directory;
# this file only saves the `cd`.

RUST := algorithms/rust
PY   := algorithms/python
CPP  := algorithms/cpp

# Exercise names come from the C++ solutions, which exist for all of them.
NAMES := $(sort $(notdir $(basename $(wildcard $(CPP)/solutions/*.cpp))))

.PHONY: all rust python cpp status progress list clean $(NAMES)
# The rust-% / py-% / cpp-% targets are deliberately NOT phony: make skips
# pattern rules for phony targets, and these are pattern rules. No file by
# those names exists at the root, so they rebuild every time anyway.

all: status

# ---------------------------------------------------------------- per language

rust:
	@cd $(RUST) && cargo test --no-fail-fast

python:
	@cd $(PY) && uv run pytest

cpp:
	@$(MAKE) --no-print-directory -C $(CPP)

# ---------------------------------------------------------------- one exercise

$(NAMES): %: cpp-% rust-% py-%
	@:

rust-%:
	@printf "%-10s " "rust"
	@cd $(RUST) && cargo test --quiet --bin $* 2>&1 | grep -E "^test result" | tail -1 \
	  || echo "no such bin"

py-%:
	@printf "%-10s " "python"
	@cd $(PY) && uv run pytest -q solutions/$*.py 2>&1 | tail -1

cpp-%:
	@printf "%-10s " "cpp"
	@$(MAKE) --no-print-directory -C $(CPP) $* 2>&1 | grep -E "^test result" | tail -1 \
	  || echo "FAILED (see: make -C $(CPP) $*)"

# ---------------------------------------------------------------- housekeeping

status:
	@scripts/progress.py

progress:
	@scripts/progress.py --write

list:
	@printf "%s\n" $(NAMES)

clean:
	@cd $(RUST) && cargo clean
	@$(MAKE) --no-print-directory -C $(CPP) clean
	@rm -rf $(PY)/.pytest_cache $(PY)/solutions/__pycache__
