from abc import ABC, abstractmethod
from typing import Any, List, Dict, Protocol
from collections import defaultdict


class ProcessingStage(Protocol):
    """
    Protocol defining duck-typing interface for processing stages.

    Any class implementing execute() method is compatible regardless
    of inheritance hierarchy.
    """

    def execute(self, data: Any) -> Any:
        """
        Execute processing stage on input data.

        Args:
            data: Input data to process

        Returns:
            Processed data output
        """
        ...


class ProcessingPipeline(ABC):
    """
    Abstract base class for multi-stage processing pipelines.

    Manages sequential execution of processing stages with
    performance tracking and error handling.
    """

    def __init__(self, pipeline_id: str) -> None:
        """
        Initialize pipeline with unique identifier.

        Args:
            pipeline_id: Unique identifier for this pipeline
        """
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.performance: Dict[str, int] = defaultdict(int)

    def add_stage(self, stage: ProcessingStage) -> None:
        """
        Add processing stage to pipeline.

        Args:
            stage: Processing stage implementing execute() method
        """
        self.stages.append(stage)

    @abstractmethod
    def execute_pipeline(self, data: Any) -> Any:
        """
        Execute all stages in pipeline sequentially.

        Args:
            data: Input data to process through pipeline

        Returns:
            Final processed output after all stages
        """
        pass

    def get_performance(self) -> Dict[str, int]:
        """
        Get performance metrics for pipeline.

        Returns:
            Dictionary with execution counts and success metrics
        """
        return dict(self.performance)


class InputStage:
    """
    Initial processing stage for data validation and normalization.

    Prepares raw input data for subsequent processing stages.
    """

    def __init__(self, stage_name: str) -> None:
        """
        Initialize input stage with identifier.

        Args:
            stage_name: Name identifying this input stage
        """
        self.stage_name = stage_name

    def execute(self, data: Any) -> Dict[str, Any]:
        """
        Validate and normalize input data.

        Args:
            data: Raw input data

        Returns:
            Dictionary with normalized data and metadata
        """
        return {
            "stage": self.stage_name,
            "data": data,
            "status": "validated"
        }


class TransformStage:
    """
    Intermediate processing stage for data transformation.

    Applies business logic and data manipulation operations.
    """

    def __init__(self, stage_name: str) -> None:
        """
        Initialize transform stage with identifier.

        Args:
            stage_name: Name identifying this transform stage
        """
        self.stage_name = stage_name

    def execute(self, data: Any) -> Dict[str, Any]:
        """
        Transform input data with processing logic.

        Args:
            data: Input data to transform

        Returns:
            Dictionary with transformed data and processing metadata
        """
        if isinstance(data, dict):
            return {
                "stage": self.stage_name,
                "data": data.get("data", data),
                "status": "transformed"
            }
        return {
            "stage": self.stage_name,
            "data": data,
            "status": "transformed"
        }


class OutputStage:
    """
    Final processing stage for output formatting and delivery.

    Prepares processed data for external consumption or storage.
    """

    def __init__(self, stage_name: str) -> None:
        """
        Initialize output stage with identifier.

        Args:
            stage_name: Name identifying this output stage
        """
        self.stage_name = stage_name

    def execute(self, data: Any) -> str:
        """
        Format data for output delivery.

        Args:
            data: Processed data to format

        Returns:
            Formatted string ready for output
        """
        if isinstance(data, dict):
            data_content = data.get("data", "")
            return f"Output from {self.stage_name}: {data_content}"
        return f"Output from {self.stage_name}: {data}"


class JSONAdapter(ProcessingPipeline):
    """
    Pipeline adapter for JSON data processing.

    Specialized pipeline for handling JSON-formatted data with
    validation, transformation, and output formatting.
    """

    def execute_pipeline(self, data: Any) -> Any:
        """
        Execute JSON processing pipeline through all stages.

        Args:
            data: JSON data to process

        Returns:
            Final processed JSON output
        """
        try:
            self.performance["total_executions"] += 1
            result = data

            for stage in self.stages:
                result = stage.execute(result)

            self.performance["successful_executions"] += 1
            return result
        except Exception as e:
            self.performance["failed_executions"] += 1
            return f"Pipeline error: {str(e)}"

    def process(self, data: Any) -> Any:
        """
        Process JSON data through pipeline.

        Args:
            data: JSON data to process

        Returns:
            Processed output
        """
        return self.execute_pipeline(data)


class CSVAdapter(ProcessingPipeline):
    """
    Pipeline adapter for CSV data processing.

    Specialized pipeline for handling comma-separated value data
    with parsing, transformation, and formatting capabilities.
    """

    def execute_pipeline(self, data: Any) -> Any:
        """
        Execute CSV processing pipeline through all stages.

        Args:
            data: CSV data to process

        Returns:
            Final processed CSV output
        """
        try:
            self.performance["total_executions"] += 1
            result = data

            for stage in self.stages:
                result = stage.execute(result)

            self.performance["successful_executions"] += 1
            return result
        except Exception as e:
            self.performance["failed_executions"] += 1
            return f"Pipeline error: {str(e)}"

    def process(self, data: Any) -> Any:
        """
        Process CSV data through pipeline.

        Args:
            data: CSV data to process

        Returns:
            Processed output
        """
        return self.execute_pipeline(data)


