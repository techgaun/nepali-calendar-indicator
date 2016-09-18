# nepali-calendar-indicator
> Simple indicator applet to show Nepali date and calendar

Showing the calendar is not done yet. If anybody wants to contribute, you're welcome to do so :)

### Installation

The goal is to be able to do `pip install nepcal_applet` and have the applet running but there's little bit of work that needs to be done for that. This requires python 3.x and python-gi.

For time-being, the following works:

```shell
git clone https://github.com/techgaun/nepali-calendar-indicator.git
cd nepali-calendar-indicator
make install

# if you see permission errors (which should be due to system-wide pip)
sudo make install
```

After the successful installation, it looks like below:

![Nepcal Screenshot](screenshot.png)
