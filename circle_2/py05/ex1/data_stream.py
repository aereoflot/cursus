from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional


class DataStream(ABC):
    """
    Abstract base class for data stream processing.

    Provides common interface for batch processing, filtering,
    and statistics gathering across different data stream types.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize data stream with unique identifier.

        Args:
            stream_id: Unique identifier for this stream
        """
        self.stream_id = stream_id
        self.processed_count = 0
        self.total_items = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data and return result.

        Args:
            data_batch: List of data items to process

        Returns:
            String describing the processing results
        """
        pass

    @abstractmethod
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Filter data batch based on criteria.

        Args:
            data_batch: List of data items to filter
            criteria: Optional filtering criteria

        Returns:
            Filtered list of data items
        """
        pass

    def get_stats(self) -> Dict[str, Any]:
        """
        Get processing statistics for this stream.

        Returns:
            Dictionary with stream ID, processed count, and total items
        """
        return {
            "stream_id": self.stream_id,
            "processed_batches": self.processed_count,
            "total_items": self.total_items
        }


class SensorStream(DataStream):
    """
    Specialized stream for environmental sensor data processing.

    Handles temperature, humidity, and pressure readings with
    statistical analysis and threshold filtering.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize sensor stream with temperature tracking.

        Args:
            stream_id: Unique identifier for this sensor stream
        """
        super().__init__(stream_id)
        self.sensor_type = "Environmental Sensors"
        self.total_temperature = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process batch of sensor readings with statistical analysis.

        Args:
            data_batch: List of sensor reading values or dictionaries

        Returns:
            String with batch size and average temperature
        """
        try:
            self.processed_count += 1
            self.total_items += len(data_batch)

            count = len(data_batch)
            temps = []

            for item in data_batch:
                if isinstance(item, dict) and "temp" in item:
                    temps.append(item["temp"])
                elif isinstance(item, (int, float)):
                    temps.append(item)

            if temps:
                avg_temp = sum(temps) / len(temps)
                self.total_temperature += avg_temp
                return f"Sensor batch processed: {count} readings, \
avg temp: {avg_temp:.1f}°C"
            else:
                return f"Sensor batch processed: {count} readings"
        except Exception as e:
            return f"Error processing sensor batch: {str(e)}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Filter sensor data for high-priority temperature alerts.

        Args:
            data_batch: List of sensor readings
            criteria: Filter criteria ('high-priority' for temp > 30°C)

        Returns:
            List of critical temperature readings above 30°C
        """
        if criteria == "high-priority":
            filtered = []
            for item in data_batch:
                temp = None
                if isinstance(item, dict) and "temp" in item:
                    temp = item["temp"]
                elif isinstance(item, (int, float)):
                    temp = item

                if temp is not None and temp > 30:
                    filtered.append(item)
            return filtered
        return data_batch


class TransactionStream(DataStream):
    """
    Specialized stream for financial transaction processing.

    Handles buy and sell operations with net flow calculation
    and transaction volume tracking.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize transaction stream with financial tracking.

        Args:
            stream_id: Unique identifier for this transaction stream
        """
        super().__init__(stream_id)
        self.transaction_type = "Financial Data"
        self.net_flow = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process batch of financial transactions and calculate net flow.

        Args:
            data_batch: List of transaction dictionaries with type
                        and amount

        Returns:
            String with transaction analysis including count and net flow
        """
        try:
            self.processed_count += 1
            self.total_items += len(data_batch)

            count = len(data_batch)
            net = 0

            for item in data_batch:
                if isinstance(item, dict):
                    if item.get("type") == "buy":
                        net -= item.get("amount", 0)
                    elif item.get("type") == "sell":
                        net += item.get("amount", 0)

            self.net_flow += net
            sign = "+" if net >= 0 else ""
            return f"Transaction analysis: {count} \
operations, net flow: {sign}{net} units"
        except Exception as e:
            return f"Error processing transaction batch: {str(e)}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Filter transactions for large amounts.

        Args:
            data_batch: List of transaction dictionaries
            criteria: Filter criteria ('high-priority' or 'large')

        Returns:
            List of large transactions (> 100 units)
        """
        if criteria == "high-priority" or criteria == "large":
            filtered = []
            for item in data_batch:
                if isinstance(item, dict) and item.get("amount", 0) > 100:
                    filtered.append(item)
            return filtered
        return data_batch


