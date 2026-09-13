.PHONY: install-hook

install-hook:
	git_root=$$(git rev-parse --show-toplevel); \
	install -m 755 pre-commit "$$git_root/.git/hooks/pre-commit"

all: install-hook
