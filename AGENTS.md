# HookahTree delivery

This site's landing page automatically opens `catalog_retail_2024_02.pdf`.
The PDF is a required, tracked public asset. Never treat a 200 response from
`index.html` as proof that the site works: verify the redirect destination,
fallback link, PDF content type and full-file SHA-256 on both public hostnames.

For authorized changes: run `python3 scripts/check_catalog.py`, commit only
task files, push to `origin main`, wait for **Deploy to Netcup**, and run the
same checker with `--url https://hookahtree.ru/` and
`--url https://www.hookahtree.ru/` from the workstation. Do not use forced-IP
requests as the only public check. Never modify release contents manually on
the server, deploy to SimpleCloud, or include unrelated changes in a commit.

The restricted release handler belongs to `ampleev-infra`; application CI
must not change host configuration or receive the administrator SSH key.
