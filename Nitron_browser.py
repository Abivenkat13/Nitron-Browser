import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLineEdit, QWidget,
    QToolBar, QAction, QTabWidget, QMessageBox
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon
import os


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nitron Browser")
        self.setGeometry(100, 100, 1200, 800)

        self.default_homepage = "https://search.brave.com"
        self.dark_mode_enabled = False
        self.bookmarks = []

        self.apply_styles()

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_url_bar_for_tab)

        self.add_new_tab(self.default_homepage, "Home")

        self.nav_toolbar = QToolBar("Navigation")
        self.addToolBar(self.nav_toolbar)
        self.nav_toolbar.setIconSize(QSize(24, 24))

        self.add_navigation_buttons()

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def icon_path(self, filename):
        # Helper to get absolute path of icon files
        return os.path.join(os.path.dirname(__file__), "icons", filename)

    def add_navigation_buttons(self):
        buttons = [
            (self.icon_path("back.svg"), lambda: self.current_tab().back(), "Back"),
            (self.icon_path("forward.svg"), lambda: self.current_tab().forward(), "Forward"),
            (self.icon_path("reload.svg"), lambda: self.current_tab().reload(), "Reload"),
            (self.icon_path("home.svg"), self.navigate_to_home, "Home"),
            (self.icon_path("new-tab.svg"), lambda: self.add_new_tab(self.default_homepage, "New Tab"), "New Tab"),
            (self.icon_path("bookmark.svg"), self.add_bookmark, "Bookmark"),
            (self.icon_path("bookmarks-list.svg"), self.view_bookmarks, "View Bookmarks"),
            (self.icon_path("dark-mode.svg"), self.toggle_dark_mode, "Toggle Dark Mode"),
        ]

        for icon_file, action, tooltip in buttons:
            icon = QIcon(icon_file)
            btn = QAction(icon, tooltip, self)
            btn.triggered.connect(action)
            self.nav_toolbar.addAction(btn)

    def add_new_tab(self, url, title):
        browser = QWebEngineView()
        browser.setUrl(QUrl(url))

        # Removed loadStarted, loadProgress, loadFinished connections

        browser.urlChanged.connect(self.update_tab_title)

        url_bar = QLineEdit()
        url_bar.setPlaceholderText("Enter URL or search term and press Enter")
        url_bar.returnPressed.connect(lambda: self.navigate_to_url(url_bar, browser))

        tab_layout = QVBoxLayout()
        tab_layout.setContentsMargins(0, 0, 0, 0)
        tab_layout.setSpacing(0)
        tab_layout.addWidget(url_bar)
        tab_layout.addWidget(browser)

        tab_container = QWidget()
        tab_container.setLayout(tab_layout)

        self.tabs.addTab(tab_container, title)
        self.tabs.setCurrentWidget(tab_container)

    def current_tab(self):
        current_tab_container = self.tabs.currentWidget()
        if current_tab_container:
            return current_tab_container.layout().itemAt(1).widget()
        return None

    def current_url_bar(self):
        current_tab_container = self.tabs.currentWidget()
        if current_tab_container:
            return current_tab_container.layout().itemAt(0).widget()
        return None

    def navigate_to_url(self, url_bar, browser):
        text = url_bar.text().strip()
        if not text:
            return

        if " " in text or "." not in text:
            query = QUrl.toPercentEncoding(text)
            url = f"https://search.brave.com/search?q={query.decode()}"
        else:
            if not text.startswith(("http://", "https://")):
                text = "https://" + text
            url = text

        browser.setUrl(QUrl(url))

    def navigate_to_home(self):
        self.current_tab().setUrl(QUrl(self.default_homepage))
        self.current_url_bar().setText(self.default_homepage)

    def update_tab_title(self, url):
        current_tab_index = self.tabs.currentIndex()
        host = url.host()
        if host:
            self.tabs.setTabText(current_tab_index, host)
            if self.sender() == self.current_tab():
                url_bar = self.current_url_bar()
                if url_bar:
                    url_bar.setText(url.toString())

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.close()

    def toggle_dark_mode(self):
        if self.dark_mode_enabled:
            self.set_light_mode()
            self.dark_mode_enabled = False
        else:
            self.set_dark_mode()
            self.dark_mode_enabled = True

    def set_dark_mode(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #282828; color: white; }
            QToolBar { background-color: #333333; border: none; padding: 6px; }
            QToolBar QToolButton {
                color: white; background: transparent; border: none; padding: 5px; font-size: 14px;
            }
            QToolBar QToolButton:hover { color: #00bfff; }
            QTabWidget::pane { background-color: #333333; border: none; }
            QTabBar::tab {
                background: #3c3c3c; border-radius: 6px; padding: 12px; margin: 2px; color: white;
            }
            QTabBar::tab:selected { background: #4c4c4c; border: 1px solid #5c5c5c; }
            QTabBar::tab:hover { background: #444444; color: white; }
            QLineEdit {
                background-color: #3c3c3c; border: none; border-radius: 6px; color: white; padding: 8px;
            }
        """)

    def set_light_mode(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #f2f2f2; color: black; }
            QToolBar { background-color: #e0e0e0; border: none; padding: 6px; }
            QToolBar QToolButton {
                color: black; background: transparent; border: none; padding: 5px; font-size: 14px;
            }
            QToolBar QToolButton:hover { color: #0078d7; }
            QTabWidget::pane { background-color: #e0e0e0; border: none; }
            QTabBar::tab {
                background: #d0d0d0; border-radius: 6px; padding: 12px; margin: 2px; color: black;
            }
            QTabBar::tab:selected { background: #c0c0c0; border: 1px solid #b0b0b0; }
            QTabBar::tab:hover { background: #b0b0b0; color: black; }
            QLineEdit {
                background-color: #ffffff; border: none; border-radius: 6px; color: black; padding: 8px;
            }
        """)

    def add_bookmark(self):
        current_url = self.current_tab().url().toString()
        if current_url not in self.bookmarks:
            self.bookmarks.append(current_url)
            QMessageBox.information(self, "Bookmark Added", f"Bookmarked: {current_url}")
        else:
            QMessageBox.information(self, "Bookmark", "This page is already bookmarked.")

    def view_bookmarks(self):
        if not self.bookmarks:
            QMessageBox.information(self, "Bookmarks", "No bookmarks yet.")
            return
        bookmarks_list = "\n".join(self.bookmarks)
        QMessageBox.information(self, "Bookmarks", f"Your bookmarks:\n{bookmarks_list}")

    def update_url_bar_for_tab(self, index):
        url_bar = self.current_url_bar()
        if url_bar:
            browser = self.current_tab()
            if browser:
                url_bar.setText(browser.url().toString())

    def apply_styles(self):
        self.set_dark_mode()  # Load with dark mode by default


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
