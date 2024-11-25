import argparse, json, pyotp
from pathlib import Path

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--codes', required=True, type=Path)
    parser.add_argument('-s', '--site', required=False, type=str)
    return parser.parse_args()

def main():
    args = get_args()
    with args.codes.open() as f:
        totp_d = json.load(f)

    if args.site:
        site = args.site
        if site in totp_d:
            secret = totp_d[site].replace(' ', '')
            totp = pyotp.TOTP(secret).now()
            print(totp, 'for', site)
        else:
            possible_sites = [k for k in totp_d.keys() if k.startswith(site)]
            poss_len = len(possible_sites)
            if poss_len == 1:
                secret = totp_d[possible_sites[0]].replace(' ', '')
                totp = pyotp.TOTP(secret).now()
                print(totp, 'for', possible_sites[0])
            elif poss_len == 0:
                print('No site found')
            else:
                print('Multiple sites found:')
                for site in possible_sites:
                    print('\t' + site)
    else:
        print('Please specify a site with -s or --site')
        print('Available sites: ' + ', '.join(totp_d.keys()))

if __name__ == '__main__':
    main()