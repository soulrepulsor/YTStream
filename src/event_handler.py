from PyQt5 import QtCore, QtGui, QtWidgets
from ytscrape import YTScrape
from TableModel import TableModel

class EventHandler():

    def __init__(self):
        pass

    def search_button_on_click(self, keyword: str,
                               search_table: QtWidgets.QTableView):

        scrape = YTScrape(keyword)
        result = scrape.scrape()
        model = TableModel(result)
        search_table.setModel(model)
        search_table.hideColumn(1)
        search_table.resizeColumnsToContents()

