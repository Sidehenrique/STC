import pyqtgraph as pg
import numpy as np
x = np.arange(1000)
y = np.random.normal(size=(3, 1000))
plotWidget = pg.plot(title="Three plot curves")
for i in range(3):
    plotWidget.plot(x, y[i], pen=(i,3))

# class MainWindow(QtWidgets.QMainWindow):
#
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#
#         self.graphWidget = pg.PlotWidget()
#         self.setCentralWidget(self.graphWidget)
#
#         hour = [1,2,3,4,5,6,7,8,9,10]
#         temperature = [30,32,34,32,33,31,29,32,35,45]
#
#         # plot data: x, y values
#         self.graphWidget.plot(hour, temperature)
#
#
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     main = MainWindow()
#     main.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()