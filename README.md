# Grenade
IP Fragmentation utility for pcaps

## GENERAL USAGE:

    grenade.py [options] <input PCAP> <output PCAP>

Example:

    $ grenade.py --src-ip 127.3.4.0/16 input.pcap output.pcap
    input....... 14
    fragmented.. 4
    dropped..... 10
    fragments... 16 
    output...... 16


## FILTERING PACKETS:
The arguments passed to `--src-ip` and `--dst-ip` can be in any of the following formats:
- Plain IP address (i.e. `127.3.4.14`)
- CIDR Netmask (i.e. `243.7.234.3/24`)
- IP Glob Expression (i.e. `27.*.3.*`)
- IP Range Expression (i.e. `225.43.2.1-19`)

IPv6 is currently not supported

