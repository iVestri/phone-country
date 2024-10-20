#!/usr/bin/env python3

# Dictionary of country/region codes and their corresponding country/region names
phone_to_country = {
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
    '998': 'Uzbekistan',
}

country_to_phone = {

    'AF': '93',
    'AL': '355',
    'DZ': '213',
    'AS': '1-684',
    'AD': '376',
    'AO': '244',
    'AI': '1-264',
    'AG': '1-268',
    'AR': '54',
    'AM': '374',
    'AW': '297',
    'AU': '61',
    'AT': '43',
    'AZ': '994',
    'BS': '1-242',
    'BH': '973',
    'BD': '880',
    'BB': '1-246',
    'BY': '375',
    'BE': '32',
    'BZ': '501',
    'BJ': '229',
    'BM': '1-441',
    'BT': '975',
    'BO': '591',
    'BA': '387',
    'BW': '267',
    'BR': '55',
    'IO': '246',
    'VG': '1-284',
    'BN': '673',
    'BG': '359',
    'BF': '226',
    'BI': '257',
    'KH': '855',
    'CM': '237',
    'CA': '1',
    'CV': '238',
    'KY': '1-345',
    'CF': '236',
    'TD': '235',
    'CL': '56',
    'CN': '86',
    'CO': '57',
    'KM': '269',
    'CG': '242',
    'CD': '243',
    'CK': '682',
    'CR': '506',
    'CI': '225',
    'HR': '385',
    'CU': '53',
    'CY': '357',
    'CZ': '420',
    'DK': '45',
    'DJ': '253',
    'DM': '1-767',
    'DO': '1-809',
    'EC': '593',
    'EG': '20',
    'SV': '503',
    'GQ': '240',
    'ER': '291',
    'EE': '372',
    'SZ': '268',
    'ET': '251',
    'FJ': '679',
    'FI': '358',
    'FR': '33',
    'GA': '241',
    'GM': '220',
    'GE': '995',
    'DE': '49',
    'GH': '233',
    'GI': '350',
    'GR': '30',
    'GL': '299',
    'GD': '1-473',
    'GU': '1-671',
    'GT': '502',
    'GN': '224',
    'GW': '245',
    'GY': '592',
    'HT': '509',
    'HN': '504',
    'HK': '852',
    'HU': '36',
    'IS': '354',
    'IN': '91',
    'ID': '62',
    'IR': '98',
    'IQ': '964',
    'IE': '353',
    'IL': '972',
    'IT': '39',
    'JM': '1-876',
    'JP': '81',
    'JO': '962',
    'KZ': '7',
    'KE': '254',
    'KI': '686',
    'KP': '850',
    'KR': '82',
    'KW': '965',
    'KG': '996',
    'LA': '856',
    'LV': '371',
    'LB': '961',
    'LS': '266',
    'LR': '231',
    'LY': '218',
    'LI': '423',
    'LT': '370',
    'LU': '352',
    'MO': '853',
    'MG': '261',
    'MW': '265',
    'MY': '60',
    'MV': '960',
    'ML': '223',
    'MT': '356',
    'MH': '692',
    'MR': '222',
    'MU': '230',
    'MX': '52',
    'FM': '691',
    'MD': '373',
    'MC': '377',
    'MN': '976',
    'ME': '382',
    'MA': '212',
    'MZ': '258',
    'MM': '95',
    'NA': '264',
    'NR': '674',
    'NP': '977',
    'NL': '31',
    'NZ': '64',
    'NI': '505',
    'NE': '227',
    'NG': '234',
    'NU': '683',
    'NF': '672',
    'MP': '1-670',
    'NO': '47',
    'OM': '968',
    'PK': '92',
    'PW': '680',
    'PA': '507',
    'PG': '675',
    'PY': '595',
    'PE': '51',
    'PH': '63',
    'PL': '48',
    'PT': '351',
    'PR': '1-787',
    'QA': '974',
    'RO': '40',
    'RU': '7',
    'RW': '250',
    'WS': '685',
    'SM': '378',
    'SA': '966',
    'SN': '221',
    'RS': '381',
    'SC': '248',
    'SL': '232',
    'SG': '65',
    'SK': '421',
    'SI': '386',
    'SB': '677',
    'SO': '252',
    'ZA': '27',
    'ES': '34',
    'LK': '94',
    'SD': '249',
    'SR': '597',
    'SE': '46',
    'CH': '41',
    'SY': '963',
    'TW': '886',
    'TJ': '992',
    'TZ': '255',
    'TH': '66',
    'TL': '670',
    'TG': '228',
    'TO': '676',
    'TT': '1-868',
    'TN': '216',
    'TR': '90',
    'TM': '993',
    'TC': '1-649',
    'TV': '688',
    'UG': '256',
    'UA': '380',
    'AE': '971',
    'GB': '44',
    'US': '1',
    'UY': '598',
    'UZ': '998',
    'VU': '678',
    'VA': '379',
    'VE': '58',
    'VN': '84',
    'VI': '1-340',
    'YE': '967',
    'ZM': '260',
    'ZW': '263'
    # ... Add more codes as necessary
}

def get_country_or_region(input_code):
    # Check if the input is a number
    if input_code.isdigit():
        # Check the phone_to_country dictionary
        for phone_code, country in sorted(phone_to_country.items(), key=lambda x: -len(x[0])):
            if input_code.startswith(phone_code):
                return country
        return "Unknown region"
    # Check if the input is alpha-2
    elif len(input_code) == 2 and input_code.isalpha():
        # Convert to uppercase
        input_code = input_code.upper()
        # Check the country_to_phone dictionary
        phone_code = country_to_phone.get(input_code)
        if phone_code:
            return phone_code
        else:
            return "Unknown region"
    else:
        return "Invalid input"

if __name__ == "__main__":
    input_code = input("Enter the phone number (e.g., +44 or 44), or alpha-2 country code (e.g., GB): ").strip('+').strip()
    result = get_country_or_region(input_code)
    print(f"The region for {input_code} is: {result}")
