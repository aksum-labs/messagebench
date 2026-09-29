# Adding a case

Use original synthetic data only. Select one declared preservation rule and create a valid
positive control before its targeted mutation. Preserve source/target XML separately. Record
expected status, exit code, failing assertion IDs and XSD validity before running the oracle.
Do not change expectations merely to accommodate output. Hash files and include provenance,
control-case link and genuine review metadata in the closed corpus manifest.

The existing deterministic builders in scripts/build_extended_corpus.py and
scripts/build_pacs002_corpus.py illustrate authoring without importing the oracle. Regenerate
the combined index with scripts/build_release_index.py, run corpus verify and pytest, and
inspect changed hashes. Security-invalid documents belong in clearly marked synthetic tests.
Independent reviewers should record their real handles and exact reviewed hashes.
