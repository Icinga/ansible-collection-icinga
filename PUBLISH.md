# Creating a new release

> This is meant as an *internal* note on how to build and publish a new version of this Ansible Collection.

1. **Get the release branch ready:**  
   Push your local changes to the remote.  
   From your local release branch:  
   ```
   git push --set-upstream origin release/<VERSION>
   ```

   To avoid having leftover files from your local directory end up in the release, please **cleanly clone the release branch to another directory**.  
   ```
   git clone --branch release/<VERSION> git@github.com:Icinga/ansible-collection-icinga.git release_<VERSION>
   cd release_<VERSION>
   ```
   You now only have files that were actually commmited.  

2. **Increase the version number:**  
   The version of this Collection - as seen by Ansible Galaxy - is determined by **galaxy.yml**.  
   Increase the version number inside accordingly.   

3. **Create a changelog summary:**  
   This will be shown in the changelog as a short summary for this release.  

   changelogs/fragments/release_summary.yml:  
   ```
   release_summary: |
     Summary text for this release.
     "*Bugfix release*" for example.
   ```

4. **Create a new changelog:**  
   Lint the changelogs:  
   ```
   antsibull-changelog lint
   ```

   Generate the changelog:  
   ```
   antsibull-changelog release --version <VERSION>
   ```

   Commit your changes to the release branch.

5. **Build and push to Ansible Galaxy:**  
   Build a release tar ball (verbose shows skipped files):  
   ```
   ansible-galaxy collection build -vvv
   ```

   Push to Ansible Galaxy:  
   ```
   ansible-galaxy collection publish --token <TOKEN> icinga-icinga-<VERSION>.tar.gz
   ```
   > This might show errors which does **not** necessarily mean that it failed.  
   > Have a look at [Ansible Galaxy](https://galaxy.ansible.com/ui/repo/published/icinga/icinga/) and confirm if the release could be published.

6. **Create a release on GitHub:**  
   When [creating a new release](https://github.com/Icinga/ansible-collection-icinga/releases/new)  

   - choose \<VERSION\> as tag
   - choose the branch "release/\<VERSION\>" as target (will be tagged)
   - choose \<VERSION\> as title
   - copy and paste the release's changelog entry (see [prior releases](https://github.com/Icinga/ansible-collection-icinga/releases))
   - attach the created tar ball (icinga-icinga-\<VERSION\>.tar.gz) to the release
   - if you feel extra nice, credit contributors by adding their names, e.g. behind the respective issue or feature (`@name`)
