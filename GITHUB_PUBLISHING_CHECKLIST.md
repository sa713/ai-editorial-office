# GitHub Publishing Checklist

Before publishing this project to GitHub:

- [ ] Create the GitHub repository only as `private`.
- [ ] Review `.gitignore`.
- [ ] Confirm there are no `.env` files, keys, tokens, certificates, or secrets.
- [ ] Confirm there are no internal documents that must stay outside GitHub.
- [ ] Confirm there is no personal data.
- [ ] Confirm there are no working materials that cannot be stored outside the
  corporate perimeter.
- [ ] Confirm large binary/source files are intentionally excluded or separately
  approved.
- [ ] Confirm `AGENTS.md` remains canonical.
- [ ] Confirm review-gate has not been changed.
- [ ] Before any push, manually review `git status` and `git diff`.
