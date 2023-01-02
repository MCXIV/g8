# -*- coding: utf-8 -*-
# --------------------------------------------------
# It downloads a file from a url, and displays a progress status
# Quentin Dufournet, 2023
# --------------------------------------------------
# Built-in
import sys
import os

# 3rd party
import requests
from rich.progress import (
    DownloadColumn,
    Progress,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)
from rich import print as rprint

# --------------------------------------------------
# Usage: python3 g8.py https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz
# --------------------------------------------------


class g8():
    @staticmethod
    def main():
        """
        It downloads a file from a given URL and displays a progress status while doing so
        The URL is the first argument

        .. warning:: URL must start with http:// or https://, if you want to use http://, add the argument --allow-http
        """

        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            rprint('[bold red]Missing URL :(')
            sys.exit(1)

        progress = Progress(
            TextColumn("[bold #4f54a3][i]{task.fields[filename]}"),
            "⥊",
            "[progress.percentage][magenta]{task.percentage:>3.1f}%",
            "⥊",
            DownloadColumn(),
            "⥊",
            TransferSpeedColumn(),
            "⥊",
            TimeRemainingColumn(),
        )

        if not url.startswith('http'):
            rprint('[bold red]Invalid URL :(')
            sys.exit(1)

        if url.startswith('http://') and '--allow-http' not in sys.argv:
            rprint('[bold #FFA500]HTTP is not safe, add the argument --allow-http')
            sys.exit(1)

        with progress:
            response = requests.get(url, stream=True)
            totalLength = response.headers.get('content-length')
            if totalLength is None or int(totalLength) == 0:
                rprint('[bold red]No content found :(')
                sys.exit(1)

            fileName = url.split('/')[-1]

            taskId = progress.add_task(
                description='Download',
                filename=f'~/{fileName}',
                total=int(totalLength),
                start=True,
            )

            with open(fileName, "wb") as f:
                for data in response.iter_content(chunk_size=2048):
                    f.write(data)
                    progress.update(taskId, advance=len(data))

            if os.path.getsize(fileName) != int(totalLength):
                rprint('[bold red]Download failed :(')
                sys.exit(1)

            progress.stop()
            rprint(f'[bold green]! {fileName} downloaded successfully !')

            sys.exit(0)

# To run the script directly
if __name__ == "__main__":
    g8().main()
