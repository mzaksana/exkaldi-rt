# coding=utf-8
#
# Yu Wang (University of Yamanashi)
# May, 2020
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections import namedtuple

_MAJOR_VERSION = '1'
_MINOR_VERSION = '1'
_PATCH_VERSION = '4'

version = namedtuple("ExKaldiRT",["plain","major","minor","patch"])(
                   '.'.join([_MAJOR_VERSION, _MINOR_VERSION, _PATCH_VERSION]),
                   _MAJOR_VERSION, _MINOR_VERSION, _PATCH_VERSION
                  )

