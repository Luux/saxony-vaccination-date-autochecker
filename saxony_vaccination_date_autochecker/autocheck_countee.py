"""
Check countee for free vaccination center dates periodically.

------------------------------------------
Brought to you by Luux - https://luux.dev/
------------------------------------------
"""
import argparse
import win32api
import datetime
import threading
import time
from requests_html import HTMLSession
from bs4 import BeautifulSoup

countee_saxony = "https://www.countee.ch/app/de/counter/impfee/_iz_sachsen"


class Autochecker():
    """Autochecker class."""

    def __init__(self, intervall_minutes, vaccination_center, countee_url):
        """Initialize the autochecker.

        Parameters
        ----------
        intervall_minutes : int
            Defines the intervall for periodic checking.
        vaccination_center : str
            Vaccination center name as displayed on countee.
        countee_url : str
            URL to countee counter.
        """
        self.intervall_minutes = intervall_minutes
        self.vaccination_center = vaccination_center
        self.countee_url = countee_url
        self.freedates_when_last_checked = 0

    def check_countee(self):
        """Simple countee check.

        (Makes fresh request when called.)

        Returns
        -------
        vaccination_freedates: int
            Number of free vaccination dates.

        details_formatted: str
            Textual information about free vaccination dates.
        """

        session = HTMLSession(mock_browser=False)
        page = session.get(self.countee_url)
        page.html.render(sleep=1)
        soup = BeautifulSoup(page.html.html, features="lxml")

        vaccination_center_element = soup.find(
            "h1", text=self.vaccination_center)
        vaccination_freedates_element = vaccination_center_element.parent.parent.find(
            "div", class_="style__val___XaOLg")
        vaccination_freedates = int(vaccination_freedates_element.text)

        separator = "\n"

        details = vaccination_center_element.parent.parent.find(
            "div", class_="style__times___3p-CE"
        ).get_text(separator=separator)
        details_formatted = self._format_date_details(details, separator)

        return vaccination_freedates, details_formatted

    def _format_date_details(self, details, separator):
        """Format the extracted date detail string.

        Parameters
        ----------
        details : str
            Text content from vaccination center date information from countee.
        separator : str
            Seperator in the raw text content. 

        Returns
        -------
        details_formatted : str
            Formatted date information for a better output.
        """
        details_raw = details.split(separator)
        details_formatted = ""

        for i in range(len(details_raw) // 2):
            unformatted_date = details_raw[i * 2].replace("\n", "")
            unformatted_date_count = details_raw[i * 2 + 1]
            details_formatted += f"{unformatted_date}: {unformatted_date_count}\n"
        return details_formatted

    def check_and_alert(self, initial: bool = False):
        """Perform a single request and check the current free vaccination dates.

        If more dates are free than the last time a check was performed, an alert box is used to notify the user.

        Parameters
        ----------
        initial : bool, optional
            If this is the first call, ommit the info about the last time checked (default: False).
        """
        freedates, details = self.check_countee()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(
            f"[{current_time}] Freie Termine in {self.vaccination_center}: {freedates}")

        if freedates > self.freedates_when_last_checked:
            self._alert_nonblocking(
                f"{freedates } freie Impftermine in {self.vaccination_center}!\n"
                f"(Vor {self.intervall_minutes} Minuten waren es {self.freedates_when_last_checked})\n\n"
                f"{details}", "Yey!"
            )
        elif initial:
            self._alert_nonblocking(
                f"{freedates } freie Impftermine in {self.vaccination_center}.\n\n"
                f"Dieses Programm wird nun alle {self.intervall_minutes} Minuten überprüfen, "
                "ob mehr Impftermine frei sind als bei der letzten Überprüfung. "
                "Sollte dieser Fall eintreten, erscheint eine Meldung wie diese hier.\n\n"
                "This tool is brought to you by Luux.\nIf you like it, say hello @ https://luux.dev/ :)",
                "Info"
            )
        self.freedates_when_last_checked = freedates

    def sleep(self):
        """Wait until the next check."""
        time.sleep(self.intervall_minutes * 60)

    def _alert_nonblocking(self, message, title):
        """Alert without blocking further checks until the message box is closed.

        Parameters
        ----------
        message : str
            Message box content.
        title : str
            Message box title.
        """
        thread = threading.Thread(
            target=self._messagebox, args=(message, title))
        thread.start()

    def _messagebox(self, message, title):
        """Displays a message box on top.

        This blocks the current thread until the message box is closed.

        Parameters
        ----------
        message : str
            Message box content.
        title : str
            Message box title.
        """
        win32api.MessageBox(
            0, message, title)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("vaccination_center", type=str,
                        help="The vaccination center name as displayed on countee. Example: \"Dresden IZ\".")
    parser.add_argument("--intervall", type=int, default=10,
                        help="Check intervall in minutes (default: 10).")
    args = parser.parse_args()
    autochecker = Autochecker(
        args.intervall, args.vaccination_center, countee_saxony)

    autochecker.check_and_alert(initial=True)
    autochecker.sleep()

    while True:
        autochecker.check_and_alert()
        autochecker.sleep()
