# Three active FINOS contribution targets

Checked 1 October 2026. The shortlist concerns plausible technical fit, not a promise of maintainer interest. DataHelix is archived and excluded.

| Rank | Target | Useful bounded contribution | Required process / fit limits |
|---|---|---|---|
| 1 | [Morphir](https://github.com/finos/morphir) | Executable semantic example illustrating identifier strings, decimal/currency separation and repeated-item preservation across a model transformation. Use the existing categorized Markdown/Gherkin integration example framework, not a MessageBench dependency. | Read CONTRIBUTING.md, docs/developers/contributing.md and example-integration-tests.md at the current pinned checkout; initialize pinned submodules. Human rights/CLA requirements must be checked before submission. No claim that Morphir currently loses these fields. |
| 2 | [Common Domain Model](https://github.com/finos/common-domain-model) | A synthetic mapping/regression example demonstrating reference and repeated-item preservation at a documented mapping boundary, if the maintainers identify an actual CDM use case. | Follow its contributor agreement and test/build guide. CDM focuses on financial products/events, not this project's exact payment messages; do not import ISO payment semantics into CDM without agreement. |
| 3 | [Legend](https://github.com/finos/legend) | A narrow Pure/mapping data-quality test demonstrating lexical identifier preservation and explicit normalization, using the appropriate Legend component's tests. | Umbrella CONTRIBUTING.md redirects to component rules. Pick the exact engine/model component and inspect its contribution process before creating a PR. A broad unsolicited preservation framework would be unsuitable. |

Substantive contribution already prepared separately: mx20022 round-trip preservation edge-case packet with executable test and targeted witness. See external/upstream/mx20022/. No upstream PR or FINOS contribution credit is earned by a local patch.

Current source inspections and contribution URLs are recorded in evidence/recognition-sources.json. Existing FINOS project contributions do not require buying membership; new-project submission requires a Member proposal/sponsor. [Official rules](https://community.finos.org/docs/journey/participate/).
