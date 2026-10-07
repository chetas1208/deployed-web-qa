# Security Policy

## Reporting a vulnerability

Please do not open a public issue for security-sensitive findings. Contact the repository maintainer privately through the GitHub security-advisory workflow or the maintainer's verified GitHub contact channel.

Include:

- a concise description;
- affected files or behavior;
- safe reproduction steps that do not expose credentials or private data;
- impact and suggested mitigation, if known.

## Credential handling

This skill must never request, store, print, commit, or screenshot passwords, API keys, session cookies, or tokens beyond what is necessary for an explicitly authorized login flow. Test credentials should be seeded, scoped, and disposable whenever possible.
