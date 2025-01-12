# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

####### A2F Controller configs DataClasses ################
from dataclasses import dataclass

@dataclass
class URL:
    ip: str
    port: int


@dataclass
class ServerReceiver:
    port: int
    max_wait_time_idle_ms: int


@dataclass
class ServerPublicInterface:
    port: int
    max_user_number: int


@dataclass
class A2FControllerConfigConnections:
    send_audio: URL
    receive_anim_data: ServerReceiver


@dataclass
class A2FControllerGC:
    enabled: bool
    interval_run_second: int
    max_size_stored_data_second: int


@dataclass
class A2FControllerConfigCommon:
    max_processing_duration_second: int
    max_audio_buffer_size_second: int
    max_audio_clip_size_second: int
    max_sample_rate: int
    fps_logging_interval_second: int
    garbage_collector: A2FControllerGC


@dataclass
class A2FControllerConfig:
    audio2face: A2FControllerConfigConnections
    public_interface: ServerPublicInterface
    common: A2FControllerConfigCommon
