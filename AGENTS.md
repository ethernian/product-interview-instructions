# Agent Instructions

When working in a stage directory named `01-*` through `09-*` under `stages/`, read and follow `stages/<stage>/AGENTS.md` if it exists.

When the user asks to `run <stage>`, treat this as a request to start or resume that stage, not as a shell command. Read and follow `stages/<stage>/README.md`, including any invocation and argument mapping. Resolve paths relative to the stage directory when its instructions say to do so. If the stage or its required instructions are missing, explain what is missing and ask the user how to proceed. Do not start a stage merely because its files are being read or edited.
