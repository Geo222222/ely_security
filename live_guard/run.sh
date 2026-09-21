#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG="${ELY_CONFIG:-$ROOT/live_guard.json}"
if [[ ! -f "$CONFIG" ]]; then
  cp "$ROOT/live_guard.example.json" "$CONFIG"
  echo "Created $CONFIG. Review trusted_cidrs before relying on new-device classification."
fi
exec python3 "$ROOT/ely_live_guard.py" --config "$CONFIG" "$@"
