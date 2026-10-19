import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).parent


class ArchiveContractTest(unittest.TestCase):
    def test_disposition_is_prominent(self) -> None:
        readme = (ROOT / "README.md").read_text()
        ownership = (ROOT / "OWNERSHIP.md").read_text()

        self.assertIn("Disposition: archive", readme)
        self.assertIn("Do not run or deploy", readme)
        self.assertIn("Disposition: archive after this audit lands", ownership)
        self.assertIn("Recovery contract", ownership)

    def test_historical_launcher_fails_closed(self) -> None:
        result = subprocess.run(
            [ROOT / "Makefile"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Castela is archived", result.stderr)


if __name__ == "__main__":
    unittest.main()