class EventStream(DataStream):
    """
    Specialized stream for system event processing.

    Tracks system events with error detection and analysis.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize event stream with error tracking.

        Args:
            stream_id: Unique identifier for this event stream
        """
        super().__init__(stream_id)
        self.event_type = "System Events"
        self.error_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process batch of system events and detect errors.

        Args:
            data_batch: List of event items (dicts or strings)

        Returns:
            String with event analysis including error count
        """
        try:
            self.processed_count += 1
            self.total_items += len(data_batch)

            count = len(data_batch)
            errors = 0

            for item in data_batch:
                if isinstance(item, dict):
                    if "error" in item.get("event", "").lower():
                        errors += 1
                elif isinstance(item, str):
                    if "error" in item.lower():
                        errors += 1

            self.error_count += errors

            if errors > 0:
                return f"Event analysis: {count} events, \
{errors} error detected" if errors == 1 else f"Event analysis: \
{count} events, {errors} errors detected"
            else:
                return f"Event analysis: {count} events processed"
        except Exception as e:
            return f"Error processing event batch: {str(e)}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Filter events by error detection.

        Args:
            data_batch: List of event items
            criteria: Filter criteria ('high-priority' for errors)

        Returns:
            List of error events only
        """
        if criteria == "high-priority":
            filtered = []
            for item in data_batch:
                if isinstance(item, dict):
                    if "error" in item.get("event", "").lower():
                        filtered.append(item)
                elif isinstance(item, str):
                    if "error" in item.lower():
                        filtered.append(item)
            return filtered
        return data_batch


class StreamProcessor:
    """
    Manages multiple data streams polymorphically.

    Coordinates processing and filtering across different stream types
    using polymorphic behavior.
    """

    def __init__(self) -> None:
        """
        Initialize stream processor with empty stream list.
        """
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """
        Add a data stream to the processor.

        Args:
            stream: DataStream instance to manage
        """
        self.streams.append(stream)

    def process_all(self, data_batches: List[List[Any]]) -> List[str]:
        """
        Process all streams with corresponding data batches.

        Args:
            data_batches: List of data batches, one per stream

        Returns:
            List of processing results from each stream
        """
        results = []
        for i, stream in enumerate(self.streams):
            if i < len(data_batches):
                result = stream.process_batch(data_batches[i])
                results.append(result)
        return results

    def filter_all(self, data_batches: List[List[Any]],
                   criteria: Optional[str] = None) -> List[List[Any]]:
        """
        Filter data for all streams using specified criteria.

        Args:
            data_batches: List of data batches to filter
            criteria: Filter criteria to apply across all streams

        Returns:
            List of filtered data batches from each stream
        """
        filtered_results = []
        for i, stream in enumerate(self.streams):
            if i < len(data_batches):
                filtered = stream.filter_data(data_batches[i], criteria)
                filtered_results.append(filtered)
        return filtered_results


def main():
    """
    Demonstrate polymorphic data stream processing system.

    Shows usage of different stream types with unified interface.
    """
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor_stream.stream_id}, \
Type: {sensor_stream.sensor_type}")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    result = sensor_stream.process_batch([
        {"temp": 22.5},
        {"humidity": 65},
        {"pressure": 1013}
    ])
    print(result)

    print("\nInitializing Transaction Stream...")
    trans_stream = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans_stream.stream_id}, \
Type: {trans_stream.transaction_type}")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    result = trans_stream.process_batch([
        {"type": "buy", "amount": 100},
        {"type": "sell", "amount": 150},
        {"type": "buy", "amount": 75}
    ])
    print(result)

    print("\nInitializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    print(f"Stream ID: {event_stream.stream_id}, \
Type: {event_stream.event_type}")
    print("Processing event batch: [login, error, logout]")
    result = event_stream.process_batch(["login", "error", "logout"])
    print(result)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_002"))
    processor.add_stream(TransactionStream("TRANS_002"))
    processor.add_stream(EventStream("EVENT_002"))

    batch_data = [
        [25.0, 28.5],
        [{"type": "buy", "amount": 50}, {"type": "sell", "amount": 75},
         {"type": "buy", "amount": 100}, {"type": "sell", "amount": 125}],
        ["login", "logout", "error"]
    ]

    results = processor.process_all(batch_data)

    for i, result in enumerate(results, 1):
        print(f"Stream {i}: {result}")

    print("\n=== High-Priority Data Filtering ===")
    print("Filtering for high-priority items across all streams...")

    high_priority = [
        [32.0, 35.0, 28.0],
        [{"type": "buy", "amount": 50}, {"type": "sell", "amount": 150},
         {"type": "buy", "amount": 200}],
        ["login", "error", "warning", "error"]
    ]

    filtered = processor.filter_all(high_priority, "high-priority")

    for i, data in enumerate(filtered, 1):
        print(f"Filtered Stream {i}: {len(data)} high-priority items")

    print("\n=== Stream Statistics ===")
    for stream in processor.streams:
        stats = stream.get_stats()
        print(f"Stream {stats['stream_id']}: \
{stats['processed_batches']} batches, {stats['total_items']} total items")

    print("\nAdvanced stream processing complete. Nexus ready for \
enterprise integration.")


if __name__ == "__main__":
    main()
