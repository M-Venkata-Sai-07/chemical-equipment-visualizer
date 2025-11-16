import sys
import traceback
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QFileDialog, QLabel, QListWidget, QMessageBox, QSplitter
)
from PyQt5 import QtCore

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

import api_handler

class Chart(Canvas):
    def __init__(self):
        fig = Figure(figsize=(5, 4), tight_layout=True)
        self.ax = fig.add_subplot(111)
        super().__init__(fig)

    def plot_distribution(self, dist: dict):
        self.ax.clear()
        if not dist:
            self.ax.text(0.5, 0.5, "No data", ha="center")
            self.draw()
            return

        labels = list(dist.keys())
        values = list(dist.values())
        self.ax.bar(labels, values)
        self.ax.set_title("Equipment Type Distribution")
        self.ax.set_ylabel("Count")
        self.ax.set_xlabel("Type")
        self.draw()

class DesktopApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer - Desktop")
        self.resize(900, 600)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Top buttons
        top = QHBoxLayout()
        self.btn_upload = QPushButton("Upload CSV")
        self.btn_refresh = QPushButton("Refresh History")
        self.btn_pdf = QPushButton("Download PDF")
        self.status = QLabel("Status: Ready")

        top.addWidget(self.btn_upload)
        top.addWidget(self.btn_refresh)
        top.addWidget(self.btn_pdf)
        top.addStretch()
        top.addWidget(self.status)
        layout.addLayout(top)

        # Split view
        split = QSplitter(QtCore.Qt.Horizontal)
        layout.addWidget(split)

        # History panel
        self.history_list = QListWidget()
        left = QWidget()
        left_layout = QVBoxLayout()
        left.setLayout(left_layout)
        left_layout.addWidget(QLabel("History (last 5 uploads):"))
        left_layout.addWidget(self.history_list)

        # Detail panel
        right = QWidget()
        right_layout = QVBoxLayout()
        right.setLayout(right_layout)

        self.summary = QLabel("Summary will appear here")
        self.summary.setWordWrap(True)

        self.chart = Chart()

        right_layout.addWidget(self.summary)
        right_layout.addWidget(self.chart)

        split.addWidget(left)
        split.addWidget(right)

        # Connect actions
        self.btn_upload.clicked.connect(self.upload_csv)
        self.btn_refresh.clicked.connect(self.load_history)
        self.btn_pdf.clicked.connect(self.download_pdf)
        self.history_list.itemClicked.connect(self.history_selected)

        # initial load
        self.load_history()

    def set_status(self, msg):
        self.status.setText(f"Status: {msg}")

    def upload_csv(self):
        try:
            path, _ = QFileDialog.getOpenFileName(self, "Choose CSV", filter="CSV (*.csv)")
            if not path:
                return

            self.set_status("Uploading…")
            data = api_handler.upload_file(path)
            QMessageBox.information(self, "Uploaded", "CSV uploaded successfully.")
            self.set_status("Done.")

            self.show_summary(data)
            self.load_history()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            traceback.print_exc()

    def load_history(self):
        try:
            self.set_status("Loading history...")
            history = api_handler.get_history()
            self.history_list.clear()

            for item in history:
                self.history_list.addItem(f"{item['id']}: {item['file_name']}")

            self.set_status("History loaded.")

            if history:
                self.show_summary(history[0]["summary"])
                self.chart.plot_distribution(history[0]["summary"]["type_distribution"])

        except Exception as e:
            QMessageBox.critical(self, "Error", "Backend is not running!")
            traceback.print_exc()

    def history_selected(self, item):
        try:
            id_ = int(item.text().split(":")[0])
            history = api_handler.get_history()

            for h in history:
                if h["id"] == id_:
                    self.show_summary(h["summary"])
                    self.chart.plot_distribution(h["summary"]["type_distribution"])
                    break

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show_summary(self, summary):
        txt = (
            f"Total Records: {summary['total_records']}\n"
            f"Avg Flowrate: {summary['avg_flowrate']}\n"
            f"Avg Pressure: {summary['avg_pressure']}\n"
            f"Avg Temperature: {summary['avg_temperature']}\n\n"
            f"Type Distribution:\n"
        )
        for k, v in summary["type_distribution"].items():
            txt += f"  {k}: {v}\n"

        self.summary.setText(txt)

    def download_pdf(self):
        try:
            item = self.history_list.currentItem()
            if not item:
                QMessageBox.warning(self, "Select item", "Please select a dataset.")
                return

            id_ = int(item.text().split(":")[0])
            save_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", f"report_{id_}.pdf", filter="PDF (*.pdf)")
            if not save_path:
                return

            self.set_status("Downloading PDF...")
            api_handler.download_report(id_, save_path)
            self.set_status("PDF saved.")
            QMessageBox.information(self, "Saved", f"PDF saved to:\n{save_path}")

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DesktopApp()
    w.show()
    sys.exit(app.exec_())
