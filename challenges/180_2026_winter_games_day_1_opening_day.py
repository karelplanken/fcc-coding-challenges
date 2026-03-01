# Daily Coding challenge #180 (2026-02-06) - freeCodeCamp.org
# 2026 Winter Games Day 1: Opening Day
# Today marks the start of the 2026 Winter Games. The next 17 days will bring you coding
# challenges inspired by them.

# For the first one, you are given a two-letter country code and need to return the flag
# emoji for that country.

# Use this list:

# Country	Code	Flag
# Albania	"AL"	"🇦🇱"
# Andorra	"AD"	"🇦🇩"
# Argentina	"AR"	"🇦🇷"
# Armenia	"AM"	"🇦🇲"
# Australia	"AU"	"🇦🇺"
# Austria	"AT"	"🇦🇹"
# Azerbaijan	"AZ"	"🇦🇿"
# Belgium	"BE"	"🇧🇪"
# Benin	"BJ"	"🇧🇯"
# Bolivia	"BO"	"🇧🇴"
# Bosnia and Herzegovina	"BA"	"🇧🇦"
# Brazil	"BR"	"🇧🇷"
# Bulgaria	"BG"	"🇧🇬"
# Canada	"CA"	"🇨🇦"
# Chile	"CL"	"🇨🇱"
# China	"CN"	"🇨🇳"
# Colombia	"CO"	"🇨🇴"
# Croatia	"HR"	"🇭🇷"
# Cyprus	"CY"	"🇨🇾"
# Czech Republic	"CZ"	"🇨🇿"
# Denmark	"DK"	"🇩🇰"
# Ecuador	"EC"	"🇪🇨"
# Eritrea	"ER"	"🇪🇷"
# Estonia	"EE"	"🇪🇪"
# Finland	"FI"	"🇫🇮"
# France	"FR"	"🇫🇷"
# Georgia	"GE"	"🇬🇪"
# Germany	"DE"	"🇩🇪"
# Great Britain	"GB"	"🇬🇧"
# Greece	"GR"	"🇬🇷"
# Guinea-Bissau	"GW"	"🇬🇼"
# Haiti	"HT"	"🇭🇹"
# Hong Kong	"HK"	"🇭🇰"
# Hungary	"HU"	"🇭🇺"
# Iceland	"IS"	"🇮🇸"
# India	"IN"	"🇮🇳"
# Iran	"IR"	"🇮🇷"
# Ireland	"IE"	"🇮🇪"
# Israel	"IL"	"🇮🇱"
# Italy	"IT"	"🇮🇹"
# Jamaica	"JM"	"🇯🇲"
# Japan	"JP"	"🇯🇵"
# Kazakhstan	"KZ"	"🇰🇿"
# Kenya	"KE"	"🇰🇪"
# Kosovo	"XK"	"🇽🇰"
# Kyrgyzstan	"KG"	"🇰🇬"
# Latvia	"LV"	"🇱🇻"
# Lebanon	"LB"	"🇱🇧"
# Liechtenstein	"LI"	"🇱🇮"
# Lithuania	"LT"	"🇱🇹"
# Luxembourg	"LU"	"🇱🇺"
# Madagascar	"MG"	"🇲🇬"
# Malaysia	"MY"	"🇲🇾"
# Malta	"MT"	"🇲🇹"
# Mexico	"MX"	"🇲🇽"
# Moldova	"MD"	"🇲🇩"
# Monaco	"MC"	"🇲🇨"
# Mongolia	"MN"	"🇲🇳"
# Montenegro	"ME"	"🇲🇪"
# Morocco	"MA"	"🇲🇦"
# Netherlands	"NL"	"🇳🇱"
# New Zealand	"NZ"	"🇳🇿"
# Nigeria	"NG"	"🇳🇬"
# North Macedonia	"MK"	"🇲🇰"
# Norway	"NO"	"🇳🇴"
# Pakistan	"PK"	"🇵🇰"
# Philippines	"PH"	"🇵🇭"
# Poland	"PL"	"🇵🇱"
# Portugal	"PT"	"🇵🇹"
# Puerto Rico	"PR"	"🇵🇷"
# Romania	"RO"	"🇷🇴"
# San Marino	"SM"	"🇸🇲"
# Saudi Arabia	"SA"	"🇸🇦"
# Serbia	"RS"	"🇷🇸"
# Singapore	"SG"	"🇸🇬"
# Slovakia	"SK"	"🇸🇰"
# Slovenia	"SI"	"🇸🇮"
# South Africa	"ZA"	"🇿🇦"
# South Korea	"KR"	"🇰🇷"
# Spain	"ES"	"🇪🇸"
# Sweden	"SE"	"🇸🇪"
# Switzerland	"CH"	"🇨🇭"
# Thailand	"TH"	"🇹🇭"
# Trinidad & Tobago	"TT"	"🇹🇹"
# Turkey	"TR"	"🇹🇷"
# Ukraine	"UA"	"🇺🇦"
# United Arab Emirates	"AE"	"🇦🇪"
# United States	"US"	"🇺🇸"
# Uruguay	"UY"	"🇺🇾"
# Uzbekistan	"UZ"	"🇺🇿"
# Venezuela	"VE"	"🇻🇪"
from dataclasses import dataclass, field
from types import MappingProxyType

