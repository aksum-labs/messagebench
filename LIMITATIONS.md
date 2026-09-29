# Limitations

Engineering candidate 0.2.0-rc.1 has completed local technical verification; genuine independent
review and public release approval are BLOCKED-BY-HUMAN.

Only pacs.008.001.08 and pacs.002.001.10 are supported. camt.053.001.08 is intentionally excluded
because complete redistribution rights were not established; see docs/camt053-asset-review.md.
The 100 paired fixtures are original synthetic cases, not real bank data or independently approved
examples. The 27 extracted fields do not cover all message information.

Contracts compare only declared assertions. Unknown required facts, ambiguous keys and unknown
timezones cannot pass. Keyed items require unique declared identifiers and explicit comparator
semantics. Other dates, fees, structured remittance and supplementary structures remain outside
the declared field inventory. Allowed message-ID regeneration is not a promise of ID equality.

No operational or scheme-rule validity, certification, account-standard correctness, settlement,
connectivity, translation, custody or whole-document preservation is claimed. No Ethiopian
proprietary rules or institutional endorsements exist in this project.

CLI bounds include file/XML quotas and CPU/wall/address-space limits; they are not an OS sandbox
or a peak-RSS guarantee. Library callers own process isolation. Linux is the verified safe-file
profile. Reports redact values but hashes can still enable correlation. Native dependency review
is bounded to the documented sources; no universal vulnerability-free assertion is made.

The supplied native wheel is platform-specific and is not proven reproducible. Python wheel/sdist
reproducibility is limited to two clean builds in the same locked environment. Offline installation
was performed by the implementer, not an independent person. Local Scorecard checks are not a
public repository score; no OpenSSF badge, signature identity or hosted CI result is fabricated.
