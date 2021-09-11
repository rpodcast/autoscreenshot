import pytest

from autoscreenshot import cli

def test_parser_dryrun():
    """
    Ensure the dry run option works
    """
    parser = cli.create_parser()

    args = parser.parse_args(["--dryrun"]) 
    assert args.dryrun == True