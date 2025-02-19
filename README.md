# vscode-python-setup

This repositori contains configuration files for setting up a Python development environment in VSCode. It includes workspace settings and recommended 
extensions to streamline development.

The list of recommended extensions is saved in `.vscode/extensions.json`. It contains:
```json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.debugpy",
        "charliermarsh.ruff",
        "tamasfe.even-better-toml",
        "ms-python.mypy-type-checker",
        "njpwerner.autodocstring",
        "streetsidesoftware.code-spell-checker",
        "aaron-bond.better-comments",
        "davidanson.vscode-markdownlint",
        "janisdd.vscode-edit-csv",
        "vscode-icons-team.vscode-icons",
    ]
}
```

The VSCode workspace configuration file is saved in `.vscode/settings.json`. It contains:
```json
{
    "editor.rulers": [
        {
            "column": 72,
            "color": "green"
        },
        {
            "column": 120,
            "color": "blue"
        },
    ],
    "workbench.iconTheme": "vscode-icons",
    "git.openRepositoryInParentFolders": "always",
    "autoDocstring.docstringFormat": "numpy",
    "autoDocstring.startOnNewLine": true,
    "autoDocstring.includeExtendedSummary": true,
    "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        },
    },
    "mypy-type-checker.cwd": "${nearestConfig}"
}
```

To make sure that in other projects the ruff formatter is not used automatically with default settings, I recommend that it is disabled for user settings. To do this follow these steps:
1. Open `seetings`
2. Select `User tab
3. Search `@id:editor.defaultFormatter @lang:python formatter`
4. Select `None`

The liners settings are saved in `pyproject.toml`. It contains:
```toml
[tool.pytest.ini_options]
pythonpath = ["src"]

[tool.ruff]
line-length = 120
src = ["src", "test"]
target-version = "py38"

[tool.ruff.lint]
select = ["ALL"]
ignore = [
    "D203", # one-blank-line-before-class
    "D212", # summary line in docstrings will start with the second raw
    "D413", # not applicable for numpy docstrings
    "EM101", # raw-string-in-exception
    "EM102", # we want to use f string in exception messages
    "TRY003", # we want to write long exception messages
]

[tool.ruff.lint.pycodestyle]
max-doc-length = 72

[tool.mypy]
python_version = "3.8"
warn_return_any = true

```