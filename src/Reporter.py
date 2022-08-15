from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Checker import Checker

from rich.console import Console
from typing import AnyStr
import json

from __version__ import __version__

import time


class Reporter:
    """
    Class to report the results of Checker.failures dictionary.
    """

    def __init__(self, checker: Checker) -> None:
        self.failures = checker.failures
        self.options = checker.options
        self.console = Console()
        self.source = checker.source

    def report(self) -> None:
        """
        Prints the results of the Checker.failures dictionary.
        """
        self.console.print()
        self.console.print("################################################################################\n")
        if not self.failures:
            self.console.print("No failures found.")
            return
        else:
            fails = [failure for failures in self.failures.values() for failure in failures]
            # Print the number of failures and the files that have failures
            # add up the number elements in items()
            self.console.print(f"{len(fails)} failures found in {len(self.failures)} files.")

        # Print the files that have failures
        self.console.print("================================================================================")
        self.console.print("Failures:")
        self.console.print("--------------------------------------------------------------------------------")
        for file_path, urls in self.failures.items():
            self.console.print(f"[bold]File[/bold]: [green]{file_path}[/green]")
            for url in urls:
                self.console.print(f"   URL:  {url}")
            self.console.print("")

        # Write the report to file if the option is set
        if self.options["report_to_file"]:
            self.report_to_file(self.options["report_filename"])

    def report_to_file(self, file_path: AnyStr) -> None:
        """
        Prints the results of the Checker.failures dictionary to a file as JSON.
        """
        # Add "failures" key to the dictionary
        failures = {
            "metadata": {
                "time": time.strftime("%Y-%m-%d %H:%M:%S"),
                "version": __version__,
                "input": self.source,
            },
            "failures": self.failures,
        }

        time_stamp = time.strftime("%Y-%m-%d-%H-%M-%S")

        with open(f"{file_path}-{time_stamp}.json", "w") as file:
            file.write(json.dumps(failures, indent=4))
