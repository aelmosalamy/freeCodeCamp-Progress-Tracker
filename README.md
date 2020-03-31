# freeCodeCamp-Progress-Tracker
A CLI tool that fetches, logs &amp; displays freeCodeCamp progress.

And yea, this tool runs a headless webdriver through Selenium to extract the user data, I know it's a bit of an overkill but I didn't find an official API from freeCodeCamp apart from the open-api initiative where things look a bit messy and work-in-progress, and... this should do the job :)
# Dependencies
* Python 3
* Python Binding for Selenium
```
pip install selenium
```
* Firefox webdriver (geckodriver)
Get it here and make sure you put it into your PATH environmental variable, might need system reboot for the change to take effect
```
https://github.com/mozilla/geckodriver/releases
```

However, I am planning to switch another webdriver with chromium and HTMLUnitDriver in mind, for performance purposes.

*This project is a work-in-progress and there is a lot of refactoring, documenting and cleaning up left; Additionally, even though core functionality is available, some features are lacking such as the ability to store logs and display these logs. The bright side is: This means that there is a lot of opportunities for contribution and a big room for collaboration, so stay tuned!*
