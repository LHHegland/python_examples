# python_examples

**NAMESPACE:** me.hegland-lance

**PURPOSE:** Practice using VSCode, Markdown, Python, Git, and GitHub tools while testing development environment installation and configuration.

.

## Table of Contents

- [Features](#features)
- [Background](#background)
- [Known Issues](#known-issues)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Authors](#authors)
- [Roadmap](#roadmap)
- [License](#license)

.

## **Features**

Hands-on practice and testing of Python, VSCode, Git, and GitHub tools (i.e. experiential learning) that is relatively quick and easy plus offers reusable code modules, including the following:

- creating local and remote GitHub repositories
- using the following Git features
   | Command | Tutorial | Git Ref |
   |---------|----------|---------|
   | clone | [Link](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) | [Link](https://git-scm.com/docs/git-clone) |
   | init | [Link](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-init) | [Link](https://git-scm.com/docs/git-init) |
   | status | [Link](https://www.atlassian.com/git/tutorials/inspecting-a-repository) | [Link](https://git-scm.com/docs/git-status) |
   | diff | [Link](https://www.atlassian.com/git/tutorials/saving-changes/git-diff) | [Link](https://git-scm.com/docs/git-diff) |
   | add | [Link](https://www.atlassian.com/git/tutorials/saving-changes) | [Link](https://git-scm.com/docs/git-add) |
   | commit | [Link](https://www.atlassian.com/git/tutorials/saving-changes/git-commit) | [Link](https://git-scm.com/docs/git-commit) |
   | remote | [Link](https://www.atlassian.com/git/tutorials/syncing) | [Link](https://git-scm.com/docs/git-remote) |
   | push | [Link](https://www.atlassian.com/git/tutorials/syncing/git-push) | [Link](https://git-scm.com/docs/git-push) |
- using VSCode to update project files, including the following:
  - module_sample.py
  - config_log.py
  - README.md
  - LICENSE.txt
- using [Python style coding conventions](https://peps.python.org/pep-0008/) to improve code readability, usability, and sustainability, including [function annotations](https://peps.python.org/pep-0008/#function-annotations), [type hints](https://peps.python.org/pep-0484/), [variable annotations](https://peps.python.org/pep-0008/#variable-annotations), and [variable annotation syntax](https://peps.python.org/pep-0526/)
- using [Python docstring conventions](https://peps.python.org/pep-0257/) for modules and functions to improve readability, usability, and testability
- using common and unexpected [exception trapping](https://docs.python.org/3/tutorial/errors.html) (i.e. error handling) to improve usability, testability, plus debugability with easy-to-understand and actionable messages 
- [importing](https://docs.python.org/3/reference/import.html) from [The Python Standard Library](https://docs.python.org/3/library/index.html) to efficiently integrate credible functionality (i.e. broadly reviewed, tested, and trusted by community members), including the following:
  - providing a command line interface for module config_log.py's help and usage information, which improves module usability and testability, by using [argparse library](https://docs.python.org/3/library/argparse.html) (See `py config_log.py -h`)
  - logging to either stderr or file depending on user input, plus short "FYI" messages (e.g. info, debug) versus more detailed "alert" messages (e.g. warning, error, critical), which improves testability and debugability, using [logging library](https://docs.python.org/3/library/logging.html) plus [logging "how-to" references](https://docs.python.org/3/howto/logging.html#loggers) to learn about [flow](https://docs.python.org/3/howto/logging.html#logging-flow), [levels](https://docs.python.org/3/howto/logging.html#logging-levels), [handlers](https://docs.python.org/3/library/logging.handlers.html), [records](https://docs.python.org/3/library/logging.html#logging.LogRecord), [filters](https://docs.python.org/3/library/logging.html#filter-objects), plus [formatters](https://docs.python.org/3/howto/logging.html#formatters) (both [date formatting](https://docs.python.org/3/library/time.html#time.strftime) and [record formatting](https://docs.python.org/3/library/logging.html#logrecord-attributes))
- importing from inter-application modules to reuse developed functionality

.

## **Background**

Lance Hegland wanted to test his local development environment, including the following tools:

- VSCode
- Python
- Git
- GitHub

.

## **Known Issues**

None

.

## **Requirements**

1. Familiarity and access to recent versions of the following development tools:
   | Tool                         | Download | Reference | with VSCode |
   |------------------------------|----------|-----------|-------------|
   | VSCode | [Link](https://code.visualstudio.com/Download) | [Link](https://code.visualstudio.com/learn) | |
   | + Markdown Preview Github Styling | [Link](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-preview-github-styles) | | |
   | + GitHub Pull Requests and Issues | [Link](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) | | |
   | + Python Tools | [Link](https://marketplace.visualstudio.com/items?itemName=ms-python.python) | | |
   | Python | [Link](https://www.python.org/downloads/) | [Link](https://wiki.python.org/moin/BeginnersGuide) | [Link](https://code.visualstudio.com/docs/languages/python) |
   | Git | [Link](https://git-scm.com/downloads) | [Link](https://git-scm.com/videos) | [Link](https://vscode.github.com/) |
   | GitHub  | | [Link](https://github.com) | [Link](https://code.visualstudio.com/docs/sourcecontrol/github) |

.

## **Installation**

1. Review [README.md](https://github.com/LHHegland/python_examples/blob/master/README.md) for GitHub user [LHHegland](https://github.com/LHHegland) repository [python_examples](https://github.com/LHHegland/python_examples)
1. Perform the necessary actions to satisfy [minimum requirements](https://github.com/LHHegland/python_examples/blob/master/README.md#requirements).
1. From your local projects directory, copy the entire remote GitHub repository LHHegland/python_examples into a local working area (`git clone git@github.com:LHHegland/python_examples.git`)

.

## **Configuration**

None

.

## **Usage**

Use VSCode, Markdown, Python, Git, and GitHub tools and code examples as you do the following:

1. Use VSCode to create a Python module hello_world
1. Use VSCode to create a Python module (e.g. user_greeting) that asks for the users full name (e.g. Pat Smith) and returns the message "Hi, {first_name}!" (E.g. "Hi, Pat!").
1. Create a Python module (e.g. logging_display) that uses the [logging library](https://docs.python.org/3/library/logging.html) to display logging messages (e.g. info, debug, warning, error, critical) to the user's screen (e.g. stderr).
1. Create a Python module (e.g. logging_file) that uses the [logging library](https://docs.python.org/3/library/logging.html) to record logging messages (e.g. info, debug, warning, error, critical) in a specific file (e.g. my.log).
1. Create a single Python module (e.g. logging_both) that uses the [logging library](https://docs.python.org/3/library/logging.html) to either display or store logging messages depending on the command line options or function parameters provided by the user; combining the functionality of logging_display and logging_file.
1. Update your Python module logging_both to include exception trapping [exception trapping](https://docs.python.org/3/tutorial/errors.html) (i.e. error handling) to improve usability, testability, plus debugability with easy-to-understand and actionable messages.
1. Update your Python module logging_both to include a command line interface to display help and usage information, which improves module usability and testability, by using [argparse library](https://docs.python.org/3/library/argparse.html) (See `py config_log.py -h`)
1. Update your user greeting module to include logging.
1. Review and update your modules for conformance with the following:
   1. [Python style coding conventions](https://peps.python.org/pep-0008/) to improve code readability, usability, and sustainability, including [function annotations](https://peps.python.org/pep-0008/#function-annotations), [type hints](https://peps.python.org/pep-0484/), [variable annotations](https://peps.python.org/pep-0008/#variable-annotations), and [variable annotation syntax](https://peps.python.org/pep-0526/)
   1. [Python docstring conventions](https://peps.python.org/pep-0257/) for modules and functions to improve readability, usability, and testability
1. Create a README document using Markdown language
1. [Choose an open source license](https://choosealicense.com/) and copy the text into a LICENSE.txt file
1. Create and push your Python example package to a newly created remote repository in your GitHub account.
   1. From your local working area with your newly created files, initialize your local repository (`git init`)
   1. Update working area to staging area (`git add --verbose --all`)
   1. Review differences: working vs. staging vs. commits
      1. Review file differences between last commit vs staging areas vs working area (`git status`)
      1. Review file line differences between staging area vs working area (`git diff`)
      1. Review differences to be committed (file line differences between last commit vs staging area) (`git diff --cached`)
   1. Update staging area to commits area (`git commit --message="Initial Commit with Base Files"`)
   1. Review differences: working vs. staging vs. commits
      1. Review differences between last commit vs staging areas vs working area (`git status`)
      1. Review file line differences between staging area vs working area (`git diff`)
      1. Review file line differences to be committed (last commit vs staging area) (`git diff --cached`)
      1. Review file line differences between last commit vs working area (`git diff HEAD`)
      1. Review commit history (`git log --oneline`)
      1. Review commit change summary by file (`git log --stat`)
      1. Review brief commit messages by author (`git shortlog`)
      1. Review commit diagram (`git log --graph --oneline --decorate`)
      1. Review commit changes by file (`git log -p`)
   1. [Create remote GitHub repository](https://github.com/) my_python_examples
   1. Connect to that remote repository (`git remote add origin git@github.com:your_username/my_python_examples.git`)
   1. Verify remote repository (`git remote -v`)
   1. Review existing branches (`git branch --list`)
   1. Update remote repository (`git push -u origin master`)
.

## **Authors**

- Lance Hegland ([lance.hegland@gmail.com](mailto:lance.hegland@gmail.com))

.

## **Roadmap**

None

.

## **License**

GNU General Public License v3.0 (GNU GPLv3)

- See [LICENSE.txt](LICENSE.txt)
- See [GNU General Public License v3.0 (GNU GPLv3)](https://choosealicense.com/licenses/gpl-3.0/)