from pytest import mark


@dataclass(frozen=True)
class Country:
    name: str
    code: str
    flag: str = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            'flag',
            ''.join(chr(0x1F1E6 + ord(char) - ord('A')) for char in self.code.upper()),
        )

COUNTRIES = MappingProxyType(
    {
        'AL': Country(name='Albania', code='AL'),
        'AD': Country(name='Andorra', code='AD'),
        'AR': Country(name='Argentina', code='AR'),
        'AM': Country(name='Armenia', code='AM'),
        'AU': Country(name='Australia', code='AU'),
        'AT': Country(name='Austria', code='AT'),
        'AZ': Country(name='Azerbaijan', code='AZ'),
        'BE': Country(name='Belgium', code='BE'),
        'BJ': Country(name='Benin', code='BJ'),
        'BO': Country(name='Bolivia', code='BO'),
        'BA': Country(name='Bosnia and Herzegovina', code='BA'),
        'BR': Country(name='Brazil', code='BR'),
        'BG': Country(name='Bulgaria', code='BG'),
        'CA': Country(name='Canada', code='CA'),
        'CL': Country(name='Chile', code='CL'),
        'CN': Country(name='China', code='CN'),
        'CO': Country(name='Colombia', code='CO'),
        'HR': Country(name='Croatia', code='HR'),
        'CY': Country(name='Cyprus', code='CY'),
        'CZ': Country(name='Czech Republic', code='CZ'),
        'DK': Country(name='Denmark', code='DK'),
        'EC': Country(name='Ecuador', code='EC'),
        'ER': Country(name='Eritrea', code='ER'),
        'EE': Country(name='Estonia', code='EE'),
        'FI': Country(name='Finland', code='FI'),
        'FR': Country(name='France', code='FR'),
        'GE': Country(name='Georgia', code='GE'),
        'DE': Country(name='Germany', code='DE'),
        'GB': Country(name='Great Britain', code='GB'),
        'GR': Country(name='Greece', code='GR'),
        'GW': Country(name='Guinea-Bissau', code='GW'),
        'HT': Country(name='Haiti', code='HT'),
        'HK': Country(name='Hong Kong', code='HK'),
        'HU': Country(name='Hungary', code='HU'),
        'IS': Country(name='Iceland', code='IS'),
        'IN': Country(name='India', code='IN'),
        'IR': Country(name='Iran', code='IR'),
        'IE': Country(name='Ireland', code='IE'),
        'IL': Country(name='Israel', code='IL'),
        'IT': Country(name='Italy', code='IT'),
        'JM': Country(name='Jamaica', code='JM'),
        'JP': Country(name='Japan', code='JP'),
        'KZ': Country(name='Kazakhstan', code='KZ'),
        'KE': Country(name='Kenya', code='KE'),
        'XK': Country(name='Kosovo', code='XK'),
        'KG': Country(name='Kyrgyzstan', code='KG'),
        'LV': Country(name='Latvia', code='LV'),
        'LB': Country(name='Lebanon', code='LB'),
        'LI': Country(name='Liechtenstein', code='LI'),
        'LT': Country(name='Lithuania', code='LT'),
        'LU': Country(name='Luxembourg', code='LU'),
        'MG': Country(name='Madagascar', code='MG'),
        'MY': Country(name='Malaysia', code='MY'),
        'MT': Country(name='Malta', code='MT'),
        'MX': Country(name='Mexico', code='MX'),
        'MD': Country(name='Moldova', code='MD'),
        'MC': Country(name='Monaco', code='MC'),
        'MN': Country(name='Mongolia', code='MN'),
        'ME': Country(name='Montenegro', code='ME'),
        'MA': Country(name='Morocco', code='MA'),
        'NL': Country(name='Netherlands', code='NL'),
        'NZ': Country(name='New Zealand', code='NZ'),
        'NG': Country(name='Nigeria', code='NG'),
        'MK': Country(name='North Macedonia', code='MK'),
        'NO': Country(name='Norway', code='NO'),
        'PK': Country(name='Pakistan', code='PK'),
        'PH': Country(name='Philippines', code='PH'),
        'PL': Country(name='Poland', code='PL'),
        'PT': Country(name='Portugal', code='PT'),
        'PR': Country(name='Puerto Rico', code='PR'),
        'RO': Country(name='Romania', code='RO'),
        'SM': Country(name='San Marino', code='SM'),
        'SA': Country(name='Saudi Arabia', code='SA'),
        'RS': Country(name='Serbia', code='RS'),
        'SG': Country(name='Singapore', code='SG'),
        'SK': Country(name='Slovakia', code='SK'),
        'SI': Country(name='Slovenia', code='SI'),
        'ZA': Country(name='South Africa', code='ZA'),
        'KR': Country(name='South Korea', code='KR'),
        'ES': Country(name='Spain', code='ES'),
        'SE': Country(name='Sweden', code='SE'),
        'CH': Country(name='Switzerland', code='CH'),
        'TH': Country(name='Thailand', code='TH'),
        'TT': Country(name='Trinidad & Tobago', code='TT'),
        'TR': Country(name='Turkey', code='TR'),
        'UA': Country(name='Ukraine', code='UA'),
        'AE': Country(name='United Arab Emirates', code='AE'),
        'US': Country(name='United States', code='US'),
        'UY': Country(name='Uruguay', code='UY'),
        'UZ': Country(name='Uzbekistan', code='UZ'),
        'VE': Country(name='Venezuela', code='VE'),
    }
)


