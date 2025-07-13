import unittest
from unittest.mock import patch
import importlib

class TestTensorboardVisibility(unittest.TestCase):

    @patch('shutil.which', return_value='/usr/bin/tensorboard')
    def test_tensorboard_visibility_when_tensorboard_is_present(self, mock_which):
        import kohya_gui.class_tensorboard
        importlib.reload(kohya_gui.class_tensorboard)
        self.assertTrue(kohya_gui.class_tensorboard.visibility)

    @patch('shutil.which', return_value=None)
    def test_tensorboard_visibility_when_tensorboard_is_absent(self, mock_which):
        import kohya_gui.class_tensorboard
        importlib.reload(kohya_gui.class_tensorboard)
        self.assertFalse(kohya_gui.class_tensorboard.visibility)

if __name__ == '__main__':
    unittest.main()
