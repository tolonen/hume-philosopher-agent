"""Finite countermodels only: no automatic claims about Hume's intended meaning."""
import itertools
import json
import platform
import sys
from pathlib import Path


def implies(p, q):
    return not p or q


def check():
    converse_countermodels = []
    for d, c, p in itertools.product([False, True], repeat=3):
        if (d == c) and implies(c, p):
            assert implies(d, p)
            if not implies(p, d):
                converse_countermodels.append(dict(D=d, C=c, P=p))
    assert converse_countermodels == [dict(D=False, C=False, P=True)]

    # An item exists iff all its essential atoms exist. Each subset is allowed.
    atoms = frozenset('abc')
    worlds = [frozenset(x) for n in range(4)
              for x in itertools.combinations(sorted(atoms), n)]
    whole, other, part = frozenset('ab'), frozenset('bc'), frozenset('a')
    def can_without(x, y):
        return [sorted(w) for w in worlds if x <= w and not y <= w]
    assert can_without(whole, other) and can_without(other, whole)
    assert not can_without(whole, part) and can_without(part, whole)
    assert whole & other and not whole <= other and not other <= whole
    return {
        'schema': 'hpa-formal-checks-v1',
        'date': '2026-10-12',
        'python': sys.executable, 'version': platform.python_version(),
        'truth_valuations_checked': 8,
        'converse_countermodels': converse_countermodels,
        'essential_atom_worlds_checked': len(worlds),
        'W_without_V': can_without(whole, other),
        'V_without_W': can_without(other, whole),
        'W_without_a': can_without(whole, part),
        'a_without_W': can_without(part, whole),
        'historical_scope': 'Checks consequences of stated formal premises only; not evidence that Hume endorses them.',
        'novelty': 'Converse objection and overlap example already in Clay/Qu; see HPA-005.',
        'passed': True,
    }


if __name__ == '__main__':
    record = check()
    # Print results; do not write a disposable local result file.
    print(json.dumps(record))
