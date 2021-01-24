#!/usr/bin/env python3

import json
import os

from swap.cli.__main__ import main as cli_main
from swap.utils import clean_transaction_raw

# Test Values
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "..", "values.json"))
values = open(file_path, "r")
_ = json.loads(values.read())
values.close()


def test_vapor_cli_refund(cli_tester):

    refund = cli_tester.invoke(
        cli_main, [
            "vapor",
            "refund",
            "--address", _["vapor"]["wallet"]["sender"]["address"],
            "--transaction-id", _["vapor"]["transaction_id"],
            "--asset", _["vapor"]["asset"],
            "--amount", _["vapor"]["amount"],
            "--max-amount", _["vapor"]["max_amount"],
            "--unit", _["vapor"]["unit"],
            "--network", _["vapor"]["network"]
        ]
    )

    assert refund.exit_code == 0
    assert refund.output == clean_transaction_raw(
        transaction_raw=_["vapor"]["refund"]["unsigned"]["transaction_raw"]
    ) + "\n"
