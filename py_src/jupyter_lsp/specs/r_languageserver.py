from pathlib import Path

from .utils import ShellSpec


class RLanguageServer(ShellSpec):
    key = "r-languageserver"
    cmd = "Rscript"
    args = ["--slave", (Path(__file__).parent / "languageserver.R").as_posix()]
    languages = ["r"]
