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

from dataclasses import dataclass
from typing import List

@dataclass
class A2FConfigCommon:
    stream_number: int
    add_silence_padding_after_audio: bool
    queue_size_after_streammux: int
    queue_size_after_a2e: int
    queue_size_after_a2f: int
    max_len_uuid: int
    min_sample_rate: int
    max_sample_rate: int

@dataclass
class A2FConfigGrpcInput:
    port: int
    low_fps: int
    low_fps_max_duration_second: int

@dataclass
class A2FConfigGrpcOutput:
    ip: str
    port: int

@dataclass
class Emotions:
    emotion_contrast: float
    live_blend_coef: float
    preferred_emotion_strength: float
    enable_preferred_emotion: bool
    emotion_strength: float
    max_emotions: int

@dataclass
class A2FConfigA2E:
    enabled: bool
    inference_interval: int
    model_path: str
    emotions: Emotions

@dataclass
class A2FConfigApi:
    bs_weight_multipliers: List[float]

@dataclass
class A2FConfigA2F:
    model_path: str
    api: A2FConfigApi

@dataclass
class A2FConfig:
    common: A2FConfigCommon
    grpc_input: A2FConfigGrpcInput
    grpc_output: A2FConfigGrpcOutput
    A2E: A2FConfigA2E
    A2F: A2FConfigA2F

