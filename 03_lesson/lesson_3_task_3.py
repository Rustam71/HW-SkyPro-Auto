from Address import Address
from Mailing import Mailing
to_address = Address('422332', 'Moscow', 'Lubyanka', '55', '213')
from_address = Address('231456', 'Kazan', 'River st.', '100', '11')
ZAKAZ = Mailing(to_address, from_address, 2000, 'TRACKNUM 16544234')
print(ZAKAZ)