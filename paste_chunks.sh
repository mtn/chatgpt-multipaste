#!/usr/bin/env bash
echo "=== paste_chunks.sh start $(date) ==="
CHUNK=${CHUNK:-81920}
TEXT=$(pbpaste)
echo "clipboard length: ${#TEXT}"

while [[ -n "$TEXT" ]]; do
  PART=${TEXT:0:$CHUNK}
  echo "→ next chunk length ${#PART}"
  printf '%s' "$PART" | pbcopy
  osascript -e 'tell application "System Events" to keystroke "v" using {command down}'
  echo "   osascript exit code $?"
  sleep 0.15
  TEXT=${TEXT:$CHUNK}
done

echo "=== paste_chunks.sh end $(date) ==="
