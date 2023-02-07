#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

"""
Example: Generate Python code from the app generated by xArmStudio software
"""

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from ArmMovement.xarm import BlocklyTool

# blockly app path
source_path = 'example.xml'
# the path is the python code to save
target_path = './blockly_app.py'
blockly = BlocklyTool(source_path)
blockly.to_python(target_path)