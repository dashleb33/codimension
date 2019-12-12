# -*- coding: utf-8 -*-
#
# codimension - graphics python two-way code editor and analyzer
# Copyright (C) 2015-2019  Sergey Satskiy <sergey.satskiy@gmail.com>
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

"""Various minimized items for a virtual canvas"""

# pylint: disable=C0305

from html import escape
from ui.qt import Qt, QBrush, QGraphicsRectItem, QGraphicsItem, QPainterPath
from utils.globals import GlobalData
from .auxitems import Connector
from .iconmixin import IconMixin
from .cellelement import CellElement


class MinimizedCellBase(CellElement, IconMixin, QGraphicsRectItem):

    """Base for all minimized cells"""

    def __init__(self, iconFileName, ref, canvas, x, y):
        CellElement.__init__(self, ref, canvas, x, y)
        IconMixin.__init__(self, canvas, iconFileName)
        QGraphicsRectItem.__init__(self, canvas.scopeRectangle)

        self.rectWidth = None
        self.rectHeight = None
        self.connector = None

        # To make double click delivered
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)

    def renderCell(self, hIconPadding, vIconPadding):
        """Renders the cell"""
        settings = self.canvas.settings

        self.rectWidth = self.iconItem.iconWidth() + 2 * hIconPadding
        self.rectHeight = self.iconItem.iconHeight() + 2 * vIconPadding

        self.minWidth = self.rectWidth + 2 * settings.hCellPadding
        self.minHeight = self.rectHeight + 2 * settings.vCellPadding

        self.height = self.minHeight
        self.width = self.minWidth
        return (self.width, self.height)

    def drawCell(self, scene, baseX, baseY, hIconPadding, setupConnector):
        """Draws the cell"""
        self.baseX = baseX
        self.baseY = baseY

        # derived class method; it uses self.baseX and self.baseY
        setupConnector()
        scene.addItem(self.connector)

        settings = self.canvas.settings
        penWidth = settings.selectPenWidth - 1
        self.setRect(baseX + settings.hCellPadding - penWidth,
                     baseY + settings.vCellPadding - penWidth,
                     self.rectWidth + 2 * penWidth,
                     self.rectHeight + 2 * penWidth)
        scene.addItem(self)

        self.iconItem.setPos(
            baseX + settings.hCellPadding + hIconPadding,
            baseY + self.minHeight / 2 - self.iconItem.iconHeight() / 2)
        scene.addItem(self.iconItem)

    def paintCell(self, painter, bgColor, borderColor, option, widget):
        """Draws the independent comment"""
        del option
        del widget

        settings = self.canvas.settings
        painter.setPen(self.getPainterPen(self.isSelected(), borderColor))
        painter.setBrush(QBrush(bgColor))

        painter.drawRoundedRect(self.baseX + settings.hCellPadding,
                                self.baseY + settings.vCellPadding,
                                self.rectWidth, self.rectHeight,
                                settings.scopeRectRadius,
                                settings.scopeRectRadius)




