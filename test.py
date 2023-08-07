from wooey import *
import argparse

@wooey
def cli(args):
    """_summary_
    Hello
    - a
    - b
    """
    parser = argparse.ArgumentParser(description='generates and sends request to the server based on the provided arguments')
    subparser = parser.add_subparsers(dest='request', required=True)

    new_release = subparser.add_parser('new_release')
    show_release = subparser.add_parser('show_release')
    deploy_release = subparser.add_parser('deploy_release')
    abort_release = subparser.add_parser('abort_release')
    revert_release = subparser.add_parser('revert_release')
    show_filter = subparser.add_parser('show_filter')
    
    subsub_parser = show_filter.add_subparsers(dest='filter', required=True)
    filter_show_filter = subsub_parser.add_parser('filter')
    
    new_release.add_argument('-r', '--release', help='Eg: release.ag-test3.20230611.1735', metavar='Release Name')
    new_release.add_argument('-t', '--token', help='Eg: dev-name.<src-bin-name>.date.time', metavar='Token')
    new_release.add_argument('-a', '--add_config_parameter', help='Eg: "[SECTION]KEY=VALUE" "KEY=VALUE"', nargs='*', metavar='Add Key to Section')
    new_release.add_argument('-d', '--delete_config_parameter', help='Eg: "[SECTION]KEY" "KEY"', nargs='*', metavar='Delete Key from Section')
    new_release.add_argument('-m', '--modify_config_parameter', help='Eg: "[SECTION]KEY=VALUE" "KEY=VALUE"', nargs='*', metavar='Modify Key in Section')
    new_release.add_argument('-b', '--binary', type=str, help='Eg: app.flavor.date.time (used for renaming a binary if token is provided, else for changing only configs)', nargs='*', metavar='Filter on basis of Binary Name')
    new_release.add_argument('-n', '--hostname', help='Eg: ti-*-* for all \'ti\' machines,  ti-nse-* ti-bse-* for all machines of \'ti\' at nse OR bse', nargs='*', metavar='Filter on basis of Machine')
    new_release.add_argument('-c', '--config_parameters', help='Eg: "[*]KEY=*" "KEY=*"', nargs='*', metavar='Filter on basis of Config Parameters')

    group = show_release.add_mutually_exclusive_group(required=True)
    group.add_argument('-r', '--release', help='Eg: release.ag-test3.20230611.1735', metavar='Release Name')
    group.add_argument('-m', '--machine', help='Eg: ti-cschkx2-psr01', metavar='Machine Name')

    deploy_release.add_argument('-r', '--release',  help='Eg: release.ag-test3.20230611.1735', required=True, metavar='Release Name')
    deploy_release.add_argument('-n', '--hostname', help='Eg: ti-*-* for all \'ti\' machines,  ti-nse-* ti-bse-* for all machines of \'ti\' at nse OR bse', nargs='*', metavar='Filter on basis of Machine')

    abort_release.add_argument('-r', '--release',  help='Eg: release.ag-test3.20230611.1735', required=True, metavar='Release Name')

    revert_release.add_argument('-r', '--release',  help='Eg: release.ag-test3.20230611.1735', required=True, metavar='Release Name')
    revert_release.add_argument('-n', '--hostname', help='Eg: ti-*-* for all \'ti\' machines,  ti-nse-* ti-bse-* for all machines of \'ti\' at nse OR bse', nargs='*', metavar='Filter on basis of Machine')

    filter_show_filter.add_argument('-b', '--binary', type=str, help='Eg: app.flavor.date.time', nargs='*', metavar='Filter on basis of Binary Name')
    filter_show_filter.add_argument('-n', '--hostname', help='Eg: ti-*-* for all \'ti\' machines,  ti-nse-* ti-bse-* for all machines of \'ti\' at nse OR bse', nargs='*', metavar='Filter on basis of Machine')
    filter_show_filter.add_argument('-c', '--config_parameters', help='Eg: [*]KEY=* KEY=*', nargs='*', metavar='Filter on basis of Config Parameters')
    
    args = parser.parse_args()
    print(args)

cli("new_release -r release.ag-test3.20230611.1735 -t dev-name.app.flavor.date.time -a '[SECTION]KEY=VALUE' 'KEY=VALUE' -d '[SECTION]KEY' 'KEY' -m '[SECTION]KEY=VALUE' 'KEY=VALUE' -b app.flavor.date.time -n 'ti-*-*' -c '[*]KEY=*' 'KEY=*'")