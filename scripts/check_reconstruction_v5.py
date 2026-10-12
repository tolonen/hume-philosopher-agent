"""Finite translation checks, not proofs of historical attribution.

Standard library only. Run from either repository:
    /usr/bin/python3 -B scripts/check_reconstruction_v5.py
The script validates model references and prints compact reproducible results.
Possibility below is a witness in a stipulated finite frame, not belief or knowledge.
"""
import itertools
import json
from pathlib import Path


def minimal_unsatisfiable(predicates, worlds):
    """Return inclusion-minimal conflicting premise sets in the supplied domain."""
    names = list(predicates)
    found = []
    for n in range(1, len(names) + 1):
        for group in itertools.combinations(names, n):
            if any(set(old).issubset(group) for old in found):
                continue
            if not any(all(predicates[k](w) for k in group) for w in worlds):
                found.append(group)
    return found


def run():
    result = {}
    # The evidence premise says only that the bearer nature is unknown.
    ignorance = [dict(unknown=True, exists=x, suspend=s)
                 for x, s in itertools.product([False, True], repeat=2)]
    assert any(w['exists'] and not w['suspend'] for w in ignorance)
    assert any(not w['exists'] for w in ignorance)
    result['ignorance'] = {'models': len(ignorance), 'entails_existence': False,
                           'entails_suspension': False}
    # A valid logical alternative is not a historical attribution to Baxter.
    passive = dict(affirmative=True, corrective=True, strong_belief=True,
                   active_endorsement=False)
    assert all(passive[k] for k in ['affirmative', 'corrective', 'strong_belief'])
    result['assent_countermodel'] = passive
    result['other_bridge_countermodels'] = {
        'explanation_to_warrant': dict(no_bearer_in_explanation=True,
                                      all_warrant_dependencies_dispensable=False),
        'episode_to_ontology': dict(local_episode_attribution=True,
                                   perception_independent_mind_proved=False),
        'success_to_whole': dict(successful_relational_prediction=True,
                                additional_strict_whole=False),
        'effect_to_enrichment': dict(local_cause_estimate=True,
                                    independently_known_extra_relation=False,
                                    further_effect_licensed=False),
        'plausibility_to_event_truth': dict(plausible_narrative=True,
                                          narrated_event_occurred=False,
                                          author_has_concept=True)}
    # Preserve causal edges while varying owner labels: no episode-enriched
    # Humean evidence is claimed to be held fixed, only this bare graph.
    edges = ((0, 1), (1, 2), (2, 3))
    partitions = [(0,) + bits for bits in itertools.product((0, 1), repeat=3)
                  if 1 in bits]
    assert len(partitions) == 7 and len(set(partitions)) == 7
    result['owner_countermodels'] = {
        'same_bare_edges': edges, 'two_history_partitions': len(partitions),
        'examples': [partitions[0], partitions[-1]],
        'richer_sign_body_memory_context_held_fixed': False}
    # D: essential part must accompany exact whole. S: unrestricted separation
    # of two strict distinct relata requires a possible whole without this part.
    worlds = list(itertools.product((False, True), repeat=5))
    predicates = {
        'whole_in_strict_domain': lambda w: w[0],
        'essential_dependence': lambda w: all(not a or b for a, b in
                                               ((w[1], w[2]), (w[3], w[4]))),
        'unrestricted_separation': lambda w: not w[0] or
                            any(a and not b for a, b in
                                ((w[1], w[2]), (w[3], w[4])))}
    conflicts = minimal_unsatisfiable(predicates, worlds)
    assert conflicts == [tuple(predicates)]
    result['whole_part_minimal_conflict'] = conflicts
    result['repairs_not_attribution_proofs'] = {
        'restricted_separation_scope': 'Numerical difference need not be wholly distinct separability',
        'collective_existence': 'Additional whole excluded from strict domain'}
    # Appendix principles alone: distinct=True and perceived_connection=False.
    # Unity, not-bearer, and exhaustive grounds are EXTRA translations.
    frames = list(itertools.product((False, True), repeat=4))
    app = {
        'distinct_perceptions': lambda w: w[0],
        'no_perceived_connection': lambda w: not w[1],
        'unity_demand': lambda w: w[2],
        'no_simple_bearer': lambda w: not w[3],
        'exhaustive_grounds_ADDED': lambda w: not w[2] or w[1] or w[3]}
    assert any(app['distinct_perceptions'](w) and
               app['no_perceived_connection'](w) for w in frames)
    app_conflicts = minimal_unsatisfiable(app, frames)
    assert app_conflicts == [('no_perceived_connection', 'unity_demand',
                             'no_simple_bearer', 'exhaustive_grounds_ADDED')]
    result['appendix'] = {'two_stated_principles_satisfiable': True,
        'added_translation_minimal_conflict': app_conflicts,
        'exhaustiveness_textually_established': False,
        'no_perceived_connection_means_no_actual_connection': False}
    model = json.loads((Path(__file__).resolve().parents[1] /
                        'models/integrated-v5.json').read_text())
    ids = {p['id'] for p in model['propositions']}
    assert len(ids) == len(model['propositions'])
    for e in model['conjunctive_dependencies']:
        assert e['conjunctive'] and e['premises']
        assert all(p in ids for p in e['premises'])
    for t in model['consequence_tests']:
        assert all(p in ids for p in t['primary_evidence'])
    result['model_validation'] = {'propositions': len(ids),
         'edges': len(model['conjunctive_dependencies']),
         'tests': len(model['consequence_tests'])}
    result['historical_fidelity_proved'] = False
    return result


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