def get_flag(code: str) -> str:
    return COUNTRIES[code].flag


tests = [
    ('AL', '🇦🇱'),
    ('AD', '🇦🇩'),
    ('AR', '🇦🇷'),
    ('AM', '🇦🇲'),
    ('AU', '🇦🇺'),
    ('AT', '🇦🇹'),
    ('AZ', '🇦🇿'),
    ('BE', '🇧🇪'),
    ('BJ', '🇧🇯'),
    ('BO', '🇧🇴'),
    ('BA', '🇧🇦'),
    ('BR', '🇧🇷'),
    ('BG', '🇧🇬'),
    ('CA', '🇨🇦'),
    ('CL', '🇨🇱'),
    ('CN', '🇨🇳'),
    ('CO', '🇨🇴'),
    ('HR', '🇭🇷'),
    ('CY', '🇨🇾'),
    ('CZ', '🇨🇿'),
    ('DK', '🇩🇰'),
    ('EC', '🇪🇨'),
    ('ER', '🇪🇷'),
    ('EE', '🇪🇪'),
    ('FI', '🇫🇮'),
    ('FR', '🇫🇷'),
    ('GE', '🇬🇪'),
    ('DE', '🇩🇪'),
    ('GB', '🇬🇧'),
    ('GR', '🇬🇷'),
    ('GW', '🇬🇼'),
    ('HT', '🇭🇹'),
    ('HK', '🇭🇰'),
    ('HU', '🇭🇺'),
    ('IS', '🇮🇸'),
    ('IN', '🇮🇳'),
    ('IR', '🇮🇷'),
    ('IE', '🇮🇪'),
    ('IL', '🇮🇱'),
    ('IT', '🇮🇹'),
    ('JM', '🇯🇲'),
    ('JP', '🇯🇵'),
    ('KZ', '🇰🇿'),
    ('KE', '🇰🇪'),
    ('XK', '🇽🇰'),
    ('KG', '🇰🇬'),
    ('LV', '🇱🇻'),
    ('LB', '🇱🇧'),
    ('LI', '🇱🇮'),
    ('LT', '🇱🇹'),
    ('LU', '🇱🇺'),
    ('MG', '🇲🇬'),
    ('MY', '🇲🇾'),
    ('MT', '🇲🇹'),
    ('MX', '🇲🇽'),
    ('MD', '🇲🇩'),
    ('MC', '🇲🇨'),
    ('MN', '🇲🇳'),
    ('ME', '🇲🇪'),
    ('MA', '🇲🇦'),
    ('NL', '🇳🇱'),
    ('NZ', '🇳🇿'),
    ('NG', '🇳🇬'),
    ('MK', '🇲🇰'),
    ('NO', '🇳🇴'),
    ('PK', '🇵🇰'),
    ('PH', '🇵🇭'),
    ('PL', '🇵🇱'),
    ('PT', '🇵🇹'),
    ('PR', '🇵🇷'),
    ('RO', '🇷🇴'),
    ('SM', '🇸🇲'),
    ('SA', '🇸🇦'),
    ('RS', '🇷🇸'),
    ('SG', '🇸🇬'),
    ('SK', '🇸🇰'),
    ('SI', '🇸🇮'),
    ('ZA', '🇿🇦'),
    ('KR', '🇰🇷'),
    ('ES', '🇪🇸'),
    ('SE', '🇸🇪'),
    ('CH', '🇨🇭'),
    ('TH', '🇹🇭'),
    ('TT', '🇹🇹'),
    ('TR', '🇹🇷'),
    ('UA', '🇺🇦'),
    ('AE', '🇦🇪'),
    ('US', '🇺🇸'),
    ('UY', '🇺🇾'),
    ('UZ', '🇺🇿'),
    ('VE', '🇻🇪'),
]


@mark.parametrize('code, expected', tests)
def test_get_flag(code: str, expected: str) -> None:
    assert get_flag(code) == expected


if __name__ == '__main__':
    code, expected = tests[0]
    print(get_flag(code))