class MinimizedExceptCell(MinimizedCellBase):

    """Represents a minimized except block"""

    def __init__(self, ref, canvas, x, y):
        MinimizedCellBase.__init__(self, 'hiddenexcept.svg', ref, canvas, x, y)
        self.kind = CellElement.EXCEPT_MINIMIZED

        self.__setTooltip()

    def __setTooltip(self):
        """Sets the item tooltip"""
        parts = []
        for part in self.ref.exceptParts:
            lines = part.getDisplayValue().splitlines()
            if len(lines) > 1:
                parts.append('except: ' + lines[0] + '...')
            elif len(lines) == 1:
                parts.append('except: ' + lines[0])
            else:
                parts.append('except:')
        self.iconItem.setToolTip('<pre>' + escape('\n'.join(parts)) + '</pre>')

    def __setupConnector(self):
        """Sets the connector"""
        settings = self.canvas.settings

        cellToTheLeft = self.canvas.cells[self.addr[1]][self.addr[0] - 1]
        leftEdge = cellToTheLeft.baseX + cellToTheLeft.minWidth
        height = min(self.minHeight / 2, cellToTheLeft.minHeight / 2)

        self.connector = Connector(
            self.canvas, leftEdge + settings.hCellPadding,
            self.baseY + height,
            cellToTheLeft.baseX +
            cellToTheLeft.minWidth - settings.hCellPadding,
            self.baseY + height)

        self.connector.penStyle = Qt.DotLine

    def render(self):
        """Renders the cell"""
        return self.renderCell(self.canvas.settings.hHiddenExceptPadding,
                               self.canvas.settings.vHiddenExceptPadding)

    def draw(self, scene, baseX, baseY):
        """Draws the cell"""
        self.drawCell(scene, baseX, baseY,
                      self.canvas.settings.hHiddenExceptPadding,
                      self.__setupConnector)

    def paint(self, painter, option, widget):
        """Draws the independent comment"""
        self.paintCell(painter,
                       self.canvas.settings.hiddenExceptBGColor,
                       self.canvas.settings.hiddenExceptBorderColor,
                       option, widget)

    def mouseDoubleClickEvent(self, event):
        """Jump to the appropriate line in the text editor"""
        if self.editor:
            firstExcept = self.ref.exceptParts[0]
            GlobalData().mainWindow.raise_()
            GlobalData().mainWindow.activateWindow()
            self.editor.gotoLine(firstExcept.body.beginLine,
                                 firstExcept.body.beginPos)
            self.editor.setFocus()

    def getLineRange(self):
        """Provides the line range"""
        firstLineRange = self.ref.exceptParts[0].getLineRange()
        lastLineRange = self.ref.exceptParts[-1].getLineRange()
        return [firstLineRange[0], lastLineRange[1]]

    def getAbsPosRange(self):
        """Provides the absolute position range"""
        firstExcept = self.ref.exceptParts[0]
        lastExcept = self.ref.exceptParts[-1]
        return [firstExcept.begin, lastExcept.end]

    def getSelectTooltip(self):
        """Provides the tooltip"""
        lineRange = self.getLineRange()
        count = len(self.ref.exceptParts)
        if count == 1:
            return 'Minimized except block at lines ' + \
                   str(lineRange[0]) + "-" + str(lineRange[1])
        return str(count) + ' minimized except blocks at lines ' + \
               str(lineRange[0]) + "-" + str(lineRange[1])


class MinimizedCommentBase:

    """Base class for all the minimized comment cells"""

    def __init__(self):
        pass

    @staticmethod
    def getSelectTooltip(lineRange):
        """Provides the tooltip"""
        if lineRange[0] == lineRange[1]:
            return 'Minimized comment at line ' + str(lineRange[0])
        return 'Minimized comment at lines ' + \
            str(lineRange[0]) + '-' + str(lineRange[1])



class MinimizedIndependentCommentCell(MinimizedCommentBase, MinimizedCellBase):

    """Represents a minimized independent comment"""

    def __init__(self, ref, canvas, x, y):
        MinimizedCommentBase.__init__(self)
        MinimizedCellBase.__init__(self, 'hiddencomment.svg',
                                   ref, canvas, x, y)
        self.kind = CellElement.INDEPENDENT_MINIMIZED_COMMENT

        self.__setTooltip()

        self.leadingForElse = False
        self.sideForElse = False

    def __setTooltip(self):
        """Sets the item tooltip"""
        displayValue = self.ref.getDisplayValue()
        if displayValue:
            self.iconItem.setToolTip('<pre>' + escape(displayValue) + '</pre>')

    def __setupConnector(self):
        """Prepares the connector"""
        settings = self.canvas.settings

        cellToTheLeft = self.canvas.cells[self.addr[1]][self.addr[0] - 1]
        leftEdge = \
            cellToTheLeft.baseX + settings.mainLine + settings.hCellPadding

        if self.leadingForElse:
            self.connector = Connector(
                self.canvas, leftEdge + settings.hCellPadding,
                self.baseY + self.minHeight / 2,
                cellToTheLeft.baseX + settings.mainLine,
                self.baseY + self.minHeight / 2)
        else:
            self.connector = Connector(
                self.canvas, leftEdge + settings.hCellPadding,
                self.baseY + self.minHeight / 2,
                cellToTheLeft.baseX + settings.mainLine,
                self.baseY + self.minHeight / 2)
        self.connector.penColor = settings.hiddenCommentBorderColor
        self.connector.penWidth = settings.boxLineWidth

    def render(self):
        """Renders the cell"""
        return self.renderCell(self.canvas.settings.hHiddenCommentPadding,
                               self.canvas.settings.vHiddenCommentPadding)

    def draw(self, scene, baseX, baseY):
        """Draws the cell"""
        self.drawCell(scene, baseX, baseY,
                      self.canvas.settings.hHiddenCommentPadding,
                      self.__setupConnector)

    def paint(self, painter, option, widget):
        """Draws the independent comment"""
        self.paintCell(painter,
                       self.canvas.settings.hiddenCommentBGColor,
                       self.canvas.settings.hiddenCommentBorderColor,
                       option, widget)

    def adjustWidth(self):
        settings = self.canvas.settings
        cellToTheLeft = self.canvas.cells[self.addr[1]][self.addr[0] - 1]
        spareWidth = cellToTheLeft.width - cellToTheLeft.minWidth
        boxWidth = self.minWidth - 2 * settings.hCellPadding
        if spareWidth >= boxWidth:
            self.minWidth = 0
        else:
            self.minWidth = boxWidth - spareWidth
        self.width = self.minWidth

    def mouseDoubleClickEvent(self, event):
        """Jump to the appropriate line in the text editor"""
        # Needed custom because this item is used for ifs 'else' side comment
        CellElement.mouseDoubleClickEvent(self, event,
                                          self.ref.beginPos)

    def getLineRange(self):
        """Provides the line range"""
        return self.ref.getLineRange()

    def getAbsPosRange(self):
        """Provides the absolute position range"""
        return [self.ref.begin, self.ref.end]

    def getSelectTooltip(self):
        """Provides the tooltip"""
        return MinimizedCommentBase.getSelectTooltip(self.getLineRange())


