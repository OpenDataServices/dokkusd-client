# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2023-03-23

## Added

- nginx / client_max_body_size option - set by command line option or environmental variable.
- nginx / proxy-read-timeout option - set by command line option or environmental variable.
- Dokku app names are cleaned up. Invalid characters are changed to "-". Lower case is enforced.
- ps:scale - set by command line option or environmental variable.

## Changed

- nginx / client_max_body_size option - setting this by app.json is deprecated and will be removed in a later version.


## Fixed

- When creating new git remote name, check it does not already exist. If it does, add random numbers to name.

## [0.4.0] - 2022-11-18

## Added

- nginx / client_max_body_size option

## Fixed

- JSON typo in docs

## [0.3.0] - 2022-11-05

## Added

- environmentvariablesprefixedby option
- keep_git_dir option

## [0.2.0] - 2022-11-01

## Changed

- Force push when deploying

## [0.1.0] - 2022-10-04

First release with changelog
