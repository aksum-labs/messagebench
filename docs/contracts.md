# Preservation contracts and semantics

The bundled `pacs008-preserve.json` is a **draft engineering contract**, never an institutional
rule. JSON Schema Draft 2020-12 is in `schemas/contracts.schema.json`; unknown keys, duplicate
JSON keys, conflicting exclusions, duplicate assertion IDs/fields and all-optional assertion
sets are rejected. Maximum 1,000 assertions and 1 MiB JSON, with depth checked after decoding.
The Python JSON decoder may also reject excessive nesting before that check.

Each assertion names a built-in field, comparator, cardinality, missing-value policy and
required flag. No XPath, regex, scripts or executable expressions. Unknown fields and recognized
but unsupported comparators yield UNSUPPORTED, not success. Required unsupported/indeterminate
checks block PASS. `NOT_APPLICABLE` is reserved; this prototype has no applicability predicates
and never uses that state to suppress an error.

Absence and present-empty are distinct. Presence mismatch fails. Both absent may pass only
under `compare-presence`; under `require-present`, both absent are INDETERMINATE. XSD validation
runs before comparison, so schema-forbidden empty content fails input validation independently.

Identifiers remain exact strings. No IBAN/check-digit assumption. Money is numeric `Decimal`
and a separate currency; no rounding or foreign-exchange conversion. Numeric equality permits
lexical scale differences. No instructed/interbank amount conflation. Text is exact Unicode
unless an explicit compatible comparator declares NFC. XML decoding and newline rules apply;
byte identity and XML signature equivalence are not asserted. Ethiopic text is treated as text,
not a claim about acceptance by a payment scheme.

Multisets preserve multiplicity and ignore order. Ordered-list semantics are also unit-tested.
`allowed-regeneration` tests nonempty presence, not equality. Unknown timezone/calendar handling
is deferred: no date extraction or date equivalence is claimed. All dates appear as unexamined.
Keyed associations/comparators are recognized but unsupported; a batch never falls back to
positional, amount or name matching. The default `single` association requires exactly one
transaction on each side.

Coverage units are leaf or empty elements and attributes, not schema types or economic meaning.
PASS/FAIL comparisons mark only their actual extracted units examined; skipped/incomplete ones
do not. Exclusions are explicit by known field. Other-schema leaves are unsupported; remaining
units are unexamined. Unknown paths are SHA-256 labelled so arbitrary extension names are not
rendered. Counts do not imply complete-document preservation or equivalent comparator strength.

Exit precedence: 5 internal > 4 safety/resource > 2 config > 3 incomplete > 1 failure > 0 pass.
Invalid XML/XSD is exit 1. Assertions blocked by invalid inputs are INDETERMINATE but do not
replace that input failure with a derivative missing-evidence error. Both input outcomes are
reported when possible. Configuration failures return a redacted diagnostic before evaluation.
