# query = ['ENPH', 'PLAB', 'ON', 'ALNY', 'IMXI', 'KRTX', 'DY', 'DGII', 'SIGA', 'AZPN']
query = ['(^| )\$?([A-Z]{2,4})([\n\r\s]+|,)'] # all cap letters 2 to 4 consecutively, then space | newline | comma
# query = ['\$([A-Z]{2,})'] # must have $ symbol in front of the 2 or more consecutive cap letters
users = ['markminervini', 'raoulgmi', 'barrysilbert', 'kris_hk', 'melt_dem', 'adam3us', 'sergeynazarov', 'lightcrypto', 'gametheorizing',
         'arthur_0x', 'haralabob', 'vasilytrader', 'kunal00', 'SmartContracter', 'GiganticRebirth', 'pentosh1', 'timeless_crypto', 'crypto_iso',
         'edwardmorra_btc', 'hsakatrades', 'crediblecrypto', 'rektproof', 'lomahcrypto', 'traderkoz', 'donalt', 'crypto_chase', 'cyptocred', 'loomdart',
         '22loops', 'tradermayne', 'tradersz', 'cryptocapo', 'algodtrading', 'jimtalbot', 'bitbitcrypto', 'traderkoz', 'murocrypto', 'lsdinmycoffe',
         'pierre_crypt0', 'lrncrypt', 'inmortalcrypto']


# for every user, their max count of tweets can be fetched (pretty much useless unless they're spamming)
maxcount = 1000
# fetch from how long ago
mins_ago = 360