class StreamAdapter(ProcessingPipeline):
    """
    Pipeline adapter for real-time stream data processing.

    Specialized pipeline for handling continuous data streams
    with buffering, transformation, and delivery mechanisms.
    """

    def execute_pipeline(self, data: Any) -> Any:
        """
        Execute stream processing pipeline through all stages.

        Args:
            data: Stream data to process

        Returns:
            Final processed stream output
        """
        try:
            self.performance["total_executions"] += 1
            result = data

            for stage in self.stages:
                result = stage.execute(result)

            self.performance["successful_executions"] += 1
            return result
        except Exception as e:
            self.performance["failed_executions"] += 1
            return f"Pipeline error: {str(e)}"

    def process(self, data: Any) -> Any:
        """
        Process stream data through pipeline.

        Args:
            data: Stream data to process

        Returns:
            Processed output
        """
        return self.execute_pipeline(data)


class NexusManager:
    """
    Central orchestrator for multiple processing pipelines.

    Manages lifecycle and coordination of different pipeline types
    with unified monitoring and control interface.
    """

    def __init__(self) -> None:
        """
        Initialize Nexus manager with empty pipeline registry.
        """
        self.pipelines: List[ProcessingPipeline] = []

    def register_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """
        Register new pipeline with Nexus manager.

        Args:
            pipeline: Processing pipeline to register
        """
        self.pipelines.append(pipeline)

    def execute_all(self, data_inputs: List[Any]) -> List[Any]:
        """
        Execute all registered pipelines with corresponding inputs.

        Args:
            data_inputs: List of input data for each pipeline

        Returns:
            List of outputs from all pipeline executions
        """
        results = []
        for i, pipeline in enumerate(self.pipelines):
            if i < len(data_inputs):
                result = pipeline.execute_pipeline(data_inputs[i])
                results.append(result)
        return results

    def get_system_stats(self) -> Dict[str, Any]:
        """
        Gather performance statistics from all pipelines.

        Returns:
            Dictionary with aggregated system performance metrics
        """
        total_processed = 0
        total_successful = 0
        pipeline_stats = []

        for pipeline in self.pipelines:
            perf = pipeline.get_performance()
            total_processed += perf.get("total_executions", 0)
            total_successful += perf.get("successful_executions", 0)
            pipeline_stats.append({
                "pipeline_id": pipeline.pipeline_id,
                "performance": perf
            })

        efficiency = 0.0
        if total_processed > 0:
            efficiency = total_successful / total_processed
            efficiency = efficiency * 100

        return {
            "total_pipelines": len(self.pipelines),
            "total_processed": total_processed,
            "total_successful": total_successful,
            "efficiency": f"{efficiency:.1f}%",
            "pipeline_details": pipeline_stats
        }


def main():
    """
    Demonstrate enterprise-level polymorphic pipeline system.

    Shows integration of multiple pipeline types with Protocol-based
    duck typing and comprehensive orchestration.
    """
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

    json_pipeline = JSONAdapter("JSON_PIPELINE_001")
    json_pipeline.add_stage(InputStage("JSON_Input"))
    json_pipeline.add_stage(TransformStage("JSON_Transform"))
    json_pipeline.add_stage(OutputStage("JSON_Output"))

    csv_pipeline = CSVAdapter("CSV_PIPELINE_001")
    csv_pipeline.add_stage(InputStage("CSV_Input"))
    csv_pipeline.add_stage(TransformStage("CSV_Transform"))
    csv_pipeline.add_stage(OutputStage("CSV_Output"))

    stream_pipeline = StreamAdapter("STREAM_PIPELINE_001")
    stream_pipeline.add_stage(InputStage("Stream_Input"))
    stream_pipeline.add_stage(TransformStage("Stream_Transform"))
    stream_pipeline.add_stage(OutputStage("Stream_Output"))

    print("\nInitializing JSON Pipeline...")
    result = json_pipeline.execute_pipeline(
        {"user": "Alice", "action": "login"})
    print(f"Pipeline: {json_pipeline.pipeline_id}")
    print(f"Result: {result}")

    print("\nInitializing CSV Pipeline...")
    result = csv_pipeline.execute_pipeline("user,action,timestamp")
    print(f"Pipeline: {csv_pipeline.pipeline_id}")
    print(f"Result: {result}")

    print("\nInitializing Stream Pipeline...")
    result = stream_pipeline.execute_pipeline(
        ["event1", "event2", "event3"])
    print(f"Pipeline: {stream_pipeline.pipeline_id}")
    print(f"Result: {result}")

    print("\n=== Nexus Orchestration ===")
    print("Coordinating multiple pipelines through Nexus Manager...")

    nexus = NexusManager()
    nexus.register_pipeline(json_pipeline)
    nexus.register_pipeline(csv_pipeline)
    nexus.register_pipeline(stream_pipeline)

    inputs = [
        {"data": "JSON payload"},
        "CSV,data,row",
        ["stream", "events"]
    ]

    results = nexus.execute_all(inputs)

    print("\nPipeline Execution Results:")
    for i, result in enumerate(results, 1):
        print(f"Pipeline {i}: {result}")

    print("\n=== System Performance Metrics ===")
    stats = nexus.get_system_stats()
    print(f"Total Pipelines: {stats['total_pipelines']}")
    print(f"Total Processed: {stats['total_processed']}")
    print(f"Total Successful: {stats['total_successful']}")
    print(f"System Efficiency: {stats['efficiency']}")

    print("\nDetailed Pipeline Performance:")
    for detail in stats['pipeline_details']:
        print(f"\nPipeline: {detail['pipeline_id']}")
        perf = detail['performance']
        print(f"  Executions: {perf.get('total_executions', 0)}")
        print(f"  Successful: {perf.get('successful_executions', 0)}")
        print(f"  Failed: {perf.get('failed_executions', 0)}")

    print("\nEnterprise Nexus system fully operational.")
    print("All pipelines integrated and performing optimally.")


if __name__ == "__main__":
    main()
