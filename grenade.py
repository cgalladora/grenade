#!/usr/bin/env python
from netaddr import IPNetwork, IPSet
from scapy.all import rdpcap, wrpcap

# ## GENERAL USAGE:
#
#     grenade.py [options] <input PCAP> <output PCAP>
#
# Example:
#
#     $ grenade.py --src-ip 127.3.4.0/16 input.pcap output.pcap
#     input....... 14
#     fragmented.. 4
#     dropped..... 10
#     fragments... 16 
#     output...... 16


# ## FILTERING PACKETS:
# The arguments passed to --src-ip and --dst-ip can be in any of the following formats:
# - Plain IP address (i.e. 127.3.4.14)
# - CIDR Netmask (i.e. 243.7.234.3/24)
# - IP Glob Expression (i.e. 27.*.3.*)
# - IP Range Expression (i.e. 225.43.2.1-19)


class Count:
    def __init__(self):
        self._counts = {}


    def __getattr__(self, attr):
        try:
            self._counts[attr] += 1
        except KeyError:
            self._counts[attr] = 1


    def summary(self, keys=None):
        if keys is None:
            return self._counts
        else:
            return dict(self._counts,
                        **{key: 0 for key in keys if key not in self._counts})


def process(packets, config):
    frag = config["frag_size"]
    drop = config["drop_unmatched"]
    if config["src_ip"]:
        src = IPSet(IPNetwork(config["src_ip"]))
    else:
        src = None

    if config["dst_ip"]:
        dst = IPSet(IPNetwork(config["dst_ip"]))
    else:
        dst = None

    counter = Count()

    for pkt in packets:
        counter.input
        if (src and pkt not in src) or (dst and pkt not in dst):
            if not drop:
                counter.output
                yield pkt
            else:
                counter.dropped
        else:
            counter.fragmented
            for p in pkt.fragment(frag):
                counter.fragments
                counter.output
                yield p


    # For diagnostics
    if not config.get("quiet", False):
        keys = ["input", "fragmented", "dropped", "fragments", "output"]
        summary = counter.summary(keys)
        for key in keys:
            print "{:.<12} {}".format(key, summary[key])


def get_parser():
    import argparse
    parser = argparse.ArgumentParser(
        description="Packet fragmenter",
        epilog=EPILOG
        )
    parser.add_argument("input", help="Input pcap file")
    parser.add_argument("output", help="Output pcap file")
    parser.add_argument("--src-ip", metavar="NETMASK",
                        help="Filter packets by source IP address")
    parser.add_argument("--dst-ip", metavar="NETMASK",
                        help="Filter packets by destination IP address")
    parser.add_argument("-f", "--frag-size", type=int, 
                        default="576", help="Fragment size")
    parser.add_argument("-D", "--drop-unmatched", action="store_true",
                        help="Discard packets not matched by --src-ip or --dst-ip")
    return parser


def main():
    config = vars(get_parser().parse_args())
    pcap = rdpcap(config["input"])
    fragmented = process(pcap, config)
    wrpcap(config["output"], fragmented)


if __name__ == "__main__":
    main()
