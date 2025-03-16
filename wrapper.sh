#!/bin/bash
source "$FELINE_ENV/activate"
python "$FELINE_PY" "$@"
deactivate
