from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class DataIngestionArtifact:
    raw_artifact_path: Path
    ingested_data_filepath: Path
    raw_dvc_path: Path

    def __repr__(self) -> str:
        raw_artifact_str = self.raw_artifact_path.as_posix() if self.raw_artifact_path else "None"
        raw_dvc_str = self.raw_dvc_path.as_posix() if self.raw_dvc_path else "None"
        ingested_data_str = self.ingested_data_filepath.as_posix() if self.ingested_data_filepath else "None"

        return (
            "\nData Ingestion Artifact:\n"
            f"  - Raw Artifact:     '{raw_artifact_str}'\n"
            f"  - Raw DVC Path:     '{raw_dvc_str}'\n"
            f"  - Ingested Data Path:     '{ingested_data_str}'\n"
        )


@dataclass(frozen=True)
class DataValidationArtifact:
    validated_filepath: Path
    validation_status: bool

    def __repr__(self) -> str:
        validated_str = self.validated_filepath.as_posix() if self.validated_filepath else "None"

        return (
            "\nData Validation Artifact:\n"
            f"  - Validated Data Path: '{validated_str}'\n"
            f"  - Validation Status:   '{self.validation_status}'\n"
        )
