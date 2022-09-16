#!/bin/bash
# Deployment script

set -e
make_live="false"
version=${USER}`cat /dev/random | LC_CTYPE=C tr -dc "[:lower:][:digit:]" | head -c 8`
while [ $# -gt 0 ]; do
  case "$1" in
    --version=*)
      version="${1#*=}"
      ;;
    --make-live=*)
      make_live="${1#*=}"
      ;;
    --project=*)
      project="${1#*=}"
      ;;
    *)
      printf "***************************\n"
      printf "* Error: Invalid argument.*\n"
      printf "***************************\n"
      exit 1
  esac
  shift
done

CMD="gcloud app deploy  --version $version --project=$project"
if [ \( "$make_live" = "false" \) ]; then
  CMD="${CMD} --no-promote"
fi

echo "CMD: ${CMD}"
`$CMD`
