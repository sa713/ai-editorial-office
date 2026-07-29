#!/bin/sh

set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)

python3 \
  "$ROOT_DIR/ai-editorial-office/scripts/check_product_intent_output.py" \
  "$ROOT_DIR/ai-editorial-office/tests/fixtures/product_intent_output/cases.json"
