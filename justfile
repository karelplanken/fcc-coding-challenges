set dotenv-load := true

# Python environment ------------------------------------------------------------------

# Install from the lockfile.
install:
    uv sync --all-extras --all-groups

# Refresh the lockfile and sync (use when you intentionally want newer deps).
upgrade:
    uv lock --upgrade
    uv sync --all-extras --all-groups

# Code quality ------------------------------------------------------------------------
format *paths=".":
    uv run --frozen ruff check --fix {{ paths }}
    uv run --frozen ruff format {{ paths }}

check-ruff *paths=".":
    uv run --frozen ruff check {{ paths }}

check-types *paths=".":
    uv run --frozen mypy {{ paths }}

check-complexity *paths=".":
    uv run --frozen complexipy {{ paths }}

check-spelling *paths=".":
    uv run --frozen codespell {{ paths }}

# Fast check of what you're about to commit — run this routinely.
check-secrets:
    gitleaks protect --staged --source . --verbose

# Slower full commit-history audit — run occasionally, or before making a repo public.
check-secrets-history:
    gitleaks detect --source . --verbose

# Test --------------------------------------------------------------------------------
test target="":
    uv run --frozen pytest {{ target }} --cov --cov-report=term-missing

# Convenience bundle without test
check-no-test *paths=".": (check-ruff paths) (check-types paths) (check-complexity paths) (check-spelling paths)
    @echo "types + complexity + tests OK"

# Convenience bundle: what you'd run before committing.
check *paths=".": (check-ruff paths) (check-types paths) (check-complexity paths) (check-spelling paths) (test paths)
    @echo "types + complexity + tests OK"

# Project specific commands -----------------------------------------------------------

# One-off sanity check, not for routine use--------------------------------------------
check-types-verify:
    @uv run mypy -vv . 2>&1 | grep -E "Config File|'strict_equality'|'disallow_untyped_defs'"