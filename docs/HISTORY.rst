Changelog
=========

1.1.1 (unreleased)
------------------

- Nothing changed yet.


1.1.0 (2017-07-27)
------------------

New features:

- Fix code for Python 3 compatiblity.
  [cas--]


1.0.0 (2017-07-20)
------------------

Breaking changes:

- Fix bug: Values containing variable substitution syntax breaks things. This is a breaking change
  because problematic values are escaped, eg. "${foo}" becomes "$${foo}".

0.2.0 (2012-08-21)
------------------

- Now it's possible to read environment variables.

0.1b1 (2011-08-18)
------------------

- First release.
