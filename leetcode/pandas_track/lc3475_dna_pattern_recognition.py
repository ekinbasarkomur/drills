"""
3475. DNA Pattern Recognition  · Medium · https://leetcode.com/problems/dna-pattern-recognition/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    samples = frame(['sample_id', 'dna_sequence', 'species'], [[1, 'ATGCTAGCTAGCTAA', 'Human'], [2, 'GGGTCAATCATC', 'Human'], [3, 'ATATATCGTAGCTA', 'Human'], [4, 'ATGGGGTCATCATAA', 'Mouse'], [5, 'TCAGTCAGTCAG', 'Mouse'], [6, 'ATATCGCGCTAG', 'Zebrafish'], [7, 'CGTATGCGTCGTA', 'Zebrafish']], {})
    check(analyze_dna_patterns(samples), ['sample_id', 'dna_sequence', 'species', 'has_start', 'has_stop', 'has_atat', 'has_ggg'], [[1, 'ATGCTAGCTAGCTAA', 'Human', 1, 1, 0, 0], [2, 'GGGTCAATCATC', 'Human', 0, 0, 0, 1], [3, 'ATATATCGTAGCTA', 'Human', 0, 0, 1, 0], [4, 'ATGGGGTCATCATAA', 'Mouse', 1, 1, 0, 1], [5, 'TCAGTCAGTCAG', 'Mouse', 0, 0, 0, 0], [6, 'ATATCGCGCTAG', 'Zebrafish', 0, 1, 1, 0], [7, 'CGTATGCGTCGTA', 'Zebrafish', 0, 0, 0, 0]], ordered=True)
