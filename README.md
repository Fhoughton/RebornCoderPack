# RebornCoderPack
RebornCoderPack is a rewrite of the Minecraft Coder Pack (MCP) version 4.3, which was used to create mods for Minecraft Beta 1.7.3.

The pack was created to fix the 'software rot' of the original mods tools which had:
- A broken update checker, that crashed the tools upon use
- Packaged python binaries (we currently use the system version, and later aim to use Nuitka to ship compiled executables)
- Outdated instructions for setting up tooling such as Eclipse (the modern pack recommends Visual Studio Code)
- Outdated design decisions (18 bash/batch scripts to execute the tools, which is now done by a manager `rbc.py`)
