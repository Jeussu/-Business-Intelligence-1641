import numpy as np
import csv

hotel_bookings = []

for row in csv.reader(open("../hotel_bookings.csv", "r"), delimiter=','):
    hotel_bookings.append(row)

country_dict = {'AFG': 'Afghanistan',
                'ALA': 'Aland Islands',
                'ALB': 'Albania',
                'DZA': 'Algeria',
                'ASM': 'American Samoa',
                'AND': 'Andorra',
                'AGO': 'Angola',
                'AIA': 'Anguilla',
                'ATA': 'Antarctica',
                'ATG': 'Antigua and Barbuda',
                'ARG': 'Argentina',
                'ARM': 'Armenia',
                'ABW': 'Aruba',
                'AUS': 'Australia',
                'AUT': 'Austria',
                'AZE': 'Azerbaijan',
                'BHS': 'Bahamas',
                'BAH': 'Bahrain',
                'BGD': 'Bangladesh',
                'BRB': 'Barbados',
                'BLR': 'Belarus',
                'BEL': 'Belgium',
                'BLZ': 'Belize',
                'BEN': 'Benin',
                'BMU': 'Bermuda',
                'BTN': 'Bhutan',
                'BOL': 'Bolivia',
                'BIH': 'Bosnia and Herzegovina',
                'BWA': 'Botswana',
                'BVT': 'Bouvet Island',
                'BRA': 'Brazil',
                'VGB': 'British Virgin Islands',
                'IOT': 'British Indian Ocean Territory',
                'BRN': 'Brunei Darussalam',
                'BGR': 'Bulgaria',
                'BFA': 'Burkina Faso',
                'BDI': 'Burundi',
                'KHM': 'Cambodia',
                'CMR': 'Cameroon',
                'CAN': 'Canada',
                'CPV': 'Cape Verde',
                'CYM': 'Cayman Islands',
                'CAF': 'Central African Republic',
                'TCD': 'Chad',
                'CHL': 'Chile',
                'CN': 'China',
                'HKG': 'Hong Kong, Special Administrative Region of China',
                'MAC': 'Macao, Special Administrative Region of China',
                'CXR': 'Christmas Island',
                'CCK': 'Cocos (Keeling) Islands',
                'COL': 'Colombia',
                'COM': 'Comoros',
                'COG': 'Congo (Brazzaville)',
                'COD': 'Congo, Democratic Republic of the',
                'COK': 'Cook Islands',
                'CRI': 'Costa Rica',
                'CIV': 'Cote d\'Ivoire',
                'HRV': 'Croatia',
                'CUB': 'Cuba',
                'CYP': 'Cyprus',
                'CZE': 'Czech Republic',
                'DNK': 'Denmark',
                'DJI': 'Djibouti',
                'DMA': 'Dominica',
                'DOM': 'Dominican Republic',
                'ECU': 'Ecuador',
                'EGY': 'Egypt',
                'SLV': 'El Salvador',
                'GNQ': 'Equatorial Guinea',
                'ERI': 'Eritrea',
                'EST': 'Estonia',
                'ETH': 'Ethiopia',
                'FLK': 'Falkland Islands (Malvinas)',
                'FRO': 'Faroe Islands',
                'FJI': 'Fiji',
                'FIN': 'Finland',
                'FRA': 'France',
                'GUF': 'French Guiana',
                'PYF': 'French Polynesia',
                'ATF': 'French Southern Territories',
                'GAB': 'Gabon',
                'GMB': 'Gambia',
                'GEO': 'Georgia',
                'DEU': 'Germany',
                'GHA': 'Ghana',
                'GIB': 'Gibraltar',
                'GRC': 'Greece',
                'GRL': 'Greenland',
                'GRD': 'Grenada',
                'GLP': 'Guadeloupe',
                'GUM': 'Guam',
                'GTM': 'Guatemala',
                'GGY': 'Guernsey',
                'GIN': 'Guinea',
                'GNB': 'Guinea-Bissau',
                'GUY': 'Guyana',
                'HAI': 'Haiti',
                'HMD': 'Heard Island and Mcdonald Islands',
                'VAT': 'Holy See (Vatican City State)',
                'HND': 'Honduras',
                'HUN': 'Hungary',
                'ISL': 'Iceland',
                'IND': 'India',
                'IDN': 'Indonesia',
                'IRN': 'Iran, Islamic Republic of',
                'IRQ': 'Iraq',
                'IRL': 'Republic of Ireland',
                'IMN': 'Isle of Man',
                'ISR': 'Israel',
                'ITA': 'Italy',
                'JAM': 'Jamaica',
                'JPN': 'Japan',
                'JEY': 'Jersey',
                'JOR': 'Jordan',
                'KAZ': 'Kazakhstan',
                'KEN': 'Kenya',
                'KIR': 'Kiribati',
                'PRK': 'Korea, Democratic People\'s Republic of',
                'KWT': 'Kuwait',
                'KGZ': 'Kyrgyzstan',
                'LAO': 'Lao PDR',
                'LVA': 'Latvia',
                'LBN': 'Lebanon',
                'LSO': 'Lesotho',
                'LIB': 'Liberia',
                'LBY': 'Libya',
                'LIE': 'Liechtenstein',
                'LTU': 'Lithuania',
                'LUX': 'Luxembourg',
                'MKD': 'Macedonia, Republic of',
                'MDG': 'Madagascar',
                'MWI': 'Malawi',
                'MYS': 'Malaysia',
                'MDV': 'Maldives',
                'MLI': 'Mali',
                'MLT': 'Malta',
                'MHL': 'Marshall Islands',
                'MTQ': 'Martinique',
                'MRT': 'Mauritania',
                'MUS': 'Mauritius',
                'MYT': 'Mayotte',
                'MEX': 'Mexico',
                'FSM': 'Micronesia, Federated States of',
                'MDA': 'Moldova',
                'MCO': 'Monaco',
                'MNG': 'Mongolia',
                'MNE': 'Montenegro',
                'MSR': 'Montserrat',
                'MAR': 'Morocco',
                'MOZ': 'Mozambique',
                'MMR': 'Myanmar',
                'NAM': 'Namibia',
                'NRU': 'Nauru',
                'NPL': 'Nepal',
                'NLD': 'Netherlands',
                'ANT': 'Netherlands Antilles',
                'NCL': 'New Caledonia',
                'NZL': 'New Zealand',
                'NIC': 'Nicaragua',
                'NER': 'Niger',
                'NGA': 'Nigeria',
                'NIU': 'Niue',
                'NFK': 'Norfolk Island',
                'MNP': 'Northern Mariana Islands',
                'NOR': 'Norway',
                'OMA': 'Oman',
                'PAK': 'Pakistan',
                'PLW': 'Palau',
                'PSE': 'Palestinian Territory, Occupied',
                'PAN': 'Panama',
                'PNG': 'Papua New Guinea',
                'PRY': 'Paraguay',
                'PER': 'Peru',
                'PHL': 'Philippines',
                'PCN': 'Pitcairn',
                'POL': 'Poland',
                'PRT': 'Portugal',
                'PRI': 'Puerto Rico',
                'QAT': 'Qatar',
                'REU': 'Reunion',
                'ROU': 'Romania',
                'RUS': 'Russian Federation',
                'RWA': 'Rwanda',
                'BLM': 'Saint-Barthelemy',
                'SHN': 'Saint Helena',
                'KNA': 'Saint Kitts and Nevis',
                'LCA': 'Saint Lucia',
                'MAF': 'Saint-Martin (French part)',
                'SPM': 'Saint Pierre and Miquelon',
                'VCT': 'Saint Vincent and Grenadines',
                'WSM': 'Samoa',
                'SMR': 'San Marino',
                'STP': 'Sao Tome and Principe',
                'SAU': 'Saudi Arabia',
                'SEN': 'Senegal',
                'SRB': 'Serbia',
                'SYC': 'Seychelles',
                'SLE': 'Sierra Leone',
                'SGP': 'Singapore',
                'SVK': 'Slovakia',
                'SVN': 'Slovenia',
                'SLB': 'Solomon Islands',
                'SOM': 'Somalia',
                'ZAF': 'South Africa',
                'SGS': 'South Georgia and the South Sandwich Islands',
                'SSD': 'South Sudan',
                'ESP': 'Spain',
                'LKA': 'Sri Lanka',
                'SDN': 'Sudan',
                'SUR': 'Suriname',
                'SJM': 'Svalbard and Jan Mayen Islands',
                'SWZ': 'Swaziland',
                'SWE': 'Sweden',
                'CHE': 'Switzerland',
                'SYR': 'Syrian Arab Republic (Syria)',
                'TWN': 'Taiwan, Republic of China',
                'TJK': 'Tajikistan',
                'TZA': 'Tanzania, United Republic of',
                'THA': 'Thailand',
                'TLS': 'Timor-Leste',
                'TGO': 'Togo',
                'TKL': 'Tokelau',
                'TGA': 'Tonga',
                'TRI': 'Trinidad and Tobago',
                'TUN': 'Tunisia',
                'TUR': 'Turkey',
                'TKM': 'Turkmenistan',
                'TCA': 'Turks and Caicos Islands',
                'TUV': 'Tuvalu',
                'UGA': 'Uganda',
                'UKR': 'Ukraine',
                'ARE': 'rn">United Arab Emirates',
                'GBR': 'United Kingdom',
                'USA': 'United States of America',
                'UMI': 'United States Minor Outlying Islands',
                'URY': 'Uruguay',
                'UZB': 'Uzbekistan',
                'VAN': 'Vanuatu',
                'VEN': 'Venezuela (Bolivarian Republic of)',
                'VNM': 'Viet Nam',
                'VIR': 'Virgin Islands, US',
                'WLF': 'Wallis and Futuna Islands',
                'ESH': 'Western Sahara',
                'YEM': 'Yemen',
                'ZMB': 'Zambia',
                'ZWE': 'Zimbabwe',
                'ZAI': 'Zaire',
                'URS': 'Soviet Union',
                'FRG': 'Germany FR',
                'YUG': 'Yugoslavia',
                'SCO': 'Scotland',
                'GDR': 'German DR',
                'NIR': 'Northern Ireland',
                'ENG': 'England',
                'KOR': 'Korean Republic',
                'TCH': 'Czechoslovakia',
                'WAL': 'Wales',
                'SCG': 'rn">Serbia and Montenegro',
                'NIG': 'Nigeria',
                'SEY': 'Seychellois',
                'GAM': 'Gambian',
                'INH': 'Dutch East Indies',
                'CUW': 'Curacao',
                'BER': 'Bermuda',
                'BHR': 'Bahrain',
                'NULL': 'No country',
                'OMN': 'Oman',
                'CHN': 'China',
                'TMP': 'No country'}

