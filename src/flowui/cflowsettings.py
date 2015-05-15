# -*- coding: utf-8 -*-
#
# codimension - graphics python two-way code editor and analyzer
# Copyright (C) 2015  Sergey Satskiy <sergey.satskiy@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# $Id$
#

" The settings used for rendering and drawing "


# The recommended way to use custom settings is to derive from
# CFlowSettings and change the required options in a new class __init__.
# Then to create an instance of the custom settings class and use it
# accordingly.


from PyQt4.QtGui import QColor


class CFlowSettings:
    " Holds the control flow rendering and drawing settings "

    def __init__( self ):

        self.debug = False      # visible virtual cells

        self.hPadding = 5       # in pixels (left and right)
        self.vPadding = 5       # in pixels (top and bottom)

        self.lineWidth = 1      # used for connections and box edges
        self.lineColor = QColor( 0, 0, 0, 255 )

        self.needArrows = True  # affects connectors

        self.boxBGColor = QColor( 255, 255, 255, 255 )
        self.boxFGColor = QColor( 0, 0, 0, 255 )

        return


DEFAULT_CFLOW_SETTINGS = CFlowSettings()

