import mimetypes
import os

from imswitch.imcommon import constants
from .basecontrollers import ImScrWidgetController


class FilesController(ImScrWidgetController):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._widget.setRootPath(os.path.join(constants.rootFolderPath, 'scripts'))

        # Connect FilesView signals
        self._widget.sigItemDoubleClicked.connect(self.checkAndOpenItem)

    def checkAndOpenItem(self, itemPath):
        mime, _ = mimetypes.guess_type(itemPath)
        if mime is not None and mime.startswith('text/'):
            self._commChannel.sigOpenFileFromPath.emit(itemPath)



# Copyright (C) 2020, 2021 TestaLab
# This file is part of ImSwitch.
#
# ImSwitch is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ImSwitch is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.