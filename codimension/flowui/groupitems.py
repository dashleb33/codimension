# -*- coding: utf-8 -*-
#
# codimension - graphics python two-way code editor and analyzer
# Copyright (C) 2018  Sergey Satskiy <sergey.satskiy@gmail.com>
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

"""Virtual canvas items to handle groups (opened/collapsed)"""


from ui.qt import (Qt, QPointF, QPen, QBrush, QPainterPath, QColor,
                   QGraphicsRectItem, QGraphicsPathItem, QGraphicsItem,
                   QStyleOptionGraphicsItem, QStyle, QApplication,
                   QMimeData, QByteArray)
from .items import CellElement
from .auxitems import Connector
from .routines import getBorderColor


class HGroupSpacerCell(CellElement):

    """Represents a horizontal spacer cell used to shift items due to groups"""

    def __init__(self, ref, canvas, x, y):
        CellElement.__init__(self, ref, canvas, x, y)
        self.kind = CellElement.H_GROUP_SPACER

        # Number of spacers to be inserted
        self.count = 0

    def render(self):
        """Renders the cell"""
        self.width = self.count * 2 * self.canvas.settings.openGroupHSpacer
        self.height = 0
        self.minWidth = self.width
        self.minHeight = self.height
        return (self.width, self.height)

    def draw(self, scene, baseX, baseY):
        """Draws the cell"""
        # There is no need to draw anything. The cell just reserves some
        # horizontal space for better appearance
        self.baseX = baseX
        self.baseY = baseY


class GroupItemBase:

    """Common functionality for the group items"""

    def __init__(self):
        self.nestedRefs = []

        self.groupBeginCMLRef = None
        self.groupEndCMLRef = None

        # True if the previous item is terminal, i.e no connector needed
        self.isTerminal = False

    def getGroupId(self):
        """Provides the group ID"""
        return self.groupBeginCMLRef.id

    def _getText(self):
        """Provides the box text"""
        return self.groupBeginCMLRef.title

    def getLineRange(self):
        """Provides the line range"""
        return [self.groupBeginCMLRef.ref.beginLine,
                self.groupEndCMLRef.ref.endLine]

    def getAbsPosRange(self):
        """Provides the absolute position range"""
        return [self.groupBeginCMLRef.ref.begin,
                self.groupEndCMLRef.ref.end]

    def getSelectTooltip(self):
        """Provides the tooltip"""
        lineRange = self.getLineRange()
        return 'Group at lines ' + \
               str(lineRange[0]) + "-" + str(lineRange[1])

    def getGroupColors(self, defaultBG, defaultFG, defaultBorder=None):
        """Provides the item colors"""
        bg = defaultBG
        fg = defaultFG
        if self.groupBeginCMLRef.bgColor:
            bg = self.groupBeginCMLRef.bgColor
        if self.groupBeginCMLRef.fgColor:
            fg = self.groupBeginCMLRef.fgColor
        if self.groupBeginCMLRef.border:
            return bg, fg, self.groupBeginCMLRef.border
        if defaultBorder is None:
            return bg, fg, getBorderColor(bg)
        return bg, fg, defaultBorder


