import requests
from bs4 import BeautifulSoup
import re
from typing import Optional, Tuple, Dict


def fetch_page_text(url: str) -> str:
	"""Fetch the URL and return the page text (HTML as string).

	Raises requests.HTTPError on non-2xx responses.
	"""
	resp = requests.get(url)
	resp.raise_for_status()
	return resp.text


def soup_from_html(html: str) -> BeautifulSoup:
	return BeautifulSoup(html, 'html.parser')


def parse_text(all_text: str) -> Dict[str, Dict[str, Optional[str]]]:
	"""Parse the flattened page text and extract report date, lake level and surface temp.

	Returns a dict with keys 'report', 'lake', 'temp' each containing {'label': str|None, 'value': str|None}.
	The function uses the same regex style as the original script: it expects a label line followed
	by a value line starting with two digits.
	"""
	def find(pattern: str) -> Tuple[Optional[str], Optional[str]]:
		m = re.search(pattern, all_text, re.MULTILINE)
		if not m:
			return None, None
		return m.group(1).strip(), m.group(2).strip()

	report_label, report_value = find(r"\s*(Lake Level Forecast)\s*(\d\d.*)")
	lake_label, lake_value = find(r"(Current.*)\n(\d\d.*)")
	temp_label, temp_value = find(r"(Surface.*)\n(\d\d.*)")

	return {
		'report': {'label': report_label, 'value': report_value},
		'lake': {'label': lake_label, 'value': lake_value},
		'temp': {'label': temp_label, 'value': temp_value},
	}


def extract_from_url(url: str) -> Dict[str, Dict[str, Optional[str]]]:
	html = fetch_page_text(url)
	soup = soup_from_html(html)
	text = soup.get_text()
	print(text)
	return parse_text(text)


def main() -> None:
	# default behavior preserved for CLI compatibility
	url = 'https://www.ameren.com/property/lake-of-the-ozarks/reports'
	try:
		data = extract_from_url(url)
	except Exception as e:
		print(f"Failed to fetch or parse page: {e}")
		return

	# mirror original printed output style when values are present
	if data['report']['label'] and data['report']['value']:
		print(data['report']['label'] + "  " + data['report']['value'])
	if data['lake']['label'] and data['lake']['value']:
		print(data['lake']['label'] + "  " + data['lake']['value'])
	if data['temp']['label'] and data['temp']['value']:
		print(data['temp']['label'] + "  " + data['temp']['value'])


if __name__ == '__main__':
	main()