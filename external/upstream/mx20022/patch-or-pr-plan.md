# Apply and review the prepared patch

```bash
git clone https://github.com/socrates8300/mx20022.git
cd mx20022
git checkout 810cfa2e486745ca3a779c460a7768e1923f860a
git apply /path/to/messagebench/external/upstream/mx20022/upstream.patch
cargo fmt --all -- --check
cargo test --locked -p mx20022-parse --test preservation_v08
```

Rebase on the current upstream head before submission and re-run the exact tests. The patch changes only two files and introduces no library dependency. Proposed PR title: “Add v08 lexical identifier and duplicate Unicode remittance round-trip regression”.

Owner approves the public contribution identity and actual rights/sign-off, then submits a narrowly scoped PR or asks maintainers whether the fixture belongs in this location. Do not suggest that mx20022 lacks round-trip tests; it already has them. Submission is prepared, not accepted.
