#!/usr/bin/env bash
brew tap sqitchers/sqitch
brew install sqitch --with-postgres-support
sqitch init ming --uri https://github.com/remingtonc/ming/ --engine pg