# Hume Philosopher Agent (HPA): an experiment in LLM-assisted history of philosophy

**This is an exploratory experiment to find out what current state-of-the-art LLMs can contribute to substantive Hume scholarship, in the environment available at the time of the test (12–13 October 2026). It is a record for a philosopher to evaluate, including unsuccessful objections, revised arguments and unresolved problems.**

The intention was to give an LLM a demanding research task and see how far it could pursue the investigation independently. It was not to develop an argument through a labor-intensive collaboration in which a Hume scholar continually supplies the interpretation and uses the LLM to execute it. Mikko Tolonen set the task, supplied access to existing open, publicly available resources and subsequently clarified its scope and standards. The LLM selected particular claims, investigated sources, constructed arguments and produced separate automated assessments. Those later instructions are documented: independence here concerns the execution of the research task, not the absence of human task-setting or feedback. The results have not received human expert validation.

**Current delivery: reconstruction cycle v5, 12–13 October 2026.** The earlier grounding proposal was reopened and its strong form failed: familiar causal kinds and explanatory success do not themselves establish continued objects, unified consciousness or rational endorsement. The replacement gives conclusion-specific evidential constraints, supported by causal, testimonial and historical contrasts. Garrett’s noninferential alternative and Baxter’s passive-assent account remain live; Hakkarainen and Baxter’s composition dispute is preserved. **No certified novel discovery, resolved personal-identity problem, or human validation is claimed.**

## Where to begin

