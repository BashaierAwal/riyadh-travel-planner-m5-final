"""Verify the saved V3 cohort using an isolated historical-source copy; no model calls."""
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil, subprocess, sys, hashlib
ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"evaluate": "783d38e783060d585bce8f6d7cfd2eec896289597c082ae964c84baab02c283f", "experiment": "f5783fce81b04f39cc34a03b54853dcc1a20a3f4618775c433676ba5c5f022f9"}
def main():
    with TemporaryDirectory(prefix="m5-verification-") as temp:
        target = Path(temp) / "project"
        shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
        for name, expected in EXPECTED.items():
            body = (ROOT / "historical" / (name + ".txt")).read_bytes()
            if hashlib.sha256(body).hexdigest() != expected:
                raise ValueError("Historical source checksum mismatch: " + name)
            (target / "m5eval" / (name + ".py")).write_bytes(body)
        return subprocess.run([sys.executable, "scripts/verify_full_cohort.py"], cwd=target).returncode
if __name__ == "__main__":
    sys.exit(main())
