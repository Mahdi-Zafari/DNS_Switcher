from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
import subprocess
import ctypes
import json
import sys
import os

from ui.app_ui import Ui_Main

# =====  main app  ===== #
class win_main(QMainWindow, Ui_Main):
    def __init__(self):
        super(win_main, self).__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon(":/img/img/DNSS_logo.png"))
        self.setWindowTitle("DNS Switcher")

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.draggable = False

        self.load_dns_config()

        self.Button_exit.clicked.connect(self.close_program)
        self.btn_set_or_automatic.clicked.connect(self.toggle_dns)

        self.check_dns_status()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_dns_status)
        self.timer.start(10000)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and event.pos() in self.widget_top.rect():
            self.draggable = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.draggable:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False

    def close_program(self):
        """Close the application."""
        self.close()

    def is_admin(self):
        """Check if the script is running with administrator privileges."""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def load_dns_config(self):
        """Load DNS configuration from a JSON file."""
        config_path = os.path.join(os.path.dirname(__file__), 'config', 'dns.config.json')
        if not os.path.isfile(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, 'r') as config_file:
            config = json.load(config_file)

        self.preferred_dns = config.get("preferred_dns", "8.8.8.8")
        self.alternate_dns = config.get("alternate_dns", "8.8.4.4")

    def check_dns_status(self):
        """Check current DNS status and update UI accordingly."""
        try:
            result = subprocess.run(["netsh", "interface", "ipv4", "show", "dns"], capture_output=True, text=True, check=True)
            if self.preferred_dns in result.stdout:
                self.label_stats.setText("DNS Set")
                self.btn_set_or_automatic.setText("Revert to Automatic")
            else:
                self.label_stats.setText("DNS Automatic")
                self.btn_set_or_automatic.setText("Set DNS")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", "Failed to check DNS: " + str(e))

    def set_dns(self):
        """Set the DNS addresses."""
        try:
            subprocess.run(["netsh", "interface", "ipv4", "set", "dns", "name=\"Wi-Fi\"", "source=static", "address=" + self.preferred_dns], check=True)
            subprocess.run(["netsh", "interface", "ipv4", "add", "dns", "name=\"Wi-Fi\"", "address=" + self.alternate_dns, "index=2"], check=True)
            self.label_stats.setText("DNS Set")
            self.btn_set_or_automatic.setText("Revert to Automatic")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", "Failed to set DNS: " + str(e))

    def remove_dns(self):
        """Revert DNS to automatic (DHCP)."""
        try:
            subprocess.run(["netsh", "interface", "ipv4", "set", "dns", "name=\"Wi-Fi\"", "source=dhcp"], check=True)
            self.label_stats.setText("DNS Automatic")
            self.btn_set_or_automatic.setText("Set DNS")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", "Failed to revert DNS: " + str(e))

    def toggle_dns(self):
        """Toggle between setting and removing DNS."""
        if self.is_admin():
            if self.label_stats.text() == "DNS Automatic":
                self.set_dns()
            else:
                self.remove_dns()
        else:
            QMessageBox.warning(self, "Admin Access", "This operation requires administrator privileges.")

def main():
    app = QApplication(sys.argv)
    window = win_main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
