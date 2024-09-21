#!/usr/bin/env python3

# Dictionary of country/region codes and their corresponding country/region names
country_codes = {
    '1': 'US, Canada, and US Territories',
    '2': 'Africa, Aruba, Greenland, Faroe Islands, and British Indian Ocean Territory',
    '3': 'Europe and Armenia',
    '4': 'Europe',
    '5': 'South America, Central America, Latin America, and Mexico',
    '6': 'Southeast Asia, Oceania, and Thailand',
    '7': 'Russia and Kazakhstan',
    '8': 'East Asia, South Asia, and Bangladesh',
    '9': 'West Asia, Central Asia, Middle East, and Mongolia',
    '20': 'Egypt',
    '30': 'Greece',
    '31': 'Netherlands',
    '32': 'Belgium',
    '33': 'France',
    '34': 'Spain',
    '36': 'Hungary',
    '39': 'Italy',
    '40': 'Romania',
    '41': 'Switzerland',
    '43': 'Austria',
    '44': 'United Kingdom',
    '45': 'Denmark',
    '46': 'Sweden',
    '47': 'Norway',
    '48': 'Poland',
    '49': 'Germany',
    '51': 'Peru',
    '52': 'Mexico',
    '53': 'Cuba',
    '54': 'Argentina',
    '55': 'Brazil',
    '56': 'Chile',
    '57': 'Colombia',
    '58': 'Venezuela',
    '60': 'Malaysia',
    '61': 'Australia',
    '62': 'Indonesia',
    '63': 'Philippines',
    '64': 'New Zealand',
    '65': 'Singapore',
    '66': 'Thailand',
    '81': 'Japan',
    '82': 'South Korea',
    '84': 'Vietnam',
    '86': 'China',
    '90': 'Turkey',
    '91': 'India',
    '92': 'Pakistan',
    '93': 'Afghanistan',
    '94': 'Sri Lanka',
    '95': 'Myanmar',
    '98': 'Iran',
    '211': 'South Sudan',
    '212': 'Morocco',
    '213': 'Algeria',
    '216': 'Tunisia',
    '218': 'Libya',
    '220': 'Gambia',
    '221': 'Senegal',
    '222': 'Mauritania',
    '223': 'Mali',
    '224': 'Guinea',
    '225': 'Ivory Coast',
    '226': 'Burkina Faso',
    '227': 'Niger',
    '228': 'Togo',
    '229': 'Benin',
    '230': 'Mauritius',
    '231': 'Liberia',
    '232': 'Sierra Leone',
    '233': 'Ghana',
    '234': 'Nigeria',
    '235': 'Chad',
    '236': 'Central African Republic',
    '237': 'Cameroon',
    '238': 'Cape Verde',
    '239': 'Sao Tome and Principe',
    '240': 'Equatorial Guinea',
    '241': 'Gabon',
    '242': 'Republic of the Congo',
    '243': 'Democratic Republic of the Congo',
    '244': 'Angola',
    '245': 'Guinea-Bissau',
    '246': 'British Indian Ocean Territory',
    '247': 'Ascension Island',
    '248': 'Seychelles',
    '249': 'Sudan',
    '250': 'Rwanda',
    '251': 'Ethiopia',
    '252': 'Somalia',
    '253': 'Djibouti',
    '254': 'Kenya',
    '255': 'Tanzania',
    '256': 'Uganda',
    '257': 'Burundi',
    '258': 'Mozambique',
    '260': 'Zambia',
    '261': 'Madagascar',
    '262': 'Reunion',
    '263': 'Zimbabwe',
    '264': 'Namibia',
    '265': 'Malawi',
    '266': 'Lesotho',
    '267': 'Botswana',
    '268': 'Eswatini',
    '269': 'Comoros',
    '290': 'Saint Helena',
    '291': 'Eritrea',
    '297': 'Aruba',
    '298': 'Faroe Islands',
    '299': 'Greenland',
    '350': 'Gibraltar',
    '351': 'Portugal',
    '352': 'Luxembourg',
    '353': 'Ireland',
    '354': 'Iceland',
    '355': 'Albania',
    '356': 'Malta',
    '357': 'Cyprus',
    '358': 'Finland',
    '359': 'Bulgaria',
    '370': 'Lithuania',
    '371': 'Latvia',
    '372': 'Estonia',
    '373': 'Moldova',
    '374': 'Armenia',
    '375': 'Belarus',
    '376': 'Andorra',
    '377': 'Monaco',
    '378': 'San Marino',
    '379': 'Vatican City',
    '380': 'Ukraine',
    '381': 'Serbia',
    '382': 'Montenegro',
    '383': 'Kosovo',
    '385': 'Croatia',
    '386': 'Slovenia',
    '387': 'Bosnia and Herzegovina',
    '389': 'North Macedonia',
    '420': 'Czechia',
    '421': 'Slovakia',
    '423': 'Liechtenstein',
    '500': 'Falkland Islands',
    '501': 'Belize',
    '502': 'Guatemala',
    '503': 'El Salvador',
    '504': 'Honduras',
    '505': 'Nicaragua',
    '506': 'Costa Rica',
    '507': 'Panama',
    '508': 'Saint Pierre and Miquelon',
    '509': 'Haiti',
    '590': 'Guadeloupe',
    '591': 'Bolivia',
    '592': 'Guyana',
    '593': 'Ecuador',
    '594': 'French Guiana',
    '595': 'Paraguay',
    '596': 'Martinique',
    '597': 'Suriname',
    '598': 'Uruguay',
    '599': 'Curacao',
    '670': 'East Timor',
    '672': 'Antarctica',
    '673': 'Brunei',
    '674': 'Nauru',
    '675': 'Papua New Guinea',
    '676': 'Tonga',
    '677': 'Solomon Islands',
    '678': 'Vanuatu',
    '679': 'Fiji',
    '680': 'Palau',
    '681': 'Wallis and Futuna',
    '682': 'Cook Islands',
    '683': 'Niue',
    '685': 'Samoa',
    '686': 'Kiribati',
    '687': 'New Caledonia',
    '688': 'Tuvalu',
    '689': 'French Polynesia',
    '690': 'Tokelau',
    '691': 'Micronesia',
    '692': 'Marshall Islands',
    '850': 'North Korea',
    '852': 'Hong Kong',
    '853': 'Macau',
    '855': 'Cambodia',
    '856': 'Laos',
    '870': 'Inmarsat',
    '880': 'Bangladesh',
    '881': 'Global Mobile Satellite System',
    '882': 'International Networks',
    '883': 'International Networks',
    '886': 'Taiwan',
    '960': 'Maldives',
    '961': 'Lebanon',
    '962': 'Jordan',
    '963': 'Syria',
    '964': 'Iraq',
    '965': 'Kuwait',
    '966': 'Saudi Arabia',
    '967': 'Yemen',
    '968': 'Oman',
    '970': 'Palestine',
    '971': 'United Arab Emirates',
    '972': 'Israel',
    '973': 'Bahrain',
    '974': 'Qatar',
    '975': 'Bhutan',
    '976': 'Mongolia',
    '977': 'Nepal',
    '992': 'Tajikistan',
    '993': 'Turkmenistan',
    '994': 'Azerbaijan',
    '995': 'Georgia',
    '996': 'Kyrgyzstan',
    '997': 'Kazakhstan',
    '998': 'Uzbekistan'
    # ... Add more codes as necessary
}

def get_country_or_region(phone_code):
    # Iterate through the country codes to find the matching prefix
    for code, region in sorted(country_codes.items(), key=lambda x: -len(x[0])):  # Sort by length of the code
        if phone_code.startswith(code):
            return region
    return "Unknown region"  # Default if no match is found

if __name__ == "__main__":
    phone_code = input("Enter the phone number or code (e.g., +44 or 44): ").strip('+')  # Strip leading '+'
    result = get_country_or_region(phone_code)
    print(f"The region for {phone_code} is: {result}")