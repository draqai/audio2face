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

import grpc
from pathlib import Path
import os
from typing import List, Optional, Tuple, Union


GRPC_URI = "grpc.nvcf.nvidia.com:443"


def create_channel(
    ssl_cert: Optional[Union[str, os.PathLike]] = None,
    uri=GRPC_URI,
    use_ssl: bool = False,
    metadata: Optional[List[Tuple[str, str]]] = None,
) -> grpc.Channel:
    """Creates a secure grpc channel."""

    def metadata_callback(context, callback):
        callback(metadata, None)

    if ssl_cert is not None or use_ssl:
        root_certificates = None
        if ssl_cert is not None:
            ssl_cert = Path(ssl_cert).expanduser()
            with open(ssl_cert, "rb") as f:
                root_certificates = f.read()
        creds = grpc.ssl_channel_credentials(root_certificates)
        if metadata:
            auth_creds = grpc.metadata_call_credentials(metadata_callback)
            creds = grpc.composite_channel_credentials(creds, auth_creds)
        channel = grpc.secure_channel(uri, creds)
    else:
        channel = grpc.insecure_channel(uri)
    return channel
