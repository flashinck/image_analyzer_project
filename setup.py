from setuptools import setup, find_packages

setup(
    name="image-analyzer",
    version="1.0.0",
    author="Владислав",
    description="Программа для анализа изображений с использованием ИНС",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "tensorflow>=2.10.0",
        "torch>=1.13.0",
        "opencv-python>=4.7.0",
        "Pillow>=9.0.0",
        "numpy>=1.24.0",
        "PyQt5>=5.15.0",
        "requests>=2.28.0"
    ],
    python_requires=">=3.10",
)