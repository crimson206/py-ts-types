#!/bin/bash
set -e

cd ts_package
yarn
yarn build
yarn publish

