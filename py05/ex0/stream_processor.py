from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """
    Abstract base class defining the common processing interface.

    Provides template for data processing with validation and formatting.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the data and return result string.

        Args:
            data: Input data to be processed

        Returns:
            Formatted string with processing results
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate if data is appropriate for this processor.

        Args:
            data: Input data to validate

        Returns:
            True if data is valid, False otherwise
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Format the output string with default implementation.

        Args:
            result: Processing result to format

        Returns:
            Formatted output string with "Output: " prefix
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Specialized processor for numeric data.

    Handles lists of numbers with statistical analysis including
    sum and average calculations.
    """

    def validate(self, data: Any) -> bool:
        """
        Validate if data is a list of numbers.

        Args:
            data: Input data to validate

        Returns:
            True if data is a list of int or float, False otherwise
        """
        if not isinstance(data, list):
            return False
        return all(isinstance(item, (int, float)) for item in data)

    def process(self, data: Any) -> str:
        """
        Process numeric data and return formatted result.

        Args:
            data: List of numeric values to process

        Returns:
            Formatted string with count, sum, and average
        """
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")

            print("Validation: Numeric data verified")
            count = len(data)
            total = sum(data)
            average = total / count if count > 0 else 0
            result = f"Processed {count} numeric values, \
sum={total}, avg={average}"
            return self.format_output(result)
        except Exception as e:
            re = self.format_output(f"Error processing numeric data: {str(e)}")
            return re


class TextProcessor(DataProcessor):
    """
    Specialized processor for text data.

    Analyzes text strings with character and word counting.
    """

    def validate(self, data: Any) -> bool:
        """
        Validate if data is a string.

        Args:
            data: Input data to validate

        Returns:
            True if data is a string, False otherwise
        """
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        """
        Process text data and return formatted result.

        Args:
            data: Text string to analyze

        Returns:
            Formatted string with character and word counts
        """
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")

            print("Validation: Text data verified")
            char_count = len(data)
            word_count = len(data.split())
            result = f"Processed text: \
{char_count} characters, {word_count} words"
            return self.format_output(result)
        except Exception as e:
            return self.format_output(f"Error processing text data: {str(e)}")


class LogProcessor(DataProcessor):
    """
    Specialized processor for log entries.

    Parses log messages and categorizes by severity level
    (ERROR, WARN, INFO, DEBUG).
    """

    def validate(self, data: Any) -> bool:
        """
        Validate if data is a log entry string.

        Args:
            data: Input data to validate

        Returns:
            True if string contains valid log level, False otherwise
        """
        if not isinstance(data, str):
            return False
        log_levels = ["ERROR", "WARN", "INFO", "DEBUG"]
        return any(level in data for level in log_levels)

    def process(self, data: Any) -> str:
        """
        Process log data and return formatted result.

        Args:
            data: Log entry string with severity level

        Returns:
            Formatted string with prefix and extracted message
        """
        try:
            if not self.validate(data):
                raise ValueError("Invalid log data")

            print("Validation: Log entry verified")

            if "ERROR" in data:
                level = "ERROR"
                prefix = "[ALERT]"
            elif "WARN" in data:
                level = "WARN"
                prefix = "[WARNING]"
            elif "INFO" in data:
                level = "INFO"
                prefix = "[INFO]"
            else:
                level = "DEBUG"
                prefix = "[DEBUG]"

            parts = data.split(":", 1)
            message = parts[1].strip() if len(parts) > 1 else data

            result = f"{prefix} {level} level detected: {message}"
            return self.format_output(result)
        except Exception as e:
            return self.format_output(f"Error processing log data: {str(e)}")


def main():
    """
    Demonstrate polymorphic data processor system.

    Shows usage of different processor types with unified interface.
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    numeric_processor = NumericProcessor()
    print("Processing data: [1, 2, 3, 4, 5]")
    print(numeric_processor.process([1, 2, 3, 4, 5]))

    print("\nInitializing Text Processor...")
    text_processor = TextProcessor()
    print('Processing data: "Hello Nexus World"')
    print(text_processor.process("Hello Nexus World"))

    print("\nInitializing Log Processor...")
    log_processor = LogProcessor()
    print('Processing data: "ERROR: Connection timeout"')
    print(log_processor.process("ERROR: Connection timeout"))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    test_data = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready"
    ]

    for i, (processor, data) in enumerate(zip(processors, test_data), 1):
        result = processor.process(data)
        result_text = result.replace("Output: ", "")
        print(f"Result {i}: {result_text}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
