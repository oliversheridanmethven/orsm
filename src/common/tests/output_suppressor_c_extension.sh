#!/bin/bash
set -e
executable=$1
shift 1
args="$@"
echo "Testing suppression:"
echo "script: ${executable}"
echo "args: ${args}"

output=$(${executable} ${args})

if [ -n "${output}" ]; then
  echo "The suppressor failed and output was detected. Output = \"${output}\""
  exit 1
else
  echo "The suppressor worked and no output was detected. Output = \"${output}\""
  exit 0
fi

