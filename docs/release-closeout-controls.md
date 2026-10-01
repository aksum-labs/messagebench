# Release close-out controls

PR #7’s metadata refresh is distinct from the follow-up release changes. A real maintainer review of the exact head, normal protected merge and final-source hosted checks are prerequisites for publication; neither the App nor an AI can replace that review.

Main now has both classic protection and a no-bypass branch ruleset, with all five exact checks pinned to GitHub Actions App 15368: checks, dependencies, dependency-review, analyze and release-controls. Stale-review dismissal, code-owner review, last-push approval, thread resolution, linear history, no force push/deletion and administrator enforcement are retained. Read-only PR jobs read publicly available ruleset details, binding hidden bypass information to version-matched corporate readbacks. Missing/stale data fails closed. Administrative tokens are never issued to PR jobs. A fork runs the same tests with a read-only token; a platform failure requires maintainer repair/readback refresh, not a privileged fork exception. Real external-fork execution remains to be demonstrated by an actual contributor; same-repository CI is not relabelled as that evidence.

Release guard requires the tag to resolve to the exact current accepted main commit, a normal merged PR acceptance record and the latest successful required check of every named context from the exact source and official Actions App. Wrong source, old green checks, newer failed checks, missing contexts and incomplete policies have negative tests. After a squash merge, dispatch dependency-review with the real pre-merge base and Checks/CodeQL at the accepted main SHA before tagging. Later main changes make this strict release gate fail until the intended source/version policy is reviewed; never move a published immutable tag.

The expanded review packet hashes all corpus XML/JSON plus scripts, nine workflows, dependency lock and package metadata. It identifies semantic/rights/native review and release-engineering review separately. Two real independent reviewers complete decisions after executing/inspecting the packet. Software checks consistency only. An accountable human must verify reviewer identities, independence and authority, and substantively review the release scripts/workflows.

At protected environment approval, the accountable human must put this exact line in the approval comment, replacing HASH with the SHA-256 of the current `evidence/review-packet.json`:

```
REVIEWER-IDENTITIES-VERIFIED HASH
```

This attests that the human actually verified identities, independence, decision scope and authority. Release guard requires the actual GitHub approval record from a User account for release-review and the matching packet hash. It does not authenticate expertise or turn JSON booleans into an independent review. Do not enter that acknowledgment before performing the verification. Use an approved corporate human identity; the environment remains protected against self/admin bypass.

`REVIEWED_RELEASE_ENABLED` remains off until genuine decisions exist. The optional PyPI job is in the same protected workflow and requires `PYPI_RELEASE_ENABLED`; it verifies signed tag bytes then tests stock-index installation outside the checkout before publishing. The current stock lxml wheel fails the justified native profile, so this additional route remains disabled. It does not upload our locally built lxml wheel under somebody else’s package name. Use the supported CPython 3.12 Linux x86-64 offline bundle, retaining its native sources/notices and complete nested manifest.

Scheduled Python advisory scanning is dated and retained independently from source-bounded native advisory review. Fuzz/scan failure artifacts are uploaded with `always()`. Actions notifications require accountable maintainers to subscribe; no human response commitment is fabricated.
