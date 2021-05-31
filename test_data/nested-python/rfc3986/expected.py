scheme = '[a-zA-Z][a-zA-Z0-9+\\-.]*'
port = '[0-9]*'
unreserved = '[a-zA-Z0-9\\-._~]'
pct_encoded = '%[0-9A-Fa-f][0-9A-Fa-f]'
sub_delims = "[!$&'()*+,;=]"
h16 = '[0-9A-Fa-f]{1,4}'
dec_octet = '([0-9]|[1-9][0-9]|1[0-9]{2,2}|2[0-4][0-9]|25[0-5])'
gen_delims = '[:/?#\\[\\]@]'
reserved = f'({gen_delims}|{sub_delims})'
ipv4address = f'{dec_octet}\\.{dec_octet}\\.{dec_octet}\\.{dec_octet}'
userinfo = f'({unreserved}|{pct_encoded}|{sub_delims}|:)*'
reg_name = f'({unreserved}|{pct_encoded}|{sub_delims})*'
ipvfuture = f'[vV][0-9A-Fa-f]{{1,}}\\.({unreserved}|{sub_delims}|:){{1,}}'
segment_nz_nc = f'({unreserved}|{pct_encoded}|{sub_delims}|@){{1,}}'
pchar = f'({unreserved}|{pct_encoded}|{sub_delims}|[:@])'
ls32 = f'({h16}:{h16}|{ipv4address})'
query = f'({pchar}|[/?])*'
fragment = f'({pchar}|[/?])*'
path_empty = f'({pchar}){{0,0}}'
segment = f'({pchar})*'
segment_nz = f'({pchar}){{1,}}'
ipv6address = (
    f'(({h16}:){{6,6}}{ls32}|::({h16}:){{5,5}}{ls32}|({h16})?::({h16}'
    f':){{4,4}}{ls32}|(({h16}:)?{h16})?::({h16}:){{3,3}}{ls32}|(({h16}'
    f':){{2}}{h16})?::({h16}:){{2,2}}{ls32}|(({h16}:){{3}}{h16})?::{h16}:'
    f'{ls32}|(({h16}:){{4}}{h16})?::{ls32}|(({h16}:){{5}}{h16})?::{h16}|'
    f'(({h16}:){{6}}{h16})?::)'
)
path_absolute = f'/({segment_nz}(/{segment})*)?'
path_rootless = f'{segment_nz}(/{segment})*'
path_abempty = f'(/{segment})*'
path_noscheme = f'{segment_nz_nc}(/{segment})*'
ip_literal = f'\\[({ipv6address}|{ipvfuture})\\]'
path = (
    f'({path_abempty}|{path_absolute}|{path_noscheme}|{path_rootless}|'
    f'{path_empty})'
)
host = f'({ip_literal}|{ipv4address}|{reg_name})'
authority = f'({userinfo}@)?{host}(:{port})?'
hier_part = (
    f'(//{authority}{path_abempty}|{path_absolute}|{path_rootless}|'
    f'{path_empty})'
)
relative_part = (
    f'(//{authority}{path_abempty}|{path_absolute}|'
    f'{path_noscheme}|{path_empty})'
)
relative_ref = f'{relative_part}(\\?{query})?(\\#{fragment})?'
uri = f'{scheme}:{hier_part}(\\?{query})?(\\#{fragment})?'
absolute_uri = f'{scheme}:{hier_part}(\\?{query})?'
uri_reference = f'({uri}|{relative_ref})'
