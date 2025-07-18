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

python "$PROJECT_DIR"/src/pipeline.py --config="$CONFIG"
