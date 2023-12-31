# Changelog

All notable changes to this project will be documented in this file.

## [0.3.2] - 2022-11-24

### Bug Fixes

- Add Requester to set_displayname

### Miscellaneous Tasks

- Bump version and update changelog

## [0.3.1] - 2022-11-24

### Bug Fixes

- Allow properly setting the displayname from the token
- Use ProfileHandler for display name

### Miscellaneous Tasks

- Bump version and update changelog

## [0.3.0] - 2022-11-23

### Bug Fixes

- Use correct method name for display name change

### Features

- Handle displayname claim

## [0.2.0] - 2022-11-22

### Features

- Check chatbox login localpart pattern

### Miscellaneous Tasks

- Bump version and update changelog

## [0.1.1] - 2022-10-04

### Miscellaneous Tasks

- Remove jwcrypto version limit

### Refactoring

- Switch to async await
- Use public ModuleApi methods

## [0.1.0] - 2022-09-21

### Bug Fixes

- Fix bug in test-cases surfaced by update in jwcrypto

### Features

- Handle admin claim in JWT
- Update admin status on login

### Miscellaneous Tasks

- [**breaking**] Rename to synapse_token_authenticator
- Update CODEOWNERS
- Package using hatch
- Reformat code and add job for checking in CI
- Add changelog

<!-- generated by git-cliff -->
