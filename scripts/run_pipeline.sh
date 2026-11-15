#!/bin/bash

CONFIG="config"
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && cd .. && pwd)"

for arg in "$@"; do
  case $arg in
    --config=*)
      CONFIG="${arg#*=}" ;;
  esac
done

export PYTHONPATH=$PYTHONPATH:"$PROJECT_DIR"/src
export PYTHONHASHSEED="0"

export REPOSCOPE_RUN_TIMESTAMP="$(date +%Y%m%d_%H%M%S_%3N)"
LOG_DIR="$PROJECT_DIR/results/runs/$REPOSCOPE_RUN_TIMESTAMP"
mkdir -p "$LOG_DIR"
exec > >(tee "$LOG_DIR/reposcope.log") 2>&1

python "$PROJECT_DIR"/src/pipeline.py --config="$CONFIG"