class EmptyGroup(GroupItemBase, CellElement, QGraphicsRectItem):

    """Represents an empty group"""

    def __init__(self, ref, canvas, x, y):
        GroupItemBase.__init__(self)
        CellElement.__init__(self, ref, canvas, x, y)
        QGraphicsRectItem.__init__(self, canvas.scopeRectangle)
        self.kind = CellElement.EMPTY_GROUP

        self.__textRect = None
        self.connector = None

        # To make double click delivered
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)

    def getColors(self):
        """Provides the item colors"""
        return self.getGroupColors(self.canvas.settings.emptyGroupBGColor,
                                   self.canvas.settings.emptyGroupFGColor)

    def render(self):
        """Renders the cell"""
        settings = self.canvas.settings
        self.__textRect = self.getBoundingRect(self._getText())

        vPadding = 2 * (settings.vCellPadding + settings.vTextPadding +
                        settings.collapsedOutlineWidth)
        self.minHeight = self.__textRect.height() + vPadding
        hPadding = 2 * (settings.hCellPadding + settings.hTextPadding +
                        settings.collapsedOutlineWidth)
        self.minWidth = max(self.__textRect.width() + hPadding,
                            settings.minWidth)
        self.height = self.minHeight
        self.width = self.minWidth
        return (self.width, self.height)

    def draw(self, scene, baseX, baseY):
        """Draws the cell"""
        self.baseX = baseX
        self.baseY = baseY

        # Add the connector as a separate scene item to make the selection
        # working properly
        settings = self.canvas.settings
        self.connector = Connector(settings, baseX + settings.mainLine, baseY,
                                   baseX + settings.mainLine,
                                   baseY + self.height)
        scene.addItem(self.connector)

        # Setting the rectangle is important for the selection and for
        # redrawing. Thus the selection pen with must be considered too.
        penWidth = settings.selectPenWidth - 1
        self.setRect(baseX + settings.hCellPadding - penWidth,
                     baseY + settings.vCellPadding - penWidth,
                     self.minWidth - 2 * settings.hCellPadding + 2 * penWidth,
                     self.minHeight - 2 * settings.vCellPadding + 2 * penWidth)
        scene.addItem(self)

        self.__bgColor, self.__fgColor, self.__borderColor = self.getColors()

    def paint(self, painter, option, widget):
        """Draws the collapsed group"""
        del option      # unused argument
        del widget      # unused argument

        settings = self.canvas.settings

        # Outer rectangle
        rectWidth = self.minWidth - 2 * settings.hCellPadding
        rectHeight = self.minHeight - 2 * settings.vCellPadding

        if self.isSelected():
            selectPen = QPen(settings.selectColor)
            selectPen.setWidth(settings.selectPenWidth)
            selectPen.setJoinStyle(Qt.RoundJoin)
            painter.setPen(selectPen)
        else:
            pen = QPen(self.__borderColor)
            pen.setStyle(Qt.DashLine)
            painter.setPen(pen)
        brush = QBrush(self.__bgColor)
        painter.setBrush(brush)
        painter.drawRect(self.baseX + settings.hCellPadding,
                         self.baseY + settings.vCellPadding,
                         rectWidth, rectHeight)

        # Inner rectangle
        rectWidth -= 2 * settings.collapsedOutlineWidth
        rectHeight -= 2 * settings.collapsedOutlineWidth
        pen = QPen(self.__borderColor)
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawRect(self.baseX + settings.hCellPadding +
                         settings.collapsedOutlineWidth,
                         self.baseY + settings.vCellPadding +
                         settings.collapsedOutlineWidth,
                         rectWidth, rectHeight)

        # Draw the text in the rectangle
        pen = QPen(self.__fgColor)
        painter.setFont(settings.monoFont)
        painter.setPen(pen)

        textWidth = self.__textRect.width() + 2 * settings.hTextPadding
        textShift = (rectWidth - textWidth) / 2
        painter.drawText(
            self.baseX + settings.hCellPadding +
            settings.hTextPadding + settings.collapsedOutlineWidth +
            textShift,
            self.baseY + settings.vCellPadding + settings.vTextPadding +
            settings.collapsedOutlineWidth,
            self.__textRect.width(), self.__textRect.height(),
            Qt.AlignLeft, self._getText())


