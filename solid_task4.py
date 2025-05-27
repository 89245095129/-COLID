# Задача 4. Принцип разделения интерфейса (ISP)
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_document(self, document):
        pass


class Scannable(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class Faxable(ABC):
    @abstractmethod
    def fax_document(self, document):
        pass


class Copyable(ABC):
    @abstractmethod
    def copy_document(self):
        pass


class SimplePrinter(Printable):
    def print_document(self, document):
        print(f"Printing: {document}")


class AllInOnePrinter(Printable, Scannable, Copyable):
    def print_document(self, document):
        print(f"Printing: {document}")
        
    def scan_document(self):
        print("Scanning document...")
        
    def copy_document(self):
        print("Copying document...")