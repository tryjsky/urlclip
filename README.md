# urlclip

Copying from the clipboard with Markdown format

## Overview

This script converts HTML from the clipboard to Markdown.

When you copy a URL from Chrome's address bar, the browser copies the URL in HTML format.
you can use this script to copy the URL to Markdown format.

It supports IronPython 2.

## Usage

Copy the HTML text (or the browser's address bar) and run the script. It will overwrite the clipboard with the Markdown format.

## Implementation

The script uses Python to extract HTML from the clipboard. It leverages IronPython's CLR integration.