class MinimizedLeadingCommentCell(MinimizedCommentBase, MinimizedCellBase):

    """Represents a minimized leading comment"""

    def __init__(self, ref, canvas, x, y):
        MinimizedCommentBase.__init__(self)
        MinimizedCellBase.__init__(self, 'hiddencomment.svg',
                                   ref, canvas, x, y)
        self.kind = CellElement.LEADING_MINIMIZED_COMMENT

        self.__setTooltip()

    def __setTooltip(self):
        """Sets the item tooltip"""
        displayValue = self.ref.leadingComment.getDisplayValue()
        if displayValue:
            self.iconItem.setToolTip('<pre>' + escape(displayValue) + '</pre>')

    def __setupConnector(self):
        """Prepares the connector"""
        settings = self.canvas.settings

        cellToTheLeft = self.canvas.cells[self.addr[1]][self.addr[0] - 1]
        if cellToTheLeft.kind != CellElement.CONNECTOR:
            leftEdge = self.baseX
        else:
            leftEdge = \
                cellToTheLeft.baseX + settings.mainLine + settings.hCellPadding

        shift = self.hShift * 2 * settings.openGroupHSpacer
        leftEdge += shift

        self.connector = Connector(self.canvas, 0, 0, 0, 0)
        connectorPath = QPainterPath()
        connectorPath.moveTo(leftEdge + settings.hCellPadding,
                             self.baseY + self.minHeight / 2)
        connectorPath.lineTo(leftEdge, self.baseY + self.minHeight / 2)
        connectorPath.lineTo(leftEdge - settings.hCellPadding,
                             self.baseY + self.minHeight + settings.vCellPadding)
        self.connector.setPath(connectorPath)
        self.connector.penColor = settings.hiddenCommentBorderColor
        self.connector.penWidth = settings.boxLineWidth

    def render(self):
        """Renders the cell"""
        return self.renderCell(self.canvas.settings.hHiddenCommentPadding,
                               self.canvas.settings.vHiddenCommentPadding)

    def draw(self, scene, baseX, baseY):
        """Draws the cell"""
        self.drawCell(scene, baseX, baseY,
                      self.canvas.settings.hHiddenCommentPadding,
                      self.__setupConnector)

    def paint(self, painter, option, widget):
        """Draws the independent comment"""
        self.paintCell(painter,
                       self.canvas.settings.hiddenCommentBGColor,
                       self.canvas.settings.hiddenCommentBorderColor,
                       option, widget)

    def adjustWidth(self):
        cellToTheLeft = self.canvas.cells[self.addr[1]][self.addr[0] - 1]
        if cellToTheLeft.kind != CellElement.CONNECTOR:
            return

        settings = self.canvas.settings
        spareWidth = cellToTheLeft.width - cellToTheLeft.minWidth
        boxWidth = self.minWidth - 2 * settings.hCellPadding
        if spareWidth >= boxWidth:
            self.minWidth = 0
        else:
            self.minWidth = boxWidth - spareWidth
        self.width = self.minWidth

    def getLineRange(self):
        """Provides the line range"""
        return self.ref.leadingComment.getLineRange()

    def getAbsPosRange(self):
        """Provides the absolute position range"""
        return [self.ref.leadingComment.begin, self.ref.leadingComment.end]

    def getSelectTooltip(self):
        """Provides the tooltip"""
        return MinimizedCommentBase.getSelectTooltip(self.getLineRange())



