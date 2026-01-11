import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from src.analysis.analyzer import ImageAnalyzer
from src.storage.database import AnalysisDatabase

class AnalysisWorker(QThread):
    '''Рабочий поток для анализа'''
    finished = pyqtSignal(dict)
    error = pyqtSignal(str)
    
    def __init__(self, analyzer, image_path):
        super().__init__()
        self.analyzer = analyzer
        self.image_path = image_path
    
    def run(self):
        try:
            result = self.analyzer.analyze(self.image_path)
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))


class ImageAnalyzerGUI(QtWidgets.QMainWindow):
    '''Главное окно приложения'''
    
    def __init__(self):
        super().__init__()
        self.analyzer = ImageAnalyzer()
        self.db = AnalysisDatabase()
        self.current_analysis = None
        self.init_ui()
    
    def init_ui(self):
        '''Инициализация интерфейса'''
        self.setWindowTitle("Image Analyzer - Анализ изображений")
        self.setGeometry(100, 100, 1200, 800)
        
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QtWidgets.QHBoxLayout()
        
        left_panel = self._create_left_panel()
        main_layout.addWidget(left_panel, 1)
        
        right_panel = self._create_right_panel()
        main_layout.addWidget(right_panel, 2)
        
        central_widget.setLayout(main_layout)
        self._create_menu()
    
    def _create_left_panel(self):
        '''Создать левую панель'''
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        self.image_label = QtWidgets.QLabel("Загрузите изображение")
        self.image_label.setMinimumSize(300, 300)
        self.image_label.setStyleSheet("border: 2px dashed #ccc; background-color: #f5f5f5;")
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)
        
        button_layout = QtWidgets.QVBoxLayout()
        
        load_button = QtWidgets.QPushButton("Загрузить изображение")
        load_button.clicked.connect(self.load_image)
        button_layout.addWidget(load_button)
        
        self.model_combo = QtWidgets.QComboBox()
        self.model_combo.addItems(['ResNet50', 'VGG16', 'EfficientNetB0'])
        button_layout.addWidget(QtWidgets.QLabel("Модель:"))
        button_layout.addWidget(self.model_combo)
        
        self.device_combo = QtWidgets.QComboBox()
        self.device_combo.addItems(['CPU', 'GPU'])
        button_layout.addWidget(QtWidgets.QLabel("Устройство:"))
        button_layout.addWidget(self.device_combo)
        
        self.analyze_button = QtWidgets.QPushButton("Анализировать")
        self.analyze_button.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        self.analyze_button.clicked.connect(self.analyze_image)
        self.analyze_button.setEnabled(False)
        button_layout.addWidget(self.analyze_button)
        
        layout.addLayout(button_layout)
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def _create_right_panel(self):
        '''Создать правую панель'''
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        results_group = QtWidgets.QGroupBox("Результаты анализа")
        results_layout = QtWidgets.QVBoxLayout()
        
        self.top1_label = QtWidgets.QLabel("Ожидание анализа...")
        results_layout.addWidget(self.top1_label)
        
        self.results_table = QtWidgets.QTableWidget()
        self.results_table.setColumnCount(2)
        self.results_table.setHorizontalHeaderLabels(['Класс', 'Вероятность (%)'])
        results_layout.addWidget(self.results_table)
        
        results_group.setLayout(results_layout)
        layout.addWidget(results_group)
        
        widget.setLayout(layout)
        return widget
    
    def load_image(self):
        '''Загрузить изображение из файла'''
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выбрать изображение", "", "Images (*.jpg *.jpeg *.png *.bmp *.webp)"
        )
        
        if file_path:
            self.current_image_path = file_path
            pixmap = QPixmap(file_path)
            scaled_pixmap = pixmap.scaledToWidth(280)
            self.image_label.setPixmap(scaled_pixmap)
            self.analyze_button.setEnabled(True)
    
    def analyze_image(self):
        '''Анализировать загруженное изображение'''
        if not hasattr(self, 'current_image_path'):
            return
        
        model_name = self.model_combo.currentText()
        self.analyzer = ImageAnalyzer(model_name)
        self.analyzer.model.set_device(self.device_combo.currentText())
        
        self.worker = AnalysisWorker(self.analyzer, self.current_image_path)
        self.worker.finished.connect(self.on_analysis_finished)
        self.worker.error.connect(self.on_analysis_error)
        
        self.analyze_button.setEnabled(False)
        self.analyze_button.setText("Анализирование...")
        self.worker.start()
    
    def on_analysis_finished(self, result: dict):
        '''Обработать завершение анализа'''
        self.current_analysis = result
        
        top1 = result['predictions']
        self.top1_label.setText(
            f"Класс: {top1['class']} | Уверенность: {top1['percentage']:.2f}% | Время: {result['inference_time']*1000:.0f} мс"
        )
        
        self.results_table.setRowCount(0)
        for pred in result['predictions']:
            row = self.results_table.rowCount()
            self.results_table.insertRow(row)
            self.results_table.setItem(row, 0, QtWidgets.QTableWidgetItem(pred['class']))
            self.results_table.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{pred['percentage']:.2f}%"))
        
        self.db.save_analysis(result)
        
        self.analyze_button.setEnabled(True)
        self.analyze_button.setText("Анализировать")
    
    def on_analysis_error(self, error: str):
        '''Обработать ошибку анализа'''
        QtWidgets.QMessageBox.critical(self, "Ошибка анализа", error)
        self.analyze_button.setEnabled(True)
        self.analyze_button.setText("Анализировать")
    
    def _create_menu(self):
        '''Создать главное меню'''
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu("Файл")
        exit_action = file_menu.addAction("Выход")
        exit_action.triggered.connect(self.close)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = ImageAnalyzerGUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
