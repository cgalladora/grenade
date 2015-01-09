# Grenade
IP Fragmentation utility for pcaps

## General Usage

    grenade.py [options] <input PCAP> <output PCAP>

Example:

    $ grenade.py --src-ip 127.3.4.0/16 input.pcap output.pcap
    input....... 14
    fragmented.. 4
    dropped..... 10
    fragments... 16 
    output...... 16


## Filtering Packets
The arguments passed to `--src-ip` and `--dst-ip` can be in any of the following formats:
- Plain IP address (i.e. `127.3.4.14`)
- CIDR Netmask (i.e. `243.7.234.3/24`)
- IP Glob Expression (i.e. `27.*.3.*`)
- IP Range Expression (i.e. `225.43.2.1-19`)

## Installation
Simply do

    $ ./setup.py install

Or, if you already have the dependencies installed, 
you can run the `grenade.py` script directly, without installation.

    $ python /path/to/grenade.py [options] <arguments...>

### Dependencies
Dependencies are listed under `setup.py` in the `install_requires` setup parameter:
- netaddr (version >= `0.7.12` recommended)
- scapy (version >= `2.3.1` recommended)

IPv6 is currently not supported

