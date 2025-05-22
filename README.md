🚀 Nitron Browser

A modern, lightweight web browser built using Python's PyQt5 library.
This browser provides a clean, intuitive interface with essential web browsing features including tabbed browsing, bookmarks, and customizable themes.
Perfect for users who want a simple, fast browsing experience with both dark and light mode support.

⭐ Features


💻 Clean and modern PyQt5-based GUI
🗂️ Tabbed browsing with easy tab management
🎯 Smart URL bar - supports both URLs and search queries
💾 Bookmark system for saving favorite websites
🎨 Dark/Light mode toggle for comfortable browsing
🏡 Home button with customizable homepage
🧭 Fast navigation with back, forward, and reload buttons
🔎 Integrated search using Brave Search engine
🌍 Cross-platform - runs on Windows, macOS, and Linux


📋 Project Structure
Nitron-Browser/
│
├── browser.py             # Main Python script with browser logic
├── icons/                 # SVG icons for toolbar buttons
│   ├── back.svg
│   ├── forward.svg
│   ├── reload.svg
│   ├── home.svg
│   ├── new-tab.svg
│   ├── bookmark.svg
│   ├── bookmarks-list.svg
│   └── dark-mode.svg
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
└── screenshots/           # Folder for storing UI screenshots
    ├── nitron_dark_mode.png
    ├── nitron_light_mode.png
    └── tab_management.png

🛠️ Installation
1️⃣ Clone the repository
bashgit clone https://github.com/your-username/Nitron-Browser.git
cd Nitron-Browser
2️⃣ Create a virtual environment (recommended)
bashpython -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3️⃣ Install dependencies
bashpip install -r requirements.txt
Or install manually:
bashpip install PyQt5 PyQtWebEngine
4️⃣ Create the icons directory
Create an icons folder and add the required SVG icon files:
bashmkdir icons
# Add the required SVG files to the icons directory

💡 Note: You can download free SVG icons from Feather Icons, Heroicons, or create your own simple SVG icons.


⚡ How to Run
bashpython browser.py

⚙️ Configuration
🏠 Change Default Homepage
Edit the default_homepage variable in browser.py:
pythonself.default_homepage = "https://your-preferred-homepage.com"
🔍 Change Default Search Engine
Modify the search URL in the navigate_to_url method:
pythonurl = f"https://your-search-engine.com/search?q={query.decode()}"
The browser uses Brave Search by default for enhanced privacy.

🚧 Future Improvements
FeatureStatusDescription📥 Download Manager🔜 PlannedBuilt-in download management system📜 History🔜 PlannedBrowsing history with search functionality🎛️ Settings Panel🔜 PlannedComprehensive settings and preferences🧩 Extensions Support🔜 PlannedPlugin system for additional features🕵️ Private Browsing🔜 PlannedIncognito mode for private sessions🖥️ Full-screen Mode🔜 PlannedDistraction-free browsing experience⌨️ Keyboard Shortcuts🔜 PlannedCustomizable hotkeys for power users

📦 Dependencies

PyQt5 – Modern GUI framework for Python
PyQtWebEngine – Web engine integration for PyQt5

You can install everything with:
bashpip install -r requirements.txt
💻 System Requirements

Python: 3.6 or higher
Operating System: Windows, macOS, or Linux
Memory: 512MB RAM minimum (1GB recommended)
Storage: 100MB free space


🌐 Platform-Specific Installation
🪟 Windows
bashpip install PyQt5 PyQtWebEngine
🍎 macOS
bashpip3 install PyQt5 PyQtWebEngine
# Additional dependencies might be needed:
brew install python-tk
🐧 Linux (Ubuntu/Debian)
bashsudo apt update
sudo apt install python3-pip python3-pyqt5 python3-pyqt5.qtwebengine
pip3 install PyQt5 PyQtWebEngine
🐧 Linux (Fedora/RHEL)
bashsudo dnf install python3-pip python3-qt5 python3-qt5-webengine
pip3 install PyQt5 PyQtWebEngine

🤝 Contributing
Contributions are welcome! Here's how you can help:

🍴 Fork this repository
🌿 Create your feature branch (git checkout -b feature/amazing-feature)
💾 Commit your changes (git commit -m 'Add some amazing feature')
📤 Push to the branch (git push origin feature/amazing-feature)
🔀 Open a Pull Request

You can also open issues if you find any problems or have suggestions.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

👨‍💻 Author
Developed by Your Name.
For queries or collaborations, feel free to open an issue or connect via GitHub.

<p align="center">
  <sub>🌟 Browse the web with style and simplicity. 🌐</sub>
</p>
