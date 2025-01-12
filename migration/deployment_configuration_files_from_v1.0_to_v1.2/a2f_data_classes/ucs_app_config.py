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

####### UCS A2F App configs DataClass ################
from dataclasses import dataclass

@dataclass
class UCSConfig:
    streamNumber: int
    a2eEnabled: bool
    a2eInferenceInterval: int
    faceParams: str
    a2fModelName: str
    a2fDeviceId: int
    a2eEmotionContrast: float
    a2eLiveBlendCoef: float
    a2eEnablePreferredEmotion: bool
    a2ePreferredEmotionStrength: float
    a2eEmotionStrength: float
    a2eMaxEmotions: int
    addSilencePaddingAfterAudio: bool
    queueAfterStreammux: int
    queueAfterA2F: int
    queueAfterA2E: int
    maxLenUUID: int
    maxSampleRate: int
    minSampleRate: int
    lowFps: int
    lowFpsMaxDurationSecond: int
    useFP16A2F: bool
    useFP16A2E: bool
