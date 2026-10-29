"""
2738. Count Occurrences in Text · Medium · https://leetcode.com/problems/count-occurrences-in-text/
Plan: 30 Days of Pandas · pekiştirme · String Methods

Problem: count the files whose content contains " bull " and " bear " as standalone words (a space on both sides).
Approach: walk the rows with iterrows and add the bool of `" bull " in content` to a counter (True counts as 1). Shorter: str.contains(" bull ").sum()
Time O(n·L), space O(1)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    bull = 0
    bear = 0

    for _, file in files.iterrows():
        bull += " bull " in file["content"]
        bear += " bear " in file["content"]

    return pd.DataFrame({"word": ["bull", "bear"], "count": [bull, bear]})


# ---------------------------------------------------------------- tests


def test_example_1():
    files = frame(
        ["file_name", "content"],
        [
            [
                "draft1.txt",
                "The stock exchange predicts a bull market which would make many investors happy.",
            ],
            [
                "draft2.txt",
                "The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market.",
            ],
            [
                "draft3.txt",
                "The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market. As always predicting the future market is an uncertain game and all investors should follow their instincts and best practices.",
            ],
        ],
        {"file_name": "object", "content": "object"},
    )
    check(
        count_occurrences(files),
        ["word", "count"],
        [["bull", 3], ["bear", 2]],
        ordered=False,
    )


def test_standalone_word_only():
    # "bullet", "bears", "bull." and a word at the very start or end of the
    # content do not count: the word needs a space on either side.
    files = frame(
        ["file_name", "content"],
        [
            ["a.txt", "bull at the start does not count"],
            ["b.txt", "a bullet and some bears are not a bull."],
            ["c.txt", "here is a bull and a bear in the middle"],
            ["d.txt", "the line ends with bear"],
        ],
        {"file_name": "object", "content": "object"},
    )
    check(
        count_occurrences(files),
        ["word", "count"],
        [["bull", 1], ["bear", 1]],
        ordered=False,
    )
