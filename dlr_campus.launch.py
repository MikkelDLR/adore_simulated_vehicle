# ********************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0
#
# SPDX-License-Identifier: EPL-2.0
# ********************************************************************************

from launch import LaunchDescription
from launch_ros.actions import Node

import sys
import os
sys.path.append(os.path.dirname(__file__)) # this line is very importatnt to find the helper functions
from simulated_vehicle import create_simulated_vehicle
from simulation_visualizer import create_visualizer

start_position_latitude = 52.315893
start_position_longitude = 10.561526
start_heading = 0.0

def generate_launch_description():
    return LaunchDescription([
        *create_simulated_vehicle(
            namespace="ego_vehicle",
            start_pose_lat_lon=(start_position_latitude, start_position_longitude, start_heading),
            goal_position_lat_lon=(52.314444, 10.561929),
            vehicle_id=111,
            v2x_id=0,
        ),
        *create_visualizer(
            whitelist=["ego_vehicle"],
            visualization_offset_lat_lon=(start_position_latitude, start_position_longitude),
        )
    ])
