## GitHub CLI Basics

### Issues

- Viewing all issues

```bash
gh issue list
```

- View a specific issue

	- Replace `n` with the actual issue number.

```bash
gh issue view n
```

- View a specific issue on the browser

```bash
gh issue view n -w
```

- Create issue

```bash
gh issue create
```


### Pull Requests

- View all pull requests

```bash
gh pr list
```

- View a specific pull request

```bash
gh pr view n
```

- Create a pull request

```bash
gh pr create
```

### Repository

- Clone a repository from GitHub

	- Replace `Owner-Name` with actual owner.
	- Replace `Repository-Name` with actual repository.

```bash
gh repo clone Owner-Name/Repository-Name
```

