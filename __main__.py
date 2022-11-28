# -*- coding: utf-8 -*-
#
#         PySceneDetect: Python-Based Video Scene Detector
#   ---------------------------------------------------------------
#     [  Site:   http://www.scenedetect.scenedetect.com/         ]
#     [  Docs:   http://manual.scenedetect.scenedetect.com/      ]
#     [  Github: https://github.com/Breakthrough/PySceneDetect/  ]
#
# Copyright (C) 2014-2022 Brandon Castellano <http://www.bcastell.com>.
# PySceneDetect is licensed under the BSD 3-Clause License; see the
# included LICENSE file, or visit one of the above pages for details.
#
""" ``scenedetect.__main__`` Module

Provides entry point for PySceneDetect's command-line interface (CLI)
functionality (in addition to using in other scripts via `import scenedetect`)
by installing the module and running the `scenedetect` command, or by calling:

  > python -m scenedetect

This module provides a high-level main() function, utilizing the scenedetect.cli
module, itself based on the click library, to provide command-line interface (CLI)
parsing functionality.  Also note that a convenience script scenedetect.py is also
included for development purposes (allows ./scenedetect.py vs python -m scenedetect)

Installing PySceneDetect (using `python setup.py install` in the parent directory)
will also add the `scenedetect` command to %PATH% be used from anywhere.
"""

# PySceneDetect Library Imports
from scenedetect.cli import scenedetect_cli as cli
from scenedetect.cli.context import CliContext


def main():
    """ Main: PySceneDetect command-line interface (CLI) entry point.

    Passes control flow to the CLI parser (using the click library), whose
    entry point is the decorated scenedetect.cli.scenedetect_cli function.

    Once options have been processed, the main program logic is executed in the
    :py:func:`scenedetect.cli.controller.run_scenedetect` function.
    """
    cli_ctx = CliContext() # CliContext object passed between CLI commands.
    cli.main(obj=cli_ctx)  # Parse CLI arguments with registered callbacks.


if __name__ == '__main__':
    main()


from scenedetect import VideoManager, SceneManager, StatsManager
from scenedetect.detectors import ContentDetector
from scenedetect.scene_manager import save_images, write_scene_list_html

video_path = '/Users/subring/Desktop/2022fallProject/tiktok2/stability ball flat dumbbell fly.mp4' C:\Users\subring\Desktop\2022fallProject\tiktok2
stats_path = 'result.csv'

video_manager = VideoManager([video_path])
stats_manager = StatsManager()
scene_manager = SceneManager(stats_manager)

scene_manager.add_detector(ContentDetector(threshold=30))

video_manager.set_downscale_factor()

video_manager.start()
scene_manager.detect_scenes(frame_source=video_manager)

# result
with open(stats_path, 'w') as f:
    stats_manager.save_to_csv(f, video_manager.get_base_timecode())

scene_list = scene_manager.get_scene_list()
print(f'{len(scene_list)} scenes detected!')

save_images(
    scene_list,
    video_manager,
    num_images=1,
    image_name_template='$SCENE_NUMBER',
    output_dir='scenes')

write_scene_list_html('result.html', scene_list)

for scene in scene_list:
    start, end = scene

    # your code
    print(f'{start.get_seconds()} - {end.get_seconds()}')