1. Read [the account of the experiment](EXPERIMENT.md): aims, procedure, substantive results, failures and limits.
2. Read [the sustained integrated argument](reports/integrated-reconstruction-v5.md), then its [dependency model](models/integrated-v5.json), [actual coverage](models/coverage-v5.json) and [opposition](notes/integrated-opposition-v5.md). The [earlier positive reconstruction](reports/positive-reconstruction.md) and seven dossiers remain historical, provisional work.
3. Use [the philosopher's review guide](REVIEW_GUIDE.md) to test exact premises, counterarguments and claims of contribution.
4. Inspect [source coverage](SOURCES.md), [the bibliography](bibliography.bib), [reading ledgers and automated reviews](notes), and [the revision log](EXPERIMENT_LOG.md).

## What we aimed to do

The original brief asked whether sustained reading, careful reconstruction and criticism could produce consequential, defensible advances in history of philosophy. It required identifiable published claims, relevant Hume passages, explicit interpretive premises, the strongest reasonable defence of the scholar, and a positive alternative. A failed objection or a finding of underdetermination was an acceptable result. Novelty had to be checked, rather than inferred from the model's unfamiliarity with an argument. The [original research brief](REQUEST.md) is included.

The user subsequently directed the investigation toward Don Garrett, metaphysics proper, Jani Hakkarainen and Donald L. M. Baxter, and demanded a more substantial positive reading from Hume. These directions shaped the scope and standards; the model conducted the argumentative work within that brief. This was an interactive experiment in independent task execution, with the later instructions recorded, rather than a pre-registered benchmark.

## What was done and what survived

| Dossier | Question investigated | Current outcome |
|---|---|---|
| [HPA-001](dossiers/HPA-001.md) | Does Millican's reading of liberty and necessity improperly require exhaustive causal semantics? | Proposed refutation withdrawn; a known competing reading remains contestable. Beebee and Millican already address the relevant possibility. |
| [HPA-002](dossiers/HPA-002.md) | Does Zimmerman misidentify the motivational role of the representation argument? | Proposed refutation withdrawn after Book 3's retrospective evidence and the original qualifications were considered. |
| [HPA-003](dossiers/HPA-003.md) | Does Hume's constructive human science exclude Hakkarainen's restricted metaphysical suspension, compared with Zahn? | Science alone does not settle the issue. Compatibility with suspension does not establish Hume's actual suspension or epistemic warrant. |
| [HPA-004](dossiers/HPA-004.md) | Garrett–Millican: how do custom, reasoning and reflective induction relate? | Qualified support for customary dependence; classification of faulty demonstrations remains disputed. |
| [HPA-005](dossiers/HPA-005.md) | Hakkarainen: can whole–part dependence coexist with separability? | Local repair defended; exclusive general restriction unproved. The overlap alternative has published precedent in Qu, discussed by Clay. Baxter's later integrated reply prevents a claimed victory. |
| [HPA-006](dossiers/HPA-006.md) | Can a positive account of causal attribution avoid an unsupported substance supplement? | Contestable reconstruction using bodily causation, independent analogical experience and other-mind attribution. Basic analogy is already in scholarship. |
| [HPA-007](dossiers/HPA-007.md) | What do Hakkarainen and Baxter add about constitution, identity and assent? | Real rival accounts remain. Causal success does not settle complex unity, personal persistence, conscious unity or rational endorsement. |

The earlier central positive proposal was that Hume permits correctable local causal inquiry without first settling a substratum theory. Its objects' constitution, persistence and mode of acceptance remain further questions. The argument combines T1.4.5, EHU11, Book 2's social inferences and T1.4.6; the Appendix and Baxter's assent interpretation limit its reach. Its stronger grounding implications were withdrawn in v5; see [dossier status](models/dossier-status-v5.json). The current positive result concerns independent evidence for a relevant relation and the scope of a specified conclusion, while ordinary indexing and reflective authority require separate assessment.

## Why test this?

The comparison with recent LLM work in mathematics raises a useful question, but the tasks and standards of assessment differ. A mathematical argument can sometimes be checked through a formal proof. In history of philosophy, even a formally valid reconstruction must earn its attribution through historical texts, context, chronology and competing interpretations. An analytical approach makes some inferential steps testable; it does not make interpretation equivalent to proof checking.

As philosopher-led LLMs become possible research tools, further questions arise about how scholars will work with them and what contribution that collaboration makes. One response is “so what?” If the point of science is to advance the truth, why should the origin of a sound contribution determine its value? Whether a contribution actually advances the truth still needs to be established. This experiment is not a testament for or against either position in that debate. It is a dated test of where we stand with this kind of task: what the system can produce when given a demanding brief, and what survives philosophical scrutiny.

## How much does this establish about LLMs?

The record demonstrates that this particular workflow produced inspectable reconstructions, detected precedents and retracted several overreaching hypotheses. Whether it produced philosophically valuable understanding is the open evaluation question. Fluent prose, correct citations, finite logical checks and agreement between automated agents do not establish that value.

There was no untouched holdout, blinded expert assessment, human baseline, repeated-run comparison or control for prior model exposure. Exact model deployment and sampling configuration were not recorded in the research-stage ledgers. The sources were not all read, and an indexed corpus is not evidence that all Hume's works were inspected. Critical-edition and page-image collation remain incomplete. This case cannot estimate LLM accuracy in general or establish independent originality.

## Contents and access

The repository publishes the research brief, dossiers, four stage reports, a chronological dependency model, selected assessment notes, reading metadata, bibliography, evaluation protocol and a small dependency-free logical check. Full scholarly source files and the licensed primary corpus remain outside the public repository. The public history begins with this review edition; [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md) records important revisions but does not replace an exhaustive execution log.

The requested conversation transcript was exported separately for the user. It is not included in this public edition. [NOTICE.md](NOTICE.md) explains publication and source rights. Nothing here represents approval by the scholars discussed.

The optional logical illustration uses Python's standard library:

```sh
python3 -B scripts/check_argument_forms.py
```

It checks eight truth valuations and eight stipulated atom-worlds. Passing it verifies those formal consequences; it does not verify the interpretation of Hume. The published file inventory and checksums are in [PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json).

The new formal checks use only the standard library:

```sh
python3 -B scripts/check_reconstruction_v5.py
```

They check countermodels and minimal conflicting premise sets in stipulated translations. They do not prove historical attribution. The [new brief](REQUEST-v5.md), [prospective design](REORIENTATION-v5.md) and [cycle record](evaluation/session-v5.json) preserve the reorientation and corrections.
