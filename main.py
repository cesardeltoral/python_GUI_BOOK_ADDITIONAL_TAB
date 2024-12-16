import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,QTabWidget,
                              QHBoxLayout, QLineEdit, QPushButton, QLabel, QListWidget, QTextEdit)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt


# Define the stylesheet
STYLE_SHEET = """
QMainWindow {
    background-color:rgb(240, 240, 240);
}

QTabWidget::pane {
    border: 1px solid #cccccc;
    background: white;
    border-radius: 4px;
}

QTabWidget::tab-bar {
    left: 5px;
}
QTabBar::tab {
    background: #e1e1e1;
    border: 1px solid #cccccc;
    padding: 8px 12px;
    margin-right: 2px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
}

QTabBar::tab:selected {
    background: white;
    border-bottom-color: white;
}
QLineEdit {
    padding: 8px;
    border: 1px solid #cccccc;
    border-radius: 4px;
    background-color: white;
}

QLineEdit:focus {
    border: 1px solid #4a90e2;
}

QPushButton {
    background-color: #4a90e2;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    min-width: 100px;
}

QPushButton:hover {
    background-color: #357abd;
}

QPushButton:pressed {
    background-color: #2d6da3;
}

QListWidget {
    border: 1px solid #cccccc;
    border-radius: 4px;
    background-color: white;
    padding: 5px;
}

QListWidget::item {
    padding: 8px;
    border-bottom: 1px solid #eeeeee;
}

QListWidget::item:selected {
    background-color: #4a90e2;
    color: #000000;
}

QTextEdit {
    border: 1px solid #cccccc;
    border-radius: 4px;
    background-color: white;
    padding: 5px;
}

QLabel {
    color: #333333;
    font-size: 14px;
}

"""

class BookManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Book Manager")
        self.setGeometry(600, 200, 800, 600)
        self.setWindowIcon(QIcon("book_picture.png"))

        # Apply the stylesheet
        self.setStyleSheet(STYLE_SHEET)
    
        app_font = QFont("Segoe UI", 10)
        QApplication.setFont(app_font)

        # Create the main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # Create tab widget
        self.tabs = QTabWidget()
        self.setup_search_tab()
        self.setup_details_tab()
        self.setup_recommendations_tab()

        layout.addWidget(self.tabs)

    def setup_search_tab(self):
        search_tab = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Search section
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter book title...")
        search_button = QPushButton("Search")
        search_button.setCursor(Qt.PointingHandCursor)
        search_button.clicked.connect(lambda: self.search_books())
        
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        layout.addLayout(search_layout)
        
        # Results section
        results_label = QLabel("Search Results:")
        results_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(results_label)
        
        self.results_list = QListWidget()
        layout.addWidget(self.results_list)
        
        # View Details button
        view_details_btn = QPushButton("View Details")
        view_details_btn.setCursor(Qt.PointingHandCursor)
        view_details_btn.clicked.connect(lambda: self.view_book_details())
        layout.addWidget(view_details_btn)
        
        search_tab.setLayout(layout)
        self.tabs.addTab(search_tab, "Book Search")
        
    def setup_details_tab(self):
        details_tab = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Book details section
        self.book_title_label = QLabel("Title: ")
        self.book_author_label = QLabel("Author: ")
        self.book_genre_label = QLabel("Genre: ")
        self.book_description = QTextEdit()
        self.book_description.setReadOnly(True)
        
        layout.addWidget(self.book_title_label)
        layout.addWidget(self.book_author_label)
        layout.addWidget(self.book_genre_label)
        layout.addWidget(QLabel("Description:"))
        layout.addWidget(self.book_description)
        
        # Get recommendations button
        recommend_btn = QPushButton("Get Recommendations")
        recommend_btn.setCursor(Qt.PointingHandCursor)
        recommend_btn.clicked.connect(lambda: self.get_recommendations())
        layout.addWidget(recommend_btn) 
        
        details_tab.setLayout(layout)
        self.tabs.addTab(details_tab, "Book Details")
        
    def setup_recommendations_tab(self):
        recommendations_tab = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        layout.addWidget(QLabel("Recommended Books:"))
        self.recommendations_list = QListWidget()
        layout.addWidget(self.recommendations_list)
        
        # Back to search button
        back_btn = QPushButton("Back to Search")
        back_btn.setCursor(Qt.PointingHandCursor)
        back_btn.clicked.connect(lambda: self.back_to_search())
        layout.addWidget(back_btn)
        
        recommendations_tab.setLayout(layout)
        self.tabs.addTab(recommendations_tab, "Recommendations")
    
    def search_books(self):
        print("search_books() called")
        # Placeholder function - would normally search a database
        search_term = self.search_input.text()
        self.results_list.clear()   
        # Adding dummy data
        dummy_books = [
            "The Great Gatsby - F. Scott Fitzgerald (Fiction)",
            "1984 - George Orwell (Science Fiction)",
            "Pride and Prejudice - Jane Austen (Romance)"
        ]
        self.results_list.addItems(dummy_books)
    
    def view_book_details(self):
        print("view_book_details() called")
        # Placeholder function - would normally fetch book details
        self.book_title_label.setText("Title: The Great Gatsby")
        self.book_author_label.setText("Author: F. Scott Fitzgerald")
        self.book_genre_label.setText("Genre: Fiction")
        self.book_description.setText("A story of decadence and excess...")
        self.tabs.setCurrentIndex(1)  # Switch to details tab
    
    def get_recommendations(self):
        print("get_recommendations() called")
        # Placeholder function - would normally generate recommendations
        self.recommendations_list.clear()
        dummy_recommendations = [
            "The Catcher in the Rye - J.D. Salinger",
            "To Kill a Mockingbird - Harper Lee",
            "The Old Man and the Sea - Ernest Hemingway"
        ]
        self.recommendations_list.addItems(dummy_recommendations)
        self.tabs.setCurrentIndex(2)  # Switch to recommendations tab
    
    def back_to_search(self):
        self.tabs.setCurrentIndex(0)
        print("back_to_search() called")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BookManagerApp()
    window.show()
    sys.exit(app.exec_())

