"""Prepare hash-bound review forms; verify attestations, never invent human independence."""

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def packet():
    manifest = json.loads((ROOT / "corpus/index.json").read_text())
    files = [
        ROOT / "corpus/index.json",
        *sorted((ROOT / "contracts").glob("*.json")),
        *sorted((ROOT / "schemas").glob("*.json")),
        *sorted((ROOT / "schemas/iso").glob("*")),
    ]
    files.extend(sorted((ROOT / "src").rglob("*.py")))
    files.extend(
        [
            ROOT / "LICENSE",
            ROOT / "NOTICE",
            ROOT / "evidence/rights-register.json",
            ROOT / "evidence/native-source-pins.json",
        ]
    )
    files.extend(sorted((ROOT / "third-party").glob("*")))
    for case in manifest["cases"]:
        files.extend(ROOT / "corpus" / case[side] for side in ("source", "target"))
    return {
        "schema_version": "1.0",
        "purpose": "Independent human semantic and rights review",
        "assets": {str(p.relative_to(ROOT)): digest(p) for p in sorted(set(files))},
        "cases": [
            {
                k: c[k]
                for k in [
                    "id",
                    "source_sha256",
                    "target_sha256",
                    "contract",
                    "expected",
                    "rationale",
                    "control",
                ]
            }
            for c in manifest["cases"]
        ],
        "required_reviews": 2,
        "review_scope": [
            "expected outcomes",
            "positive controls",
            "contract semantics",
            "coverage limits",
            "schema rights/provenance",
        ],
        "independence_warning": (
            "A form or valid hash does not prove identity, expertise or "
            "independence. An accountable human must verify those facts."
        ),
    }


def canonical(document):
    return (json.dumps(document, sort_keys=True, indent=2) + "\n").encode()


def verify(document, reviews):
    sha = hashlib.sha256(canonical(document)).hexdigest()
    ids = {c["id"] for c in document["cases"]}
    accepted = []
    for review in reviews:
        if set(review) != {
            "schema_version",
            "packet_sha256",
            "reviewer_handle",
            "reviewer_is_human",
            "independent_of_implementation",
            "reviewed_at",
            "cases",
            "rights_approved",
            "scope_approved",
        }:
            raise ValueError("Review fields invalid")
        if review["schema_version"] != "1.0" or review["packet_sha256"] != sha:
            raise ValueError("Review packet does not match current assets")
        if any(
            review[k] is not True
            for k in [
                "reviewer_is_human",
                "independent_of_implementation",
                "rights_approved",
                "scope_approved",
            ]
        ):
            raise ValueError("Required reviewer attestations absent")
        handle = review["reviewer_handle"]
        if isinstance(handle, str):
            handle = handle.strip().casefold()
        if not isinstance(handle, str) or not handle.strip() or handle in accepted:
            raise ValueError("Distinct real reviewer handles required")
        if not isinstance(review["reviewed_at"], str) or not review["reviewed_at"].strip():
            raise ValueError("Review date absent")
        if set(review["cases"]) != ids or any(v != "APPROVE" for v in review["cases"].values()):
            raise ValueError("Every case requires an explicit approval")
        accepted.append(handle)
    return {
        "status": "PASS" if len(accepted) >= 2 else "BLOCKED-BY-HUMAN",
        "verified_attestation_count": len(accepted),
        "required": 2,
        "packet_sha256": sha,
        "identity_and_independence_verified_by_software": False,
        "scope": "Hash/decision consistency only; accountable humans must authenticate reviewers.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["prepare", "verify"])
    parser.add_argument("--reviews", type=Path, default=ROOT / "reviews")
    args = parser.parse_args()
    document = packet()
    if args.command == "prepare":
        (ROOT / "evidence/review-packet.json").write_bytes(canonical(document))
        form = {
            "schema_version": "1.0",
            "packet_sha256": hashlib.sha256(canonical(document)).hexdigest(),
            "reviewer_handle": "",
            "reviewer_is_human": False,
            "independent_of_implementation": False,
            "reviewed_at": "",
            "rights_approved": False,
            "scope_approved": False,
            "cases": {c["id"]: "NOT_REVIEWED" for c in document["cases"]},
        }
        (ROOT / "docs/reviewer-form.template.json").write_bytes(canonical(form))
        print("Prepared hash-bound review packet and unfilled form; no review asserted.")
    else:
        reviews = [json.loads(p.read_text()) for p in sorted(args.reviews.glob("*.json"))]
        try:
            result = verify(document, reviews)
        except (ValueError, TypeError, KeyError) as exc:
            print(json.dumps({"status": "BLOCKED-BY-HUMAN", "reason": str(exc)}))
            return 3
        print(json.dumps(result, indent=2))
        return 0 if result["status"] == "PASS" else 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