meal_dict = {'BB': 'Bed & Breakfast',
             'FB': 'Full board (breakfast, lunch and dinner)',
             'HB': 'Half board (breakfast and one other meal)',
             'SC': 'No meal',
             'Undefined': 'No meal'}

room_dict = {'A': 'Single Room',
             'B': 'Double Room',
             'C': 'Triple Room',
             'D': 'Quad Room',
             'E': 'Queen Room',
             'F': 'King Room',
             'G': 'Twin Room',
             'H': 'Studio',
             'I': 'Suite Room',
             'K': 'Apartment',
             'L': 'Villa',
             'P': 'Murphy Room'}

header = hotel_bookings[0]

hotel_bookings = hotel_bookings[1:]


def clean_data(remove_company, clean_country, clean_room, meal, kid, time):
    remove_company(hotel_bookings)
    clean_country(hotel_bookings)
    clean_room(hotel_bookings)
    meal(hotel_bookings)
    kid(hotel_bookings)
    time(hotel_bookings)


def clean_room(hotel_bookings):
    for row in hotel_bookings:
        row[19] = room_dict[row[19]]
        row[20] = room_dict[row[20]]


def remove_company(hotel_bookings):
    for row in hotel_bookings:
        del row[24]


def clean_country(hotel_bookings):
    for row in hotel_bookings:
        row[13] = country_dict[row[13]]


def meal(hotel_bookings):
    for row in hotel_bookings:
        row[12] = meal_dict[row[12]]


def kid(hotel_bookings):
    for row in hotel_bookings:
        if (row[10] == "NA"):
            row[10] = "0"
        else:
            row[10] = int(row[10]) + int(row[11])
        del row[11]


def time(hotel_bookings):
    for row in hotel_bookings:
        row[3] = row[3] + "/" + row[4] + "/" + row[6]
        del row[4]
        del row[4]
        del row[4]


clean_data(remove_company, clean_country, clean_room, meal, kid, time)

header = header[:4] + header[7:11] + header[12:24] + header[25:]
header[3] = "arrival_date"
header[7] = "kids"
hotel_bookings = list(filter(lambda row: True if row[19] != "NULL" else False, hotel_bookings))  # delete agent NULL
hotel_bookings = [header] + hotel_bookings

np.savetxt("hotel_bookings_cleaned.csv", hotel_bookings, fmt='%s', delimiter=',', newline='', encoding='utf8')
with open('hotel_bookings_cleaned.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in hotel_bookings:
        writer.writerow(row)