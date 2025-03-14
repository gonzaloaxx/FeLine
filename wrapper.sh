#!/bin/bash
source "$_VENV/activate"
python "$_PY" "$@"
deactivate


