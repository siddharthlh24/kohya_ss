import os
import tempfile
import unittest
import subprocess
from pathlib import Path

class TestAllowedPaths(unittest.TestCase):
    def setUp(self):
        print("Setting up test...")
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_dir_path = Path(self.temp_dir.name)
        self.dummy_file = self.temp_dir_path / "dummy.txt"
        with open(self.dummy_file, "w") as f:
            f.write("dummy content")

        self.config_file = self.temp_dir_path / "config.toml"
        with open(self.config_file, "w") as f:
            f.write(f'''
[server]
allowed_paths = ["{self.temp_dir.name}"]
''')
        print("Setup complete.")

    def tearDown(self):
        print("Tearing down test...")
        self.temp_dir.cleanup()
        print("Teardown complete.")

    def test_allowed_paths(self):
        print("Running test_allowed_paths...")
        # Run the gui with the new config and check if it can access the dummy file
        process = subprocess.Popen(
            [
                "python",
                "kohya_gui.py",
                "--config",
                str(self.config_file),
                "--headless",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        print("Process started.")
        # Give the server some time to start
        try:
            stdout, stderr = process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()

        print(f"Stdout: {stdout.decode()}")
        print(f"Stderr: {stderr.decode()}")
        # Check if there are any errors in the stderr
        self.assertNotIn("InvalidPathError", stderr.decode())
        print("Test complete.")

if __name__ == "__main__":
    unittest.main()
