# Contributing
A roadmap of this project is located at https://github.com/Icinga/ansible-collection-icinga/milestones. Please consider
this roadmap when you start contributing to the project.

Before starting your work on this module, you should [fork the project] to your GitHub account. This allows you to
freely experiment with your changes. When your changes are complete, submit a [pull request]. All pull requests will be
reviewed and merged if they suit some general guidelines:

* Changes are located in a topic branch
* For new functionality, proper tests are written
* Changes should not solve certain problems on special environments

## Signing our CLA

When creating a Pull Request (PR) within one of our projects on GitHub, you will be automatically asked to sign our [CLA]. You only have to sign the [CLA] once and it will apply to all of our projects.

## Branches
Choosing a proper name for a branch helps us identify its purpose and possibly find an associated bug or feature.
Generally a branch name should include a topic such as `fix` or `feature` followed by a description and an issue number
if applicable. Branches should have only changes relevant to a specific issue.

```
git checkout -b fix/service-template-typo-1234
git checkout -b feature/config-handling-1235
git checkout -b doc/fix-typo-1236
```

## Testing
Python modules are unit tested with the Python Standard Library. For integration tests we use [Molecule]. When modifying
existing modules or tasks, make sure all existing tests pass. If you add new functionality, make sure to write appropriate
tests as well.

[fork the project]: https://help.github.com/articles/fork-a-repo/
[pull request]: https://help.github.com/articles/using-pull-requests/
[Molecule]: https://github.com/ansible-community/molecule/
[CLA]: https://icinga.com/company/contributor-agreement/
