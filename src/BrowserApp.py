import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt, QThread, pyqtSignal
from datetime import datetime

class DownloadThread(QThread):
    update_signal = pyqtSignal(int)
    finished_signal = pyqtSignal()

    def __init__(self, srcs, download_dir):
        super().__init__()
        self.srcs = srcs
        self.download_dir = download_dir
        self.is_running = True

    def run(self):
        for idx, src in enumerate(self.srcs):
            if not self.is_running:
                break
            if src:
                try:
                    response = requests.get(src)
                    if response.status_code == 200:
                        filename = os.path.join(self.download_dir, f'downloaded_image_{idx}.jpg')
                        with open(filename, 'wb') as f:
                            f.write(response.content)
                        self.update_signal.emit(idx + 1)  # Update progress dialog
                except Exception as e:
                    print(f"Error downloading image {idx}: {e}")
        self.finished_signal.emit()

    def stop(self):
        self.is_running = False

class BrowserApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)

        self.button = QPushButton('Download All Images')
        self.button.clicked.connect(self.download_images)
        self.layout.addWidget(self.button)

        self.browser.load(QUrl('http://realestate.com.au'))

    def download_images(self):
        unique_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.download_dir = os.path.join(os.getcwd(), f'images_{unique_id}')
        os.makedirs(self.download_dir, exist_ok=True)

        script = """
        var imgs = document.querySelectorAll('img');
        var srcs = [];
        for (var i = 0; i < imgs.length; i++) {
            srcs.push(imgs[i].src);
        }
        srcs;
        """
        self.browser.page().runJavaScript(script, self.start_download_thread)

    def start_download_thread(self, srcs):
        self.progress_dialog = QProgressDialog("Downloading images...", "Stop", 0, len(srcs), self)
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.canceled.connect(self.stop_download)
        self.progress_dialog.show()

        self.download_thread = DownloadThread(srcs, self.download_dir)
        self.download_thread.update_signal.connect(self.update_progress)
        self.download_thread.finished_signal.connect(self.download_finished)
        self.download_thread.start()

    def update_progress(self, value):
        self.progress_dialog.setValue(value)

    def stop_download(self):
        self.download_thread.stop()

    def download_finished(self):
        self.progress_dialog.setValue(self.progress_dialog.maximum())
        self.progress_dialog.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BrowserApp()
    ex.show()
    sys.exit(app.exec_())