class MinimizedAboveCommentCell(MinimizedCommentBase, MinimizedCellBase):

    """Represents a minimized above comment"""

    def __init__(self, ref, canvas, x, y):
        MinimizedCommentBase.__init__(self)
        MinimizedCellBase.__init__(self, 'hiddencomment.svg',
                                   ref, canvas, x, y)
        self.kind = CellElement.ABOVE_MINIMIZED_COMMENT
        self.needConnector = False
        self.vConnector = None
        self.__setTooltip()

    def __setTooltip(self):
        """Sets the item tooltip"""
        displayValue = self.ref.leadingComment.getDisplayValue()
        if displayValue:
            self.iconItem.setToolTip('<pre>' + escape(displayValue) + '</pre>')

    def __setupConnector(self):
        """Prepares the connector"""
        settings = self.canvas.settings

        leftEdge = \
            self.baseX + settings.mainLine + settings.hCellPadding

        self.connector = Connector(self.canvas, 0, 0, 0, 0)
        connectorPath = QPainterPath()
        connectorPath.moveTo(leftEdge + settings.hCellPadding,
                             self.baseY + self.minHeight / 2)
        connectorPath.lineTo(leftEdge,
                             self.baseY + self.minHeight / 2)
        connectorPath.lineTo(leftEdge - settings.hCellPadding,
                             self.baseY + self.minHeight + settings.vCellPadding)
        self.connector.setPath(connectorPath)
        self.connector.penColor = settings.commentBorderColor
        self.connector.penWidth = settings.boxLineWidth

    def render(self):
        """Renders the cell"""
        self.renderCell(self.canvas.settings.hHiddenCommentPadding,
                        self.canvas.settings.vHiddenCommentPadding)
        self.minWidth += self.canvas.settings.mainLine
        self.minWidth += self.canvas.settings.hCellPadding
        self.width = self.minWidth
        return (self.width, self.height)

    def draw(self, scene, baseX, baseY):
        """Draws the cell"""
        if self.needConnector:
            self.vConnector = Connector(
                self.canvas, baseX + self.canvas.settings.mainLine, baseY,
                baseX + self.canvas.settings.mainLine, baseY + self.height)
            scene.addItem(self.vConnector)

        self.drawCell(scene, baseX, baseY,
                      self.canvas.settings.hHiddenCommentPadding,
                      self.__setupConnector)

    def paint(self, painter, option, widget):
        """Draws the independent comment"""
        self.paintCell(painter,
                       self.canvas.settings.hiddenCommentBGColor,
                       self.canvas.settings.hiddenCommentBorderColor,
                       option, widget)

    def adjustWidth(self):
        """No need to adjust the width"""
        return

    def getLineRange(self):
        """Provides the line range"""
        return self.ref.leadingComment.getLineRange()

    def getAbsPosRange(self):
        """Provides the absolute position range"""
        return [self.ref.leadingComment.begin, self.ref.leadingComment.end]

    def getSelectTooltip(self):
        """Provides the tooltip"""
        return MinimizedCommentBase.getSelectTooltip(self.getLineRange())



class MinimizedSideCommentCell(MinimizedCommentBase, MinimizedCellBase):

    """Represents a minimized side comment"""

    def __init__(self, ref, canvas, x, y):
        MinimizedCommentBase.__init__(self)
        MinimizedCellBase.__init__(self, 'hiddencomment.svg',
                                   ref, canvas, x, y)
        self.kind = CellElement.SIDE_MINIMIZED_COMMENT

        self.__setTooltip()

    def __setTooltip(self):
        """Sets the item tooltip"""
        displayValue = self.ref.sideComment.getDisplayValue()
        if displayValue:
            self.iconItem.setToolTip('<pre>' + escape(displayValue) + '</pre>')

    def __setupConnector(self):
        """Prepares the connector"""
        settings = self.canvas.settings

        cellToTheLeft = self.canvas.cells[self.addr[1]][self.addr[0] - 1]
        if cellToTheLeft.kind == CellElement.CONNECTOR:
            pass

