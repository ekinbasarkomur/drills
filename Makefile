# Run anything from the repository root.
#
#   make                  same as `make status`
#   make status           what is solved, per plan group (cached: ~1s when nothing changed)
#   make progress         the same, and rewrite PROGRESS.md
#   make next             the next problem to solve, per language and per parallel track
#   make 146              that problem's tests, in every language it has
#   make rust-146         ... in Rust only (also cpp-146, py-146, pandas-595, sql-584)
#   make new 146          scaffold a problem: any LeetCode id or slug, never overwrites
#   make copy 146 rust    put the solution on the clipboard, ready for LeetCode
#   make rust             every Rust file, raw cargo output (also cpp, python, pandas, sql)
#   make compdb           regenerate clangd's compile_commands.json for C++
#   make clean            wipe build directories and the status cache
#
# `make new ID=146 LANG=rust` and `make copy ID=146 LANG=rust` work too.

LC := leetcode
PY := python3

FIRST := $(firstword $(MAKECMDGOALS))
ARGS  := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
# LANG is also the locale variable in every shell, so only a command-line LANG= counts.
LANG_ARG := $(if $(filter command line,$(origin LANG)),$(LANG))

ifneq ($(filter $(FIRST),new copy),)

# Everything after `new` / `copy` is an argument, not a target.
new:
	@$(PY) scripts/new.py $(or $(ID),$(ARGS)) $(if $(LANG_ARG),--lang $(LANG_ARG))

copy:
	@$(PY) scripts/copy.py $(or $(ID),$(ARGS)) $(LANG_ARG)

%:
	@:

else

# Every LeetCode id that has a file, without leading zeros: `make 146`.
IDS := $(shell ls $(LC)/rust/src/bin $(LC)/cpp/solutions $(LC)/python $(LC)/pandas_track $(LC)/sql 2>/dev/null \
         | sed -n 's/^lc0*\([0-9][0-9]*\)_.*/\1/p' | sort -un)

.PHONY: all status progress next rust cpp python pandas sql clean $(IDS) compdb
# rust-% / cpp-% / py-% ... are pattern rules, and make skips pattern rules for phony targets,
# so they are deliberately not listed; no file by those names exists, so they always run.

all: status

status:
	@$(PY) scripts/progress.py

progress:
	@$(PY) scripts/progress.py --write

next:
	@$(PY) scripts/progress.py --next

$(IDS):
	@$(PY) scripts/run.py $@

rust-%:
	@$(PY) scripts/run.py $* --lang rust

cpp-%:
	@$(PY) scripts/run.py $* --lang cpp

py-%:
	@$(PY) scripts/run.py $* --lang python

python-%:
	@$(PY) scripts/run.py $* --lang python

pandas-%:
	@$(PY) scripts/run.py $* --lang pandas

sql-%:
	@$(PY) scripts/run.py $* --lang sql

rust:
	@cd $(LC)/rust && cargo test --no-fail-fast

cpp:
	@$(MAKE) --no-print-directory -k -j8 -C $(LC)/cpp

python:
	@uv run pytest $(LC)/python

pandas:
	@uv run pytest $(LC)/pandas_track

sql:
	@uv run pytest $(LC)/sql

compdb:
	@$(MAKE) --no-print-directory -C $(LC)/cpp compdb

clean:
	@cd $(LC)/rust && cargo clean
	@$(MAKE) --no-print-directory -C $(LC)/cpp clean
	@rm -rf .cache/status.json $(LC)/.pytest_cache
	@find $(LC) -name __pycache__ -type d -prune -exec rm -rf {} +

endif
