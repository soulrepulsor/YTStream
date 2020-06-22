from PyQt5 import QtCore
from typing import List

class TableModel(QtCore.QAbstractTableModel):

    _data = List[List]

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index) -> int:
        return len(self._data)

    def columnCount(self, index) -> int:
        return len(self._data[0])

