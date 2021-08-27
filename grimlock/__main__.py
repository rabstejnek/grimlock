from gooey import Gooey, GooeyParser

from grimlock import commands


@Gooey(clear_before_run=True, program_name="grimlock")
def main():
    parser = GooeyParser(description="")
    subparsers = parser.add_subparsers()

    # Add hello world command
    parser_hello = subparsers.add_parser("hello_world", prog="Hello, World!")
    parser_hello.set_defaults(func=commands.hello_world)

    # Add excel to json command
    parser_etj = subparsers.add_parser("excel_to_json", prog="Excel to JSON")
    parser_etj.add_argument("input", metavar="Excel file", help="", widget="FileChooser")
    parser_etj.set_defaults(func=commands.excel_to_json)

    args = parser.parse_args()
    print(args.func(args))


main()
