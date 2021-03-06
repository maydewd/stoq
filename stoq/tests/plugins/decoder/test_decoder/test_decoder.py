#   Copyright 2014-2015 PUNCH Cyber Analytics Group
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
Overview
========

Test stoQ decoder

"""

from stoq.plugins import StoqDecoderPlugin


class TestDecoder(StoqDecoderPlugin):

    def __init__(self):
        super().__init__()

    def activate(self, stoq):
        self.stoq = stoq

        super().activate()

    def decode(self, payload, **kwargs):
        """
        Test stoQ decoder

        :param bytes payload: Payload to be decoded
        :param **kwargs kwargs: Additional attributes (unused)

        :returns: Base64 decoded content
        :rtype: list of tuples

        """

        return [(kwargs, payload),
                (kwargs, payload)]