class OpenedGroupBegin(GroupItemBase, CellElement, QGraphicsRectItem):

    """Represents beginning af a group which can be collapsed"""

    def __init__(self, ref, canvas, x, y):
        GroupItemBase.__init__(self)
        CellElement.__init__(self, ref, canvas, x, y)
        QGraphicsRectItem.__init__(self, canvas.scopeRectangle)
        self.kind = CellElement.OPENED_GROUP_BEGIN
        self.connector = None

        # These two items are filled when rendering is finished for all the
        # items in the group
        self.groupWidth = None
        self.groupHeight = None

        self.groupEndRow = None
        self.groupEndColumn = None

        # Nest level (starts from 1) for the group within the current scope
        self.nestLevel = None

        # Max group nest level (starts from 1) for the current scope
        self.maxNestLevel = None

        # Max total nest level for all the groups in the current scope
        self.maxTotalNestLevel = None

        # Max nest level for the groups within the current group
        self.maxGroupNestLevel = 0

        self.selfAndDeeperNestLevel = None
        self.selfMaxNestLevel = None

        # To make double click delivered
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)

    def getColors(self):
        """Provides the item colors"""
        return self.getGroupColors(self.canvas.settings.openGroupBGColor,
                                   self.canvas.settings.openGroupFGColor,
                                   self.canvas.settings.openGroupBorderColor)

    def render(self):
        """Renders the cell"""
        self.width = self.canvas.settings.openGroupVSpacer * 2
        self.height = self.canvas.settings.openGroupVSpacer * 2
        self.minWidth = self.width
        self.minHeight = self.height
        return (self.width, self.height)

    def draw(self, scene, baseX, baseY):
        """Draws the cell"""
        self.baseX = baseX
        self.baseY = baseY

        settings = self.canvas.settings

        # Setting the rectangle is important for the selection and for
        # redrawing. Thus the selection pen with must be considered too.
        penWidth = settings.selectPenWidth - 1

        groupWidth = self.groupWidth + 2 * settings.openGroupHSpacer

        self.setRect(baseX - penWidth + settings.openGroupHSpacer,
                     baseY - penWidth + settings.openGroupVSpacer,
                     groupWidth + 2 * penWidth,
                     self.groupHeight + 2 * (penWidth + settings.openGroupVSpacer))
        scene.addItem(self)

        # Add the connector as a separate scene item to make the selection
        # working properly. The connector must be added after a group,
        # otherwise a half of it is hidden by the group.
        if not self.isTerminal:
            xPos = baseX + settings.mainLine
            xPos += self.selfAndDeeperNestLevel * (2 * settings.openGroupHSpacer)
            self.connector = Connector(settings,
                                       xPos,
                                       baseY,
                                       xPos,
                                       baseY + settings.openGroupVSpacer * 2)
            scene.addItem(self.connector)

        self.__bgColor, self.__fgColor, self.__borderColor = self.getColors()

    def paint(self, painter, option, widget):
        """Draws the collapsed group"""
        del option      # unused argument
        del widget      # unused argument

        settings = self.canvas.settings

        # Group rectangle
        if self.isSelected():
            selectPen = QPen(settings.selectColor)
            selectPen.setWidth(settings.selectPenWidth)
            selectPen.setJoinStyle(Qt.RoundJoin)
            painter.setPen(selectPen)
        else:
            pen = QPen(self.__borderColor)
            pen.setStyle(Qt.DotLine)
            pen.setWidth(1)
            painter.setPen(pen)
        brush = QBrush(self.__bgColor)
        painter.setBrush(brush)

        groupId = self.getGroupId()

        groupWidth = self.groupWidth + 2 * settings.openGroupHSpacer
        painter.drawRoundedRect(self.baseX + settings.openGroupHSpacer,
                                self.baseY + settings.openGroupVSpacer,
                                groupWidth,
                                self.groupHeight + 2 * settings.openGroupVSpacer,
                                settings.openGroupVSpacer,
                                settings.openGroupVSpacer)


class OpenedGroupEnd(GroupItemBase, CellElement):

    """Represents the end af a group which can be collapsed"""

    def __init__(self, ref, canvas, x, y):
        GroupItemBase.__init__(self)
        CellElement.__init__(self, ref, canvas, x, y)
        self.kind = CellElement.OPENED_GROUP_END

        self.groupBeginRow = None
        self.groupBeginColumn = None

        self.nestLevel = None
        self.maxNestLevel = None
        self.maxTotalNestLevel = None

        self.selfAndDeeperNestLevel = None

        # Max nest level for the groups within the current group
        self.maxGroupNestLevel = 1

    def render(self):
        """Renders the cell"""
        self.width = 0
        self.height = self.canvas.settings.openGroupVSpacer * 2
        self.minWidth = self.width
        self.minHeight = self.height
        return (self.width, self.height)

    def draw(self, scene, baseX, baseY):
        """Draws the cell"""
        self.baseX = baseX
        self.baseY = baseY

        if self.isTerminal:
            return

        # Add the connector as a separate scene item to make the selection
        # working properly
        settings = self.canvas.settings
        xPos = baseX + settings.mainLine
        xPos += self.selfAndDeeperNestLevel * (2 * settings.openGroupHSpacer)
        self.connector = Connector(settings,
                                   xPos,
                                   baseY,
                                   xPos,
                                   baseY + settings.openGroupVSpacer * 2)
        scene.addItem(self.connector)



