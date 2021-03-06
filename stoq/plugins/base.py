#   Copyright 2014-2018 PUNCH Cyber Analytics Group
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

import logging

from pkg_resources import parse_version as version

from stoq import signal_handler, __version__

class StoqPluginBase:

    def __init__(self):
        self.is_activated = False
        self.min_stoq_version = None
        self.max_stoq_version = None
        self.incompatible_plugin = False
        super().__init__()

    @property
    def min_version(self):
        if self.min_stoq_version:
            return version(__version__) >= version(self.min_stoq_version)
        else:
            return True

    @property
    def max_version(self):
        if self.max_stoq_version:
            return version(__version__) < version(self.max_stoq_version)
        else:
            return True

    def activate(self):

        # Instantiate the logging handler for this plugin
        logname = "stoq.{}.{}".format(self.category, self.name)
        self.log = logging.getLogger(logname)

        if not self.min_version or not self.max_version:
            self.incompatible_plugin = True
            self.log.warning("Plugin not compatible with this version of stoQ. "
                             "Unpredictable results may occur!")

        # See if plugin options were provided when Stoq() was instantiated
        plugin_options = self.stoq.plugin_options.get(self.category, {}).get(self.name, {})
        for k in plugin_options:
            if plugin_options[k] is not None:
                setattr(self, k, plugin_options[k])

        if hasattr(self, 'max_tlp'):
            self.max_tlp = self.max_tlp.lower()

        self.is_activated = True
        self.log.debug("{} plugin activated".format(self.name))

    def deactivate(self):
        self.is_activated = False
        self.log.debug("{} plugin deactivated".format(self.name))

    def heartbeat(self, force=False):
        pass
