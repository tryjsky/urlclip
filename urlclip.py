#!/usr/bin/env python
# -*- coding: utf-8 -*- #


# Copyright 2023 Y., Ryota <tryjsky@gmail.com>
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys
import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import Clipboard, TextDataFormat
from HTMLParser import HTMLParser
import re


class HtmlDocumentParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.doc = ""
		self.href = ""
		self.anchor_doc = ""
		self.is_anchor = False


	def handle_starttag(self, tag, attrs):
		if tag == "a":
			self.is_anchor = True
			# リンクのURLを取得
			for name, value in attrs:
				if name == "href":
					self.href = value


	def handle_endtag(self, tag):
		if tag == "a":
			self.doc += "[{0}]({1})".format(self.anchor_doc, self.href)
			self.anchor_doc = ""
			self.href = ""
			self.is_anchor = False
		elif tag == "div":
			self.doc += "\n"


	def handle_data(self, data):
		if self.is_anchor:
			self.anchor_doc = data
		else:
			self.doc += data.replace("\n", "")
		

def get_html():
	cliplines = Clipboard.GetText(TextDataFormat.Html).splitlines()
	line = 0
	for clip in cliplines:
		if (clip.startswith("Version:")
				or clip.startswith("StartHTML:")
				or clip.startswith("EndHTML:")
				or clip.startswith("StartFragment:")
				or clip.startswith("EndFragment:")
				or clip.startswith("SourceURL:")
				or clip == ""):
			# header part
			line = line + 1
		else:
			# body part
			return "\n".join(cliplines[line:])
	# empty body
	return ""


def set_text(text):
	if text:
		Clipboard.SetText(text)


def main():
	if Clipboard.ContainsText(TextDataFormat.Html):
		html = get_html()
		# sys.stdout.write(html)
		parser = HtmlDocumentParser()
		parser.feed(html)
		sys.stdout.write(parser.doc)
		set_text(parser.doc)


main()