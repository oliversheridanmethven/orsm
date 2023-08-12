#!/usr/bin/env python3
import unittest
from PIL import Image
import numpy as np
from media.window import ascii_from_camera, stream_from_camera
from contextlib import nullcontext


class AsciiFromCamera(unittest.TestCase):

    def setUp(self):
        self.image_size = [500, 500]

        def get_camera(*args, successful, **kwargs):
            class MockCamera:
                @staticmethod
                def read():
                    example_image_array = np.random.rand(*self.image_size, 3) * 255
                    example_image = Image.fromarray(example_image_array.astype('uint8')).convert('RGBA')
                    return [True, example_image] if successful else [False, None]

                @staticmethod
                def release():
                    pass

            return MockCamera

        self.generate_mock_camera = get_camera

    def test_ascii_from_camera(self):
        for successful in [True, False]:
            mock_camera = self.generate_mock_camera(successful=successful)
            with self.assertRaises(RuntimeError, msg=f"We expect this camera to fail.") if not successful else nullcontext():
                ascii_from_camera(camera=mock_camera)

    def test_webcam_streamer(self):
        for successful in [True, False]:
            mock_camera = self.generate_mock_camera(successful=successful)
            with self.assertRaises(RuntimeError, msg=f"We expect this camera to fail.") if not successful else nullcontext():
                timeout = 1
                frame_rate = 10
                webcam_streamer = stream_from_camera(camera=mock_camera, timeout=timeout)
                images_produced = 0
                for image in webcam_streamer:
                    self.assertIsInstance(image, str)
                    self.assertTrue(image)
                    images_produced += 1
                self.assertGreaterEqual(images_produced, 1, "At least one image should have been produced.")
                self.assertGreaterEqual(images_produced, frame_rate * timeout, f"We expect images of size {self.image_size} to be processed sufficiently fast to satisfy our desired framerate.")


if __name__ == '__main__':
    unittest.main()
