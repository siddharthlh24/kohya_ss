import unittest
from unittest.mock import patch, mock_open
import importlib

# Since we are modifying an existing file, we need to reload it
import kohya_gui.class_tensorboard
importlib.reload(kohya_gui.class_tensorboard)

class TestTensorboardVisibility(unittest.TestCase):

    @patch('shutil.which', return_value='/usr/bin/tensorboard')
    @patch('kohya_gui.class_tensorboard.check_avx_support', return_value=True)
    def test_tensorboard_visibility_when_tensorboard_and_avx_are_present(self, mock_avx, mock_which):
        importlib.reload(kohya_gui.class_tensorboard)
        self.assertTrue(kohya_gui.class_tensorboard.visibility)

    @patch('shutil.which', return_value=None)
    @patch('kohya_gui.class_tensorboard.check_avx_support', return_value=True)
    def test_tensorboard_visibility_when_tensorboard_is_absent(self, mock_avx, mock_which):
        importlib.reload(kohya_gui.class_tensorboard)
        self.assertFalse(kohya_gui.class_tensorboard.visibility)

    @patch('shutil.which', return_value='/usr/bin/tensorboard')
    @patch('kohya_gui.class_tensorboard.check_avx_support', return_value=False)
    def test_tensorboard_visibility_when_avx_is_absent(self, mock_avx, mock_which):
        importlib.reload(kohya_gui.class_tensorboard)
        self.assertFalse(kohya_gui.class_tensorboard.visibility)

    @patch('builtins.open', mock_open(read_data="flags : avx"))
    def test_check_avx_support_present(self):
        self.assertTrue(kohya_gui.class_tensorboard.check_avx_support())

    @patch('builtins.open', mock_open(read_data="flags : sse"))
    def test_check_avx_support_absent(self):
        self.assertFalse(kohya_gui.class_tensorboard.check_avx_support())

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_check_avx_support_file_not_found(self, mock_open):
        self.assertFalse(kohya_gui.class_tensorboard.check_avx_support())


if __name__ == '__main__':
    unittest.main()
