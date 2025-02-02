# Day 35 - Rain alert script

On day 35, a rain alert script was built.

This script, makes use of the Open Weather API, to fetch weather data from a set of given coordinates.

The data retrieved is the forecast of the weather in the next days in 3h periods.
On this script, data for the next 12h is retrieved, (4 periods of 3h), and if any of those periods signals the possibility of rainning, then an email is sent using Python's smtplib, warning that it's going to rain.

To use this script, you need to provide your own Open Weather API key, alongside your email credentials for smtplib. 