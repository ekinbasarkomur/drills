# Python solutions

One file per problem in `solutions/`, named after the problem in snake_case.
Each file holds the solution *and* its tests, the same way the Rust project does.

    uv run pytest                          # every problem
    uv run pytest solutions/two_sum.py     # one problem
    uv run pytest -k two_sum               # by name
    uv run pytest -x -q                    # stop at first failure, quiet
    uv run python solutions/two_sum.py     # run the __main__ scratch block

Start a new problem by copying the template:

    cp template.py solutions/two_sum.py
