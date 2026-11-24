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
CONFIG_FILE="$PROJECT_DIR/config/$CONFIG.yaml"
DATASET="$(sed -nE 's/^[[:space:]]*dataset:[[:space:]]*"([^"]+)".*/\1/p' "$CONFIG_FILE" | head -n 1)"
if [ -z "$DATASET" ]; then
  echo "Could not determine dataset from $CONFIG_FILE" >&2
  exit 1
fi
export REPOSCOPE_RESULTS_ROOT="${REPOSCOPE_RESULTS_ROOT:-$PROJECT_DIR/results/runs}"
RESULTS_ROOT="$REPOSCOPE_RESULTS_ROOT"
LOG_DIR="$RESULTS_ROOT/$DATASET/$REPOSCOPE_RUN_TIMESTAMP"
mkdir -p "$LOG_DIR"
set -o pipefail

python "$PROJECT_DIR"/src/pipeline.py --config="$CONFIG" 2>&1 | tee "$LOG_DIR/reposcope.log"
exit "${PIPESTATUS[0]}"
