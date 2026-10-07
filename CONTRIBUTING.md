# Contributing

Thanks for improving Deployed Web QA.

## Before opening a change

- Keep `SKILL.md` focused on decisions and workflow guidance that materially improve deployed-web QA.
- Preserve the read-only default and the credential-handling rules.
- Prefer observable acceptance checks over subjective claims.
- Update the README when behavior, installation, or report format changes.
- Run `python3 scripts/validate_skill.py` locally.

## Pull requests

Pull requests should explain:

- the problem being solved;
- the change in skill behavior;
- any new safety or authorization boundary;
- how the change was validated.

Do not include passwords, tokens, private URLs, private screenshots, or customer data in commits or issue discussions.
