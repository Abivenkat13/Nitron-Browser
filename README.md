# 🌐 Nitron Browser

A modern, lightweight web browser built with Python and PyQt5, featuring a clean interface, tabbed browsing, and essential web navigation tools.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## ✨ Features

- **🗂️ Tabbed Browsing** - Multiple tabs with easy navigation
- **🔍 Smart Search** - Integrated search using Brave Search engine
- **📑 Bookmarks** - Save and manage your favorite websites
- **🌙 Dark/Light Mode** - Toggle between themes for comfortable browsing
- **🏠 Home Page** - Quick access to your default homepage
- **⚡ Fast Navigation** - Back, forward, reload, and home buttons
- **📱 Modern UI** - Clean, intuitive interface with rounded corners and smooth styling

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the repository:**
   ```bash
   git clone <your-repository-url>
   cd nitron-browser
   ```

2. **Install required dependencies:**
   ```bash
   pip install PyQt5 PyQtWebEngine
   ```

3. **Create the icons directory structure:**
   ```
   nitron-browser/
   ├── browser.py
   └── icons/
       ├── back.svg
       ├── forward.svg
       ├── reload.svg
       ├── home.svg
       ├── new-tab.svg
       ├── bookmark.svg
       ├── bookmarks-list.svg
       └── dark-mode.svg
   ```

4. **Run the browser:**
   ```bash
   python browser.py
   ```

## 📁 Project Structure

```
nitron-browser/
├── browser.py              # Main browser application
├── icons/                  # Navigation icons (SVG format)
│   ├── back.svg
│   ├── forward.svg
│   ├── reload.svg
│   ├── home.svg
│   ├── new-tab.svg
│   ├── bookmark.svg
│   ├── bookmarks-list.svg
│   └── dark-mode.svg
└── README.md              # This file
```

## 🎯 Usage

### Basic Navigation
- **New Tab**: Click the "+" icon or use the new tab button
- **Close Tab**: Click the "×" on any tab (browser closes if only one tab remains)
- **Navigate**: Use back/forward buttons or enter URLs in the address bar
- **Search**: Type search terms in the address bar (uses Brave Search)
- **Home**: Click the home button to return to the default homepage

### Bookmarks
- **Add Bookmark**: Click the bookmark icon to save the current page
- **View Bookmarks**: Click the bookmarks list icon to see all saved bookmarks

### Themes
- **Toggle Dark/Light Mode**: Click the theme toggle button in the toolbar

## ⚙️ Configuration

### Default Homepage
The browser uses `https://search.brave.com` as the default homepage. To change this, modify the `default_homepage` variable in the `Browser` class:

```python
self.default_homepage = "https://your-preferred-homepage.com"
```

### Custom Styling
The browser includes custom CSS styling for both dark and light modes. You can modify the `set_dark_mode()` and `set_light_mode()` methods to customize the appearance.

## 🛠️ Technical Details

### Built With
- **Python** - Core programming language
- **PyQt5** - GUI framework
- **QtWebEngine** - Web rendering engine
- **Brave Search** - Default search engine

### Key Components
- `QMainWindow` - Main browser window
- `QTabWidget` - Tab management
- `QWebEngineView` - Web page rendering
- `QToolBar` - Navigation controls
- `QLineEdit` - Address bar

## 🐛 Troubleshooting

### Common Issues

**1. Import Error: No module named 'PyQt5'**
```bash
pip install PyQt5 PyQtWebEngine
```

**2. Icons not displaying**
- Ensure the `icons/` directory exists in the same folder as `browser.py`
- Verify all required SVG icon files are present

**3. Web pages not loading**
- Check your internet connection
- Ensure QtWebEngine is properly installed
- Try running with administrator privileges if needed

**4. Browser crashes on startup**
- Update PyQt5 to the latest version
- Check Python version compatibility (3.7+)

## 🔧 Development

### Adding New Features
The browser is designed with modularity in mind. Key areas for extension:

- **Plugins**: Add new toolbar buttons in `add_navigation_buttons()`
- **Settings**: Extend configuration options
- **History**: Implement browsing history functionality
- **Downloads**: Add download management

### Code Structure
- Navigation logic is centralized in navigation methods
- UI styling is separated into theme methods
- Tab management is handled through Qt's tab widget system

## 📋 Requirements

```
PyQt5>=5.15.0
PyQtWebEngine>=5.15.0
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

                    


---

**Made with ❤️ using Python and PyQt5**
