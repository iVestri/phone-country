A simple script to determine which country or zone a phone number originates from.

Requires python3.

----

When used, the script will provide a prompt for you to enter the first few digits of the phone number:
```
python3 phone.py >
Enter the phone number or code (e.g., +44 or 44):
```
After entering the first digit(s), the script will output the number's country or zone.
```
Enter the phone number or code (e.g., +44 or 44): 420
The region for 420 is: Czechia
```

If you cannot tell what country code is used in the number, you can use the first digit to determine which zone the number is in.

```
Enter the phone number or code (e.g., +44 or 44): +5
The region for 5 is: South America, Central America, Latin America, and Mexico
```
----
This script uses a dictionary with a list of all the different country codes I could find (mainly through Wikipedia). If a code is not listed, please let me know and I will add it.
