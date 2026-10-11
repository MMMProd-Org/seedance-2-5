# Releasing the skill

The model name is **Seedance 2.5**. The downloadable skill has a separate
version, starting at **1.0.0**. Its only version source is
[skills/seedance-2-5/VERSION](../skills/seedance-2-5/VERSION), also included in
every ZIP and .skill download.

## Prepare a version in a pull request

1. Make the skill changes in your branch.
2. Increase VERSION: three numbers, no leading zeros, followed by one newline.
   Use a patch for fixes, a minor version for compatible additions, and a major
   version for incompatible changes.
3. Rebuild the committed downloads, then validate:

```sh
python3 -B scripts/package_skill.py
python3 -B -m unittest discover -s tests -v
python3 -B scripts/package_skill.py --check
python3 -B scripts/release_skill.py --check --base FULL_PR_BASE_SHA
```

The last command prints the validated version and uses no network or writes.
Without --base it compares against HEAD's first parent, covering one commit.
For an uncommitted change, PR or several commits, supply the full base commit
SHA to compare all intended changes. The workflow supplies the PR base for
pull requests and the pre-push commit for pushes. Both its check and publication
jobs use that pre-push base, so a final documentation commit cannot hide an
earlier skill or version change in the same push.

Change VERSION whenever the skill or its downloads change. Reusing or lowering
a version fails the check. A README-only change keeps the existing version and
does not republish a release already present.

## What happens after merge

[Skill checks](../.github/workflows/check.yml) runs the tests, checks the committed
downloads and validates the version. Its dependent publication job runs only on
a push to main in MMMProd-Org/seedance-2-5.

For a new version, the job:

1. Targets the exact checked commit, prepares a draft vMAJOR.MINOR.PATCH and
   includes the version, full commit SHA and GitHub-generated change notes.
2. Uploads seedance-2-5.zip, seedance-2-5.skill and SHA256SUMS to that release ID.
3. Downloads and compares every asset, including size and any provided digest.
4. Publishes using GitHub's native `make_latest: legacy` selection, then reads
   back the public release, commit tag and all three files.

The creation response supplies the release ID. The publisher keeps that ID for
uploads and subsequent reads, checking the tag, target commit and draft state
at each stage. It does not require a newly created or updated release to appear
immediately in the release listing. An existing draft found by version is read
again by ID before any upload. API errors remain failures; no delay or retry is
used to conceal an incomplete listing.

Both archives have identical bytes and the same internal seedance-2-5 folder.
SHA256SUMS records the SHA-256 of each archive. On Linux, macOS or WSL, download
the three assets to one folder and run:

```sh
sha256sum --check SHA256SUMS
```

On native Windows, `Get-FileHash .\seedance-2-5.zip -Algorithm SHA256` returns
the ZIP's hash; compare it with the corresponding line in SHA256SUMS.

The publication job alone receives contents: write, through the native
GITHUB_TOKEN. No personal access token or repository-wide permission change is
required. The publisher rejects other event, repository, branch or checkout
contexts. Publication requires BASE_SHA from the push event; a missing, empty,
invalid or unknown base fails before any GitHub write. An explicit all-zero SHA
is treated as initialization without a previous reference, not as a missing
base. Workflow runs for different main commits are not cancelled; release
jobs serialize by version so separate versions retain their pending jobs.

## An interrupted or failed publication

A tag alone or a draft is **not** a published release. Check the workflow error
and the [release page](https://github.com/MMMProd-Org/seedance-2-5/releases).

A failed upload may leave a draft with some files. If the original commit's
code is sufficient and the cause is corrected, rerun that workflow. The script
checks existing files, uploads only missing files, and resumes publication. It never
replaces an asset, moves a tag or deletes a release. A draft for another commit,
a conflicting tag, a wrong digest or an API/permission error fails explicitly.

If the cause needs a code fix, merging the fix starts a new workflow with the
new code. Rerunning the old workflow still runs the old code; its draft also
belongs to the old commit and is rejected by the new job.

An empty, unpublished draft may be rebound only under an explicitly approved,
targeted recovery plan. Verify its exact identity, old target and Checked commit
line, that it has no assets or tag, that its old commit is an ancestor of the
new main commit, and that the skill and downloads are identical between those
commits. The PR checks and the new main checks must pass first. Change only its
target and Checked commit line, preserving all other metadata, then verify the
response and rerun the new workflow once. Stop on any changed precondition or
failure. The publisher does not automate this exception; populated drafts and
published releases are never rebound by this procedure.

An identical public release is verified without any new write. An interrupted
job that published before failing can therefore be rerun safely. Do not create
a second release manually, increase the version to conceal a failure, or
weaken the checks. A conflict needs diagnosis.

## Verification boundary

Local tests simulate GitHub, force interruptions and use temporary Git
repositories. They validate the publication decisions and requests, including
the native latest policy; they do not prove the remote service's behavior.
Actual publication requires a successful main workflow and live verification
of the public release, its tag and assets. The direct ZIP link in each README
remains available before the first release and if publication fails.

Primary references, GitHub (accessed 11 October 2026):
[release creation](https://docs.github.com/en/rest/releases/releases#create-a-release),
[release reads by ID](https://docs.github.com/en/rest/releases/releases#get-a-release),
[asset upload](https://docs.github.com/en/rest/releases/assets#upload-a-release-asset),
[release update and latest policy](https://docs.github.com/en/rest/releases/releases#update-a-release),
[workflow token permissions](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token).
