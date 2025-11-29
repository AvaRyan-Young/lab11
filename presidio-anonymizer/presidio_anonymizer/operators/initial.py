from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    """Convert the entered name into initials"""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """returns the initials"""
        return self.return_initial(text)

    def validate(self, params: Dict = None) -> None:
        """Redact does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
    
    @staticmethod
    def return_initial(text: str):
        """Return the initials of the given name"""
        indWords = text.split()
        initialChar = ""
        for i in indWords:
            newChar = (i[0])
            print(newChar)
            while newChar.isalnum() == False:
                initialChar = initialChar + newChar
                newChar = (i[+1])
            initialChar = initialChar + newChar.capitalize() + ". "
        return initialChar[:-1]