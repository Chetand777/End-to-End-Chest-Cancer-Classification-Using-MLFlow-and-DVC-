# Return type of a function
from dataclasses import dataclass
from pathlib import Path

# Allow to create a class without using self
@dataclass(frozen=True) # Not allowed to add any other functionality here
class DataIngestionConfig:
  root_dir: Path
  source_url: str
  local_data_file: Path
  unzip_dir: Path