from abc import ABC, abstractmethod

# Those classes violates the interface segregation principle (ISP). Because the parent class force method the child class doesn't supported.
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass
    
    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, docoument):
        print(f"Printing {docoument} in black and white...")
    
    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")
    
    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")


class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")
    
    def fax(self, document):
        print(f"Faxing {document}...")
        
    def scan(self, document):
        print(f"Scanning {document}...")


"-------------------------------"
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")


class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")
    
    def scan(self, document):
        print(f"Scanning {document}")