class CollapsedGroup(GroupItemBase, CellElement, QGraphicsRectItem):

    """Represents a collapsed group"""

    def __init__(self, ref, canvas, x, y):
        GroupItemBase.__init__(self)
        CellElement.__init__(self, ref, canvas, x, y)
        QGraphicsRectItem.__init__(self, canvas.scopeRectangle)
        self.kind = CellElement.COLLAPSED_GROUP
        self.__textRect = None
        self.connector = None

        # To make double click delivered
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)

    def getColors(self):
        """Provides the item colors"""
        return self.getGroupColors(self.canvas.settings.collapsedGroupBGColor,
                                   self.canvas.settings.collapsedGroupFGColor)

    def render(self):
        """Renders the cell"""
        settings = self.canvas.settings
        self.__textRect = self.getBoundingRect(self._getText())

        vPadding = 2 * (settings.vCellPadding + settings.vTextPadding +
                        settings.collapsedOutlineWidth)
        self.minHeight = self.__textRect.height() + vPadding
        hPadding = 2 * (settings.hCellPadding + settings.hTextPadding +
                        settings.collapsedOutlineWidth)
        self.minWidth = max(self.__textRect.width() + hPadding,
                            settings.minWidth)
        self.height = self.minHeight
        self.width = self.minWidth
        return (self.width, self.height)

    def draw(self, scene, baseX, baseY):
        """Draws the cell"""
        self.baseX = baseX
        self.baseY = baseY

        # Add the connector as a separate scene item to make the selection
        # working properly
        settings = self.canvas.settings
        self.connector = Connector(settings, baseX + settings.mainLine, baseY,
                                   baseX + settings.mainLine,
                                   baseY + self.height)
        scene.addItem(self.connector)

        # Setting the rectangle is important for the selection and for
        # redrawing. Thus the selection pen with must be considered too.
        penWidth = settings.selectPenWidth - 1
        self.setRect(baseX + settings.hCellPadding - penWidth,
                     baseY + settings.vCellPadding - penWidth,
                     self.minWidth - 2 * settings.hCellPadding + 2 * penWidth,
                     self.minHeight - 2 * settings.vCellPadding + 2 * penWidth)
        scene.addItem(self)

        self.__bgColor, self.__fgColor, self.__borderColor = self.getColors()

    def paint(self, painter, option, widget):
        """Draws the collapsed group"""
        del option      # unused argument
        del widget      # unused argument

        settings = self.canvas.settings

        # Outer rectangle
        rectWidth = self.minWidth - 2 * settings.hCellPadding
        rectHeight = self.minHeight - 2 * settings.vCellPadding

        if self.isSelected():
            selectPen = QPen(settings.selectColor)
            selectPen.setWidth(settings.selectPenWidth)
            selectPen.setJoinStyle(Qt.RoundJoin)
            painter.setPen(selectPen)
        else:
            pen = QPen(self.__borderColor)
            painter.setPen(pen)
        brush = QBrush(self.__bgColor)
        painter.setBrush(brush)
        painter.drawRect(self.baseX + settings.hCellPadding,
                         self.baseY + settings.vCellPadding,
                         rectWidth, rectHeight)

        # Inner rectangle
        rectWidth -= 2 * settings.collapsedOutlineWidth
        rectHeight -= 2 * settings.collapsedOutlineWidth
        pen = QPen(self.__borderColor)
        painter.setPen(pen)
        painter.drawRect(self.baseX + settings.hCellPadding +
                         settings.collapsedOutlineWidth,
                         self.baseY + settings.vCellPadding +
                         settings.collapsedOutlineWidth,
                         rectWidth, rectHeight)

        # Draw the text in the rectangle
        pen = QPen(self.__fgColor)
        painter.setFont(settings.monoFont)
        painter.setPen(pen)

        textWidth = self.__textRect.width() + 2 * settings.hTextPadding
        textShift = (rectWidth - textWidth) / 2
        painter.drawText(
            self.baseX + settings.hCellPadding +
            settings.hTextPadding + settings.collapsedOutlineWidth +
            textShift,
            self.baseY + settings.vCellPadding + settings.vTextPadding +
            settings.collapsedOutlineWidth,
            self.__textRect.width(), self.__textRect.height(),
            Qt.AlignLeft, self._getText())
