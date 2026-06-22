#!/usr/bin/env bash
# Lokale build: Hugo + Pagefind, met dezelfde stappen als de CI.
# Gebruik:  ./scripts/build.sh          (productie-baseURL uit hugo.toml)
#           ./scripts/build.sh local    (baseURL=http://localhost:8088/ voor lokaal serveren)
set -euo pipefail
cd "$(dirname "$0")/.."

BASEURL_ARG=()
if [[ "${1:-}" == "local" ]]; then
  BASEURL_ARG=(--baseURL "http://localhost:8088/")
fi

rm -rf public
hugo --minify --gc "${BASEURL_ARG[@]}"

# Pagefind: gebruik de globale binary indien aanwezig, anders npx.
if command -v pagefind >/dev/null 2>&1; then
  pagefind --site public
else
  npx -y pagefind --site public
fi

echo
echo "Klaar. Serveer lokaal met:"
echo "  python3 -m http.server 8088 --directory public